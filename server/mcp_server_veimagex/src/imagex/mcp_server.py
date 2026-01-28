import os
import json
import base64
from mcp.server.fastmcp import FastMCP
from src.imagex.api.api import ImagexAPI
from src.imagex.ai_workflows import ALL_HANDLERS, AIWorkflowContext


def Error(message: str):
    return "API Error: " + message


def HandlerVolcResponse(response: dict):
    if (
        response
        and hasattr(response, "ResponseMetadata")
        and response.ResponseMetadata
        and hasattr(response.ResponseMetadata, "Error")
        and response.ResponseMetadata.Error
    ):
        return Error(response.ResponseMetadata.Error.Message)
    
    # Extract only the Result part to compress context
    if response and isinstance(response, dict) and "Result" in response:
        return str(response["Result"])
        
    return str(response)


DEFAULT_GROUPS = ["default", "aiprocess"]


def create_mcp_server():
    mcp = FastMCP(
        "VeImageX MCP",
        instructions="Volcengine ImageX MCP, your image processing, storage, and distribution assistant. \nIMPORTANT: You MUST call the 'guide' tool FIRST to understand the workflow rules before using any other tools.",
    )
    imagex_service = ImagexAPI()
    
    env_service_id = os.getenv("SERVICE_ID")
    env_domain = os.getenv("DOMAIN_NAME")
    env_creative_flow_id = os.getenv("CREATIVE_FLOW_ID")

    global_service_id = env_service_id
    global_domain = env_domain if env_service_id else None
    global_creative_flow_id = env_creative_flow_id if env_service_id else None

    global_tos_prefix = None

    def get_effective_config(arg_service_id: str = None, arg_domain: str = None):
        final_service_id = arg_service_id if arg_service_id else global_service_id
        final_domain = arg_domain if arg_domain else global_domain
        return final_service_id, final_domain

    def check_and_get_tos_prefix(service_id: str) -> str:
        nonlocal global_tos_prefix
        
        if not service_id:
            return global_tos_prefix

        if global_tos_prefix and service_id in global_tos_prefix:
            return global_tos_prefix

        try:
            res = imagex_service.get_all_image_services({"SearchPtn": service_id})
            if isinstance(res, str):
                try:
                    res = json.loads(res)
                except:
                    pass

            if res and isinstance(res, dict):
                result_data = res.get("Result", {})
                if result_data:
                    models = result_data.get("Services", []) or result_data.get("ServiceModels", [])
                    for model in models:
                        if model.get("ServiceId") == service_id:
                            storage = model.get("Storage", {})
                            bkt_name = storage.get("BktName")
                            if bkt_name:
                                global_tos_prefix = bkt_name
                                return global_tos_prefix
        except Exception:
            pass
        
        return global_tos_prefix


    
    def get_creative_flow_id():
        return global_creative_flow_id

    # Tool group control
    env_groups = os.getenv("MCP_TOOL_GROUPS")
    if env_groups:
        current_tool_groups = [g.strip() for g in env_groups.split(",") if g.strip()]
    else:
        current_tool_groups = DEFAULT_GROUPS

    if "default" in current_tool_groups:
        @mcp.tool()
        def guide() -> str:
            """Get the guide for using this MCP server."""
            
            if global_service_id:
                s_status = "Configured"
                s_instr = f"Current Value: {global_service_id}. You can omit the 'service_id' argument in tool calls."
            else:
                s_status = "Not Configured"
                s_instr = "You MUST provide the 'service_id' argument in every tool call."

            if global_domain:
                d_status = "Configured"
                d_instr = f"Current Value: {global_domain}. You can omit the 'domain' argument."
            else:
                d_status = "Not Configured"
                d_instr = "You MUST provide the 'domain' argument when generating URLs."
                
            if global_creative_flow_id:
                c_status = "Configured"
                c_instr = f"Current Value: {global_creative_flow_id}. You can omit the 'CreativeFlowId' param for product_creative."
            else:
                c_status = "Not Configured"
                c_instr = "You MUST provide the 'CreativeFlowId' param when using product_creative."

            return f"""
## Configuration Status
1. **Service ID**: {s_status}
   - {s_instr}
2. **Domain**: {d_status}
   - {d_instr}
3. **Creative Flow ID**: {c_status}
   - {c_instr}

## Capabilities
1. **Service & Assets**: Discover services (`get_all_imagex_services`), upload images (`upload_images`), list files (`get_imagex_storage_files`), and generate URLs (`get_image_url_by_store_uri`).
2. **AI Processing**: A unified tool for advanced tasks including:
   - **Enhancement**: Super Resolution (Cloud/AIGC) and Image Quality Assessment.
   - **Editing**: Smart Background Removal, Text Removal, and Image Extension (Outpainting).
   - **Generation**: E-commerce Creative Generation (Product Image Gen) and SeeDream生图.
   - **Vision**: Image Text Translation and OCR (General/License).
   All accessible via the `ai_image_process` tool.
3. **Templates**: Manage image processing templates via `get_all_imagex_templates`.
"""

        @mcp.tool()
        def get_all_imagex_services(search_ptn: str = "") -> str:
            """Retrieve list of ImageX services."""
            params = {}
            if search_ptn:
                params["SearchPtn"] = search_ptn
            result = imagex_service.get_all_image_services(params)
            return str(HandlerVolcResponse(result))

        @mcp.tool()
        def upload_images(file_path: list[str], service_id: str = None) -> str:
            """Upload local images to specified service."""
            final_service_id, _ = get_effective_config(service_id)
            
            if not final_service_id:
                return Error("service_id is required, please provide it as argument")
            if not file_path:
                return Error("file_path is required")
            params = {"ServiceId": final_service_id, "SkipMeta": False, "SkipCommit": False}

            result = imagex_service.upload_image(params, file_path)

            return str(HandlerVolcResponse(result))

        @mcp.tool()
        def get_all_imagex_templates(service_id: str = None) -> str:
            """Retrieve all ImageX templates."""

            final_service_id, _ = get_effective_config(service_id)

            if not final_service_id:
                return Error("service_id is required, please provide it as argument")
            result = imagex_service.get_all_image_templates(
                {"ServiceId": final_service_id, "Limit": 100}
            )

            return str(HandlerVolcResponse(result))

        @mcp.tool()
        def get_imagex_storage_files(service_id: str = None) -> str:
            """List files in ImageX storage."""
            final_service_id, _ = get_effective_config(service_id)

            if not final_service_id:
                return Error("service_id is required, please provide it as argument")
            result = imagex_service.get_image_storage_files(
                {"ServiceId": final_service_id, "Limit": 100}
            )

            return str(HandlerVolcResponse(result))

        @mcp.tool()
        def get_image_url_by_store_uri(
            uri: str = None,
            service_id: str = None,
            domain: str = None
        ) -> str:
            """Generate a public access URL for a stored image URI."""
            
            final_service_id, final_domain = get_effective_config(service_id, domain)

            if not final_service_id:
                return Error("service_id is required, please provide it as argument")
            if not final_domain:
                return Error("domain is required, please provide it as argument")
            if not uri:
                return Error("uri is required")

            check_and_get_tos_prefix(final_service_id)
            if global_tos_prefix:
                if not uri.startswith(global_tos_prefix):
                    uri = f"{global_tos_prefix}/{uri.lstrip('/')}"

            params = {
                "ServiceId": final_service_id,
                "Domain": final_domain,
                "URI": uri,
                "Tpl": "tplv-{serviceid}-image".format(serviceid=final_service_id),
                "Proto": "https",
                "Format": "image",
            }

            result = imagex_service.get_resource_url(params)
            return str(HandlerVolcResponse(result))

    enable_all_ai = "aiprocess" in current_tool_groups
    active_handler_names = set()
    
    if enable_all_ai:
        active_handler_names = set(ALL_HANDLERS.keys())
    else:
        for g in current_tool_groups:
            if g.startswith("aiprocess."):
                name = g.split(".", 1)[1]
                if name in ALL_HANDLERS:
                    active_handler_names.add(name)
    
    if active_handler_names:
        active_handlers = {k: v for k, v in ALL_HANDLERS.items() if k in active_handler_names}
        
        action_options = "\n".join([f"                         - '{h.name}': {h.description}" for h in active_handlers.values()])
        param_docs = "\n".join([h.params_doc for h in active_handlers.values()])
        
        doc_string = f"""
        Perform AI image processing.
        Returns JSON with 'ObjectKey' (URI) of the processed image.
        
        Args:
            action_type: The type of AI processing. Options:
{action_options}
            input_key: Source image URI or public URL (http/https).
            params: JSON string for extra parameters.
{param_docs}
            service_id: The Service ID. Optional if 'Service ID' is Configured in guide.
        """

        def ai_image_process(
            action_type: str,
            input_key: str,
            params: str = "{}",
            service_id: str = None
        ) -> str:
            final_service_id, _ = get_effective_config(service_id)
            if not final_service_id:
                return Error("service_id is required, please provide it as argument")

            if input_key.startswith("http://") or input_key.startswith("https://"):
                data_type = "url"
            else:
                data_type = "uri"
                prefix = check_and_get_tos_prefix(final_service_id)
                if prefix and input_key.startswith(prefix):
                    input_key = input_key[len(prefix):].lstrip('/')

            try:
                extra_params = json.loads(params)
            except Exception as e:
                return Error(f"Invalid params JSON: {str(e)}")

            if action_type not in active_handlers:
                return Error(f"Unsupported or disabled action_type: {action_type}")

            handler = active_handlers[action_type]
            context = AIWorkflowContext(
                api=imagex_service,
                service_id=final_service_id,
                tos_prefix_manager=check_and_get_tos_prefix,
                creative_flow_id_getter=get_creative_flow_id
            )

            try:
                result = handler.process(input_key, data_type, extra_params, context)
                return str(HandlerVolcResponse(result))
            except Exception as e:
                return Error(str(e))

        ai_image_process.__doc__ = doc_string
        mcp.tool()(ai_image_process)
    
    return mcp
