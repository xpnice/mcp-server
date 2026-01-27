# coding:utf-8
import os
from .base_trait import BaseTrait  # Modify it if necessary


class BaseService(BaseTrait):
    def __init__(self, region=None, ak=None, sk=None, service_info_map=None,):
        if region is None:
            if os.getenv("VOLCENGINE_REGION") is None:
                region = "cn-north-1"
            else:
                region = os.getenv("VOLCENGINE_REGION")
        super().__init__({
            'ak': ak,
            'sk': sk,
            'region': region,
            'service_info_map': service_info_map
        })
  