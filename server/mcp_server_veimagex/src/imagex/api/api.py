import os
from volcengine.imagex.v2.imagex_service import ImagexService
from .config import *
import json


class ImagexAPI(ImagexService):
    def __init__(self, ak=None, sk=None, session_token=None, region=None, service_id=None, domain=None):
        if region is None:
            region = os.getenv("VOLCENGINE_REGION", "cn-north-1")
        super().__init__(region=region)
        
        # Priority: arguments > environment variables
        final_ak = ak if ak else os.getenv("VOLCENGINE_ACCESS_KEY")
        final_sk = sk if sk else os.getenv("VOLCENGINE_SECRET_KEY")
        final_token = session_token if session_token else os.getenv("VOLCENGINE_SESSION_TOKEN")
        
        self.set_ak(final_ak)
        self.set_sk(final_sk)
        if final_token:
            self.set_session_token(final_token)
            
        self.service_info.header["x-tt-mcp"] = 'volc'
        self.api_info = {**self.api_info, **api_info}
        
        self.service_id = service_id if service_id else os.getenv("SERVICE_ID")
        self.domain = domain if domain else os.getenv("DOMAIN_NAME")
        
        self.set_connection_timeout(100)
        self.set_socket_timeout(100)

    def mcp_get(self, action, params={}, doseq=0):
        res = self.get(action, params, doseq)
        if res == "":
            raise Exception("%s: empty response" % action)
        res_json = json.loads(json.dumps(res))
        return res_json

    def mcp_post(self, action, params={}, body={}):
        if not body:
            body = {}
        res = self.json(action, params, json.dumps(body))
        if res == "":
            raise Exception("%s: empty response" % action)
        res_json = json.loads(json.dumps(res))
        return res_json

    def get_all_image_services(self, params):
        return self.mcp_get("McpGetAllImageServices", params)

    def get_all_image_templates(self, params):
        return self.mcp_get("McpGetAllImageTemplates", params)

    def get_image_storage_files(self, params):
        return self.mcp_get("McpGetImageStorageFiles", params)


    def get_resource_url(self, params):
        return self.mcp_get("McpGetResourceURL", params)

    def post_ai_process(self, body):
        return self.mcp_post("McpAIProcess", {}, body)
