# veImageX MCP Server

The MCP Server implementation for veImageX provides clients with the capability to interact with Volcano Engine's veImageX service. It enables natural language-based management of veImageX cloud resources, service information queries, and integrates various image processing capabilities including text-to-image generation, AIGC image translation, image expansion, and more.

| Version | v0.2.0                   | 
|---------|--------------------------|
| Description | Manage veImageX resources and process images via MCP |
| Category | Video Cloud               |
| Tags | Image Processing, Asset Hosting |

## Features (Tools)

This MCP Server provides the following core tools:

### Base Management Tools
- **guide**: Get the guide for using this MCP server (**Recommended to call first**).
- **get_all_imagex_services**: Retrieve all service information (Service ID, Bucket, Domain, etc.).
- **upload_images**: Upload local images to a specified service.
- **get_all_imagex_templates**: Retrieve all image templates under a specified service.
- **get_imagex_storage_files**: List files in storage.
- **get_image_url_by_store_uri**: Generate a public access URL for a specified asset.

### AI Image Processing Tool (ai_image_process)
An all-in-one tool that executes different AI tasks by specifying an `action_type`. Supported capabilities include:
- **cloud_sr**: Cloud Super Resolution (2-8x zoom).
- **smart_expansion**: Intelligent Image Extension (outpainting).
- **aigc_sr**: AIGC Super Resolution (detail enhancement).
- **translate**: AIGC Image Translation (supports 30+ languages).
- **quality_assessment**: Large Model Image Quality Assessment.
- **product_creative**: E-commerce Creative Generation (product image generation).
- **remove_text**: E-commerce Text Removal.
- **ocr**: Optical Character Recognition (OCR).
- **remove_bg**: Smart Background Removal (segmentation).
- **seedream**: ImageX-SeeDream Generation.

## Environment Variables

You can configure the MCP server using the following environment variables:

| Variable | Description | Required |
| :--- | :--- | :--- |
| `VOLCENGINE_ACCESS_KEY` | Volcano Engine account ACCESS KEY | Yes |
| `VOLCENGINE_SECRET_KEY` | Volcano Engine account SECRET KEY | Yes |
| `SERVICE_ID` | Default veImageX service ID | Recommended |
| `DOMAIN_NAME` | Default veImageX domain | Recommended, using the default acceleration domain configured in the service is highly recommended. |
| `CREATIVE_FLOW_ID` | Default Creative Flow ID for product_creative | Optional |
| `MCP_TOOL_GROUPS` | Tool group configuration, supports secondary grouping | Default: `default,aiprocess` |

### Secondary Grouping Loading
To reduce context pressure on the client, you can specify specific AI capabilities via `MCP_TOOL_GROUPS`:
- `aiprocess`: Load all AI capabilities.
- `aiprocess.ocr,aiprocess.translate`: Load only OCR and translation capabilities.

## Installation & Deployment

### System Requirements
- Python 3.11 or higher.
- [uv](https://astral.sh/uv/).

### Running Locally

**Using uvx (Recommended)**
If you have [uv](https://astral.sh/uv/) installed, you can run it directly:
```bash
# Start in Stdio mode (Default)
uvx mcp-server-veimagex
# Start in SSE mode (HTTP URL access)
uvx mcp-server-veimagex --transport sse --port 8000
# Start in Streamable HTTP mode
uvx mcp-server-veimagex --transport streamable-http --port 8000
```

**Using uv with source code**
```bash
uv sync
# Start in Stdio mode (Default)
uv run mcp-server-veimagex
# Start in SSE mode
uv run mcp-server-veimagex --transport sse --port 8000
# Start in Streamable HTTP mode
uv run mcp-server-veimagex --transport streamable-http --port 8000
```

## Client Configuration (Example)

### Trae / Cursor / Claude Desktop
Add the following configuration to your MCP settings file:

**Using uvx (Recommended)**
```json
{
  "mcpServers": {
    "veimagex": {
      "command": "uvx",
      "args": ["mcp-server-veimagex"],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "Your Volcano Engine AK",
        "VOLCENGINE_SECRET_KEY": "Your Volcano Engine SK",
        "SERVICE_ID": "Your Default Service ID",
        "DOMAIN_NAME": "Your Default Domain",
        "CREATIVE_FLOW_ID": "Your Default Creative Flow ID",
        "MCP_TOOL_GROUPS": "default,aiprocess"
      }
    }
  }
}
```

**Using Python directly**

## Compatible Platforms
Ark, Trae, cursor

## Service Activation
<https://console.volcengine.cn/imagex>

## License
MIT
