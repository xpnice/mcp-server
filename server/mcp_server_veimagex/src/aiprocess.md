提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。
## 注意事项
- 请求频率：单用户请求频率限制为 **1 次/秒**。
	
- 超时时间：超时时间为 **30 秒**。
	
- 服务地址：本接口仅支持在中国区域调用，对应 region 为 `cn-north-1`，详情参看[调用方法](https://www.volcengine.com/docs/508/14106)。
## 请求说明
- 请求方式：**POST**
- 请求地址：**https://imagex.volcengineapi.com/?Action=AIProcess&Version=2023-05-01**
## 请求参数
下表仅列出该接口特有的请求参数和部分公共参数。更多信息请见[公共请求参数](https://www.volcengine.com/docs/508/14106#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)。
### Query
| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
| ---- | ---- | ---- | ---- | ---- |
| Action | String | 是 | `AIProcess` | 接口名称。当前 API 的名称为 `AIProcess`。 |
| Version | String | 是 | `2023-05-01` | 接口版本。当前 API 的版本为 `2023-05-01`。 |
### Body
| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
| ---- | ---- | ---- | ---- | ---- |
| ServiceId | String | 是 | `91**2g` | 服务 ID。 |\
|  |  |  |  | * 您可以在 veImageX 控制台[服务管理](https://console.volcengine.com/imagex/service_manage/)页面，在创建好的图片服务中获取服务 ID。 |\
|  |  |  |  | * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考[获取所有服务信息](https://www.volcengine.com/docs/508/9360)。 |
| WorkflowTemplateId | String | 是 | `system_workflow_ai_super_resolution` | AI 图像处理模板 ID。 |\
|  |  |  |  | 附加组件不同，模板 ID 不同，详见开发指南 > 附加组件 2.0 目录下的各组件文档。 |
| WorkflowParameter | String | 是 | `{"Input":{"ObjectKey":"example.webp","DataType":"uri"},"GenDREnhanceParam":{"ModelId":"ai_sr_model_v2","Multiple":1.2}}` | AI 图像处理模板参数，需要将 JSON 压缩并转义为字符串。 |\
|  |  |  |  | 附加组件不同，参数取值不同，详见开发指南 > 附加组件 2.0 目录下的各组件文档。|
## 返回参数
下表仅列出本接口特有的返回参数。更多信息请见[公共返回参数](https://www.volcengine.com/docs/508/14106#%E5%85%AC%E5%85%B1%E8%BF%94%E5%9B%9E%E5%8F%82%E6%95%B0)。
| 参数 | 类型 | 示例值 | 描述 |
| ---- | ---- | ---- | ---- |
| Output | String | `{"ObjectKey":"veImageX-store/ai_super_resolution/67***a/example.webp","Size":54509,"Format":"webp"}` | AI 图像处理结果，是 JSON 压缩并转义后的字符串。 |\
|  |  |  | 附加组件不同，参数取值不同，详见开发指南 > 附加组件 2.0 目录下的各组件文档。 |
## 请求示例
```json
POST https://imagex.volcengineapi.com/?Action=AIProcess&Version=2023-05-01
{
    "ServiceId": "91**2g",
    "WorkflowTemplateId": "system_workflow_ai_super_resolution",
    "WorkflowParameter": "{\"Input\":{\"ObjectKey\":\"example.webp\",\"DataType\":\"uri\"},\"GenDREnhanceParam\":{\"ModelId\":\"ai_sr_model_v2\",\"Multiple\":1.2}}"
}
```
## 返回示例
```json
{
    "ResponseMetadata": {
        "RequestId": "20230604110420****100232280022D31",
        "Action": "AIProcess",
        "Version": "2023-05-01",
        "Service": "ImageX",
        "Region": "cn-north-1"
    },
    "Result": {
        "Output": "{\"ObjectKey\":\"veImageX-store/ai_super_resolution/67***a/example.webp\",\"Size\":54509,\"Format\":\"webp\"}"
    }
}
```

## 错误码
本接口无特有的错误码。更多信息请见[公共错误码](https://www.volcengine.com/docs/6369/68677)和 [veImageX 错误码](https://www.volcengine.com/docs/508/66156)。
