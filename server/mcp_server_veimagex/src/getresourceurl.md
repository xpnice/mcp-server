本接口支持获取指定服务下单个文件的原文件访问地址，若指定模板，可获取模板处理后结果图访问地址。
## 使用说明
若文件存储至素材托管服务下，则仅支持获取原图访问地址。若文件存储至图像处理服务下，默认情况下仅支持获取模板处理后结果图访问地址，如需获取原图访问地址，请开启[源地址访问](https://www.volcengine.com/docs/508/359448)。

:::tip
您可在控制台[服务管理](https://console.volcengine.com/imagex/service_manage/)或调用 [GetImageService](https://www.volcengine.com/docs/508/9358) 查询服务类型。
:::
## 注意事项
- 请求频率：单用户请求频率限制为 **10 次/秒**
- 超时时间：约为 **5 秒**。
- 服务地址：veImageX 在全球多个区域部署，每个区域有自己对应的 OpenAPI 域名，不支持跨区域调用。具体详情请查看[服务地址](https://www.volcengine.com/docs/508/14106#%E6%9C%8D%E5%8A%A1%E5%9C%B0%E5%9D%80)。
## 请求说明
- 请求方式：**GET**
- 请求地址：**https://imagex.volcengineapi.com/?Action=GetResourceURL&Version=2023-05-01**
## 请求参数
下表仅列出该接口特有的请求参数和部分公共参数。更多信息请见[公共请求参数](https://www.volcengine.com/docs/508/14106#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)。
### Query
| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
| ---- | ---- | ---- | ---- | ---- |
| Action | String | 是 | `GetResourceURL` | 接口名称。当前 API 的名称为 `GetResourceURL`。 |
| Version | String | 是 | `2023-05-01` | 接口版本。当前 API 的版本为 `2023-05-01`。 |
| ServiceId | String | 是 | `8h**9q` | 资源所在的服务 ID。可通过以下任一方式获取。 |\
|  |  |  |  | - 在[服务管理](https://console.volcengine.com/imagex/service_manage/)页面，获取服务 ID。 |\
|  |  |  |  | - 调用 [GetAllImageServices](https://www.volcengine.com/docs/508/9360) 接口，获取服务 ID。 |
| Domain | String | 是 | `example.test.com` | 域名。您可以通过调用 OpenAPI [获取服务下所有域名](https://www.volcengine.com/docs/508/9379)获取。 |
| URI | String | 是 | `tos-i-xxxxx/test.png` | 文件存储 Uri。您可以通过调用 OpenAPI [获取服务下的上传文件](https://www.volcengine.com/docs/508/9392)获取。 |
| Tpl | String | 否 | `tplv-8h**9q-1.image` | 模板名称，缺省情况下表示无模板处理图片。您可以通过调用 OpenAPI [获取服务下所有图片模板](https://www.volcengine.com/docs/508/9386)获取。 |\
|  |  |  |  | :::warning |\
|  |  |  |  | - 若 `ServiceId` 的服务类型为图像处理服务，则 `Tpl` 为**必填**。 |\
|  |  |  |  | - 若 `ServiceId` 的服务类型为素材托管服务，则 `Tpl` 为非必填。 |\
|  |  |  |  | ::: |
| Proto | String | 否 | `https` | 协议，默认为 http，隐私图片使用 https，公开图片支持取值 http 以及 https。 |
| Format | String | 否 | `image` | 创建模板时设置的图片输出格式，默认为 image，支持取值有： |\
|  |  |  |  | - image：表示输出原格式； |\
|  |  |  |  | - 静图格式：png、jpeg、heic、avif、webp; |\
|  |  |  |  | - 动图格式：awebp、heif、avis。 |
| Timestamp | Integer | 否 | `1800` | 过期时长，最大限制为 1 年，默认为 1800s。 |\
|  |  |  |  | :::tip |\
|  |  |  |  | 仅当开启 [URL 鉴权](https://www.volcengine.com/docs/508/128828)配置后，`Timestamp` 配置生效。 |\
|  |  |  |  | ::: |
## 返回参数
下表仅列出本接口特有的返回参数。更多信息请见[公共返回参数](https://www.volcengine.com/docs/508/14106#%E5%85%AC%E5%85%B1%E8%BF%94%E5%9B%9E%E5%8F%82%E6%95%B0)。
| 参数 | 类型 | 示例值 | 描述 |
| ---- | ---- | ---- | ---- |
| URL | String | `http://example.test.com/tos-i-xxxxx/test.png~tplv-8h**9q-1.image` | 结果图访问默认地址。 |
| CompactURL | String | `http://example.test.com/test.png~tplv-8h**9q-1.image` | 结果图访问精简地址，与默认地址相比缺少 Bucket 部分。 |
| ObjURL | String | `http://example.test.com/tos-i-xxxxx/test.png` | 默认源文件访问地址。 |
| ObjCompactURL | String | `http://example.test.com/test.png` | 精简源文件地址，与默认地址相比缺少 Bucket 部分。 |
## 请求示例
```json
GET https://imagex.volcengineapi.com/?Action=GetResourceURL&Version=2023-05-01&ServiceId=8h**9q&Domain=example.test.com&URI=tos-i-xxxxx/test.png&Tpl=tplv-8h**9q-1.image&Proto=https&Format=image&Timestamp=1800
```
## 返回示例
```json
{
    "ResponseMetadata": {
        "RequestId": "20230604110420****100232280022D31",
        "Action": "GetResourceURL",
        "Version": "2023-05-01",
        "Service": "ImageX",
        "Region": "cn-north-1"
    },
    "Result": {
        "URL": "http://example.test.com/tos-i-xxxxx/test.png~tplv-8h**9q-1.image",
        "CompactURL": "http://example.test.com/test.png~tplv-8h**9q-1.image",
        "ObjURL": "http://example.test.com/tos-i-xxxxx/test.png",
        "ObjCompactURL": "http://example.test.com/test.png"
    }
}
```

## 错误码
本接口无特有的错误码。更多信息请见[公共错误码](https://www.volcengine.com/docs/6369/68677)和 [veImageX 错误码](https://www.volcengine.com/docs/508/66156)。
## 服务端 SDK
为了方便您快速开发，veImageX 提供了配套的服务端 SDK，同时支持多种编程语言。建议您使用服务端 SDK 来调用 API，参考文档如下所示：

- [Golang SDK](https://www.volcengine.com/docs/508/23767)
- [Java SDK](https://www.volcengine.com/docs/508/152495)
- [Python SDK](https://www.volcengine.com/docs/508/176930)
## 历史版本
2018-08-01 版本 [GetResourceURL](https://www.volcengine.com/docs/508/132537) 接口文档现已停止维护，建议您参考本文档使用最新版本。
<div data-source="api-doc-hub" style="display: none"></div>