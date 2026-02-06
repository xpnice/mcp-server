AIGC 大模型超分辨率附加组件利用 AI 能力，在保证与原图内容一致的前提下，能够适当生成一些丢失的细节信息，提升图片整体画面的质感和观感。当原图画质中等或较差时，能够在去噪、去伪影的同时，保持和增加一些自然的纹理细节，显著提升清晰度。本文介绍如何使用 AIGC 大模型超分辨率附加组件。
<span id="d2bf9873"></span>
# 效果示例

| | | | \
|场景 |输入图 |生成示例结果 |
|---|---|---|
| | | | \
|风景 |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed26e21b435b4770924568d052337161~tplv-goo7wpa0wc-image.image =400x) |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ec079af391c74ba188d9874061894666~tplv-goo7wpa0wc-image.image =400x) |
| | | | \
|动物 |\
| |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fed6ed42cbe04f19b13268027baeb858~tplv-goo7wpa0wc-image.image =400x) |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cf5785ae4abc4adb989257f3a92692f4~tplv-goo7wpa0wc-image.image =400x) |
| | | | \
|美食 |\
| |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/075afc9e8e9f434eac94b6b52369de38~tplv-goo7wpa0wc-image.image =400x) |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f7ff4175a8094963a8c157ddd7a4daa4~tplv-goo7wpa0wc-image.image =400x) |
| | | | \
|建筑 |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bf49a745dd884406af608440188dcfa3~tplv-goo7wpa0wc-image.image =400x) |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bbb7260e40d9476aaee78359723ebd0e~tplv-goo7wpa0wc-image.image =400x) |
| | | | \
|商品 |\
| |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6e463c07fb36414d88b3e265d80e22a6~tplv-goo7wpa0wc-image.image =400x) |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c9af5c2e00c847d699efcbacd507b932~tplv-goo7wpa0wc-image.image =400x) |
| | | | \
|老照片 |\
| |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c7cd14d571ab431bbb0cb7f4fb22cf8d~tplv-goo7wpa0wc-image.image =400x) |![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d624525781844f069122ce71a2ed7195~tplv-goo7wpa0wc-image.image =400x) |

<span id="783b1e9f"></span>
# 使用场景
以下为 AIGC 大模型超分辨率的典型场景，该功能可以适用在任何图片类型，支持同分辨率和任意倍率的超分修复。

* **风景、建筑类**：针对草地、树叶、墙面等细节纹理做到很好的修复和还原
* **商品、美食类**：衣服、鞋子材质缺失，食材模糊不清缺少纹理等，可以进行适当生成和增强
* **人像、动物类**：提升人像发丝细节、肤质肌理，动物毛发等，使画面更有质感

<span id="77acc112"></span>
# 注意事项
超分修复模型可能无法完全适配以下场景。为避免对您的业务产生不利影响，建议您在使用前了解以下情况并准备备用方案：

* **艺术性模糊图片**：如果图片本身追求“虚化”、“模糊”、”朦胧感“等艺术效果，模型会将其变清晰，可能导致结果与您的预期不符。
* **含微小文字或人脸的图片**：处理这类图片时，修复结果中可能会出现结构错误。建议避免在此类场景中使用。

为确保能够生成图像，请满足以下限制。

* **输入分辨率**：短边 ⩾ 256 px，长边 ⩽ 2048 px。如果为其他分辨率，请先通过模板变更图片分辨率。
* **输入大小**：单张图 <= 10 MB。如果超出 10 MB，请先通过模板压缩图片大小。
* **输入格式**：.png、.jpg、.jpeg、.webp。如果为其他格式，请先通过模板变更图片格式。
* **输出分辨率**：长边 ⩽ 10240 px。可通过模板二次处理为其他分辨率。
* **输出格式**：.png、.jpg、.jpeg、.webp 等。可通过模板二次处理为其他格式。
* **缩放倍数**：<=30（支持浮点数）

<span id="bc239d8f"></span>
# 性能指标
以下性能数据来自实验室数据，供您参考。

* **处理耗时**：输出 1440 × 1440 分辨率图像，模型耗时 1s 左右。
* **图像体积**：相同编码参数的情况下，同分辨率增强，输出相比输入图像码率增加 69% 左右。
* **画质评分**：相同编码参数的情况下，同分辨率增强，使用火山引擎自研图像质量评分模型进行评分，输出相比输入图像分数增加 8.5 左右。

<span id="f6c6332d"></span>
# 使用方法
<span id="8f50a905"></span>
## 前提条件

* 已[开通 veImageX 产品服务](https://www.volcengine.com/docs/508/8084#%E5%BC%80%E9%80%9A-veimagex-%E4%BA%A7%E5%93%81%E6%9C%8D%E5%8A%A1)并[创建服务](https://www.volcengine.com/docs/508/357114)。
* 已开通[智能处理计费配置](https://www.volcengine.com/docs/508/1262340#%E5%BC%80%E9%80%9A%E6%99%BA%E8%83%BD%E5%A4%84%E7%90%86%E8%AE%A1%E8%B4%B9%E9%85%8D%E7%BD%AE)。
* （可选）如需完成以下操作，确保已[新建模板](/docs/508/8087)。
   * 处理输入图像：如果输入图像不符合输入限制，您可以通过模板来压缩图片大小或变更图片格式等，再将处理后的图片作为输入图像。
   * 处理生成图像：对生成的图像进行二次处理，例如添加水印或调整分辨率。

<span id="e2ec0b8c"></span>
## 步骤一：调用 AI 能力
<span id="f4d28b58"></span>
### 方式一：通过 API 调用
<span id="0b6bb58e"></span>
#### 同步处理
调用同步处理接口 [AIProcess](https://www.volcengine.com/docs/508/1515915)，提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。
**请求示例**
```JSON
POST https://imagex.volcengineapi.com/?Action=AIProcess&Version=2023-05-01
{
    "ServiceId": "91**2g", // 必选。服务 ID。
    "WorkflowTemplateId": "system_workflow_ai_super_resolution", // 必选。模板 ID。
    "WorkflowParameter": "{\"Input\":{\"ObjectKey\":\"example.webp\",\"DataType\":\"uri\"},\"GenDREnhanceParam\":{\"ModelId\":\"ai_sr_model_v2\",\"Multiple\":2}}" // 必选。模板参数。
}
```

其中，

* `ServiceId`：服务 ID，可从[服务管理](https://console.volcengine.com/imagex/service_manage/)页面获取。
* `WorkflowTemplateId`：取值固定为 `system_workflow_ai_super_resolution`。
* `WorkflowParameter`：根据[输入参数](/docs/508/1518358#81c85791)，设置该参数取值。

**返回示例**
```JSON
{
    "ResponseMetadata": {
        "RequestId": "20230604110420****100232280022D31",
        "Action": "AIProcess",
        "Version": "2023-05-01",
        "Service": "ImageX",
        "Region": "cn-north-1"
    },
    "Result": {
        "Output": "{\"ObjectKey\":\"a.webp\",\"Size\":54509,\"Format\":\"webp\"}"
    }
}
```

`Output` 的参数含义详见[输出参数](/docs/508/1518358#2fba069b)。
<span id="c68628e0"></span>
#### 异步处理
批量执行 AI 图像处理任务。
:::warning
确保已新建并启动批量处理任务队列。详见[步骤一：新建并启动任务队列](/docs/508/1749069#cdde5cc1)。
:::

1. 调用异步处理接口 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916)，创建批量处理任务。
   **请求示例**
   ```JSON
   POST https://imagex.volcengineapi.com/?Action=CreateImageAITask&Version=2023-05-01
   {
       "ServiceId": "5s****fo", // 必选。服务 ID。
       "DataType": "uri", // 必选。图片地址类型，支持取值 uri 和 url。
       "DataList": [
           "a.png",
           "uridemo.png"
       ], // 必选。图片 URI 或 URL 列表（URI 不包含 tos-*-i-* 前缀）。
       "CallbackConf": { // 可选。回调配置。
           "Method": "HTTP", // 必选。回调方式，取值固定为 HTTP。
           "Endpoint": "https://demo.com", // 必选。回调地址，用于接收处理结果。
           "DataFormat": "JSON", // 可选。回调数据格式，支持取值 XML 和 JSON。
           "Args": "product id", // 可选。业务自定义回调参数。
           "Type": "task" // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
       },
       "WorkflowParameter": "{\"GenDREnhanceParam\":{\"ModelId\":\"ai_sr_model_v2\",\"Multiple\":2}}", // 必选。模板参数。
       "WorkflowTemplateId": "system_workflow_ai_super_resolution", // 必选。模板 ID。
       "QueueId": "62f224ce61****826e38c29a" // 必选。队列 ID。
   }
   ```

   其中，
   * `WorkflowTemplateId`：取值固定为 `system_workflow_ai_super_resolution`。
   * `WorkflowParameter`：根据[输入参数](/docs/508/1518358#81c85791)，设置该参数取值。
   **返回示例**
   ```JSON
   {
       "ResponseMetadata": {
           "RequestId": "20230604110420****100232280022D31",
           "Action": "CreateImageAITask",
           "Version": "2023-05-01",
           "Service": "ImageX",
           "Region": "cn-north-1"
       },
       "Result": {
           "TaskId": "649b9d3****5537684010a7", // 任务 ID。
           "QueueId": "62f224ce61****826e38c29a" // 队列 ID。
       }
   }
   ```

2. 通过以下任一方式获取图像处理结果。
   * 回调通知：如果您在上一步设置了回调地址（`Endpoint`），则当任务完成后，veImageX 会向该回调地址发送回调消息。详见[回调](https://www.volcengine.com/docs/508/1526662)。
   * 主动查询：如果您未设置回调地址，调用 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913) 接口，获取图像处理结果。

<span id="78152646"></span>
### 方式二：通过服务端 SDK 调用
veImageX 提供了以下编程语言的 SDK，方便您调用 API。

```mixin-react
return (<Tabs>
<Tabs.TabPane title="Golang SDK" key="OGqjbJaZ0c"><RenderMd content={`<span id="b2119b4c"></span>
#### 前提条件
调用接口前，请先完成 Golang SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23757)操作。
<span id="e64164bb"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1518358#0b6bb58e)。
\`\`\`Go
package imagex_test

import (
        "context"
        "encoding/json"
        "fmt"
        "testing"

        "github.com/volcengine/volc-sdk-golang/base"
        imagex "github.com/volcengine/volc-sdk-golang/service/imagex/v2"
)

func Test_AIProcess(t *testing.T) {
        instance := imagex.NewInstance()

        instance.SetCredential(base.Credentials{
              // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
      // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
                AccessKeyID:     "ak",
                SecretAccessKey: "sk",
        })

        param := &imagex.AIProcessReq{
                AIProcessBody: &imagex.AIProcessBody{
                  ServiceID: "91**2g", // 必选。服务 ID。
                  WorkflowTemplateID: "system_workflow_ai_super_resolution",   // 必选。模板 ID。固定取值。
                  WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
 },
        }
        
        resp, err := instance.AIProcess(context.Background(), param)

        if err != nil {
                fmt.Printf("error %v", err)
        } else {
                t, _ := json.Marshal(resp)
                fmt.Printf("success %v", string(t))
        }
}
\`\`\`

<span id="45982961"></span>
#### 异步处理

1. 创建批量处理任务。接口参数说明详见 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916)。
   \`\`\`Go
   package imagex_test
   
   import (
           "context"
           "encoding/json"
           "fmt"
           "testing"
   
           "github.com/volcengine/volc-sdk-golang/base"
           imagex "github.com/volcengine/volc-sdk-golang/service/imagex/v2"
   )
   
   func Test_CreateImageAITask(t *testing.T) {
           instance := imagex.NewInstance()
   
           instance.SetCredential(base.Credentials{
                 // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
                 // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。        
                   AccessKeyID:     "ak",
                   SecretAccessKey: "sk",
           })
   
           param := &imagex.CreateImageAITaskReq{
               CreateImageAITaskBody: &imagex.CreateImageAITaskBody{
                  ServiceID: "5s****fo",                       // 必选。服务 ID。
                  QueueID:   "649a9dbc32**064d44cf5b0",        // 必选。队列 ID。
                  DataType:  "uri",                            // 必选。图片地址类型，支持取值 uri 和 url。
                  DataList:  []string{"a.png", "uridemo.png"}, // 必选。图片 URI 或 URL 列表（URI 不包含 tos-*-i-* 前缀）。
                  CallbackConf: &imagex.CreateImageAITaskBodyCallbackConf{ // 可选。回调配置。
                     Method:     "HTTP",             // 必选。回调方式，取值固定为 HTTP。
                     Endpoint:   "https://demo.com", // 必选。回调地址，用于接收处理结果。
                     DataFormat: "JSON",             // 可选。回调数据格式，支持取值 XML 和 JSON。
                     Args:       "productid",        // 可选。业务自定义回调参数。
                     Type:       "task",             // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
                  },
                  WorkflowParameter:  "{\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
                  WorkflowTemplateID: "system_workflow_ai_super_resolution",                                                // 必选。模板 ID。固定取值。
               },
           }
   
           resp, err := instance.CreateImageAITask(context.Background(), param)
   
           if err != nil {
                   fmt.Printf("error %v", err)
           } else {
                   t, _ := json.Marshal(resp)
                   fmt.Printf("success %v", string(t))
           }
   }
   \`\`\`

2. 通过以下任一方式获取图像处理结果。
   * 回调通知：如果您在上一步设置了回调地址，则当任务完成后，veImageX 会向该回调地址发送回调消息。详见[回调](https://www.volcengine.com/docs/508/1526662)。
   * 主动查询：如果您未设置回调地址，需主动获取图像处理结果。接口参数说明详见 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913)。
      \`\`\`Go
      package imagex_test
      
      import (
              "context"
              "encoding/json"
              "fmt"
              "testing"
      
              "github.com/volcengine/volc-sdk-golang/base"
              imagex "github.com/volcengine/volc-sdk-golang/service/imagex/v2"
      )
      
      func Test_GetImageAIDetails(t *testing.T) {
              instance := imagex.NewInstance()
      
              instance.SetCredential(base.Credentials{
                    // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
                    // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。              
                      AccessKeyID:     "ak",
                      SecretAccessKey: "sk",
              })
      
              param := &imagex.GetImageAIDetailsQuery{
                  QueueID: "649a9dbc32**064d44cf5b0", // 必选。队列 ID。
                  TaskID: "67174744a**54449623155b9", // 必选。任务 ID。
                  StartTime: 1684713599, // 必选。查询开始时间。Unix 秒级时间戳。
                  EndTime: 1684913599, // 必选。查询结束时间。Unix 秒级时间戳。
                  Status: "Success", // 可选。任务执行状态。默认返回所有任务。
                  SearchPtn: "test", // 可选。图片 URI 或 URL 关键字。默认返回所有任务。
                  Limit: 10, // 必选。分页条数。取值范围为 (0, 100]。
                  Offset: 0, // 可选。分页偏移量。
                  ServiceID: "5s****fo", // 必选。服务 ID。
              }
      
              resp, err := instance.GetImageAIDetails(context.Background(), param)
      
              if err != nil {
                      fmt.Printf("error %v", err)
              } else {
                      t, _ := json.Marshal(resp)
                      fmt.Printf("success %v", string(t))
              }
      }
      \`\`\`

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="Python SDK" key="WfmJSkHJRM"><RenderMd content={`<span id="5fdbd7b0"></span>
#### 前提条件
调用接口前，请先完成 Python SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23774)操作。
<span id="816b80a8"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1518358#0b6bb58e)。
\`\`\`Python
# coding:utf-8
from volcengine.imagex.v2.imagex_service import ImagexService

if __name__ == '__main__':
    service = ImagexService()

    # 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
    # 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
    service.set_ak('ak')
    service.set_sk('sk')

    body = {
        "ServiceId": "91**2g",  # 必选。服务 ID。
        "WorkflowTemplateId": "system_workflow_ai_super_resolution",  # # 必选。模板 ID。固定取值。
        "WorkflowParameter": "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}" # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    }
    query = {}

    resp = service.ai_process(query, body)
    print(resp)
\`\`\`

<span id="8c0413aa"></span>
#### 异步处理

1. 创建批量处理任务。接口参数说明详见 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916)。
   \`\`\`Python
   # coding:utf-8
   from volcengine.imagex.v2.imagex_service import ImagexService
   
   if __name__ == '__main__':
       service = ImagexService()
   
       # 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
       # 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
       service.set_ak('ak')
       service.set_sk('sk')
   
       body = {
           "ServiceId": "5s****fo",  # 必选。服务 ID。
           "QueueId": "649a9dbc32**064d44cf5b0",  # 必选。队列 ID。
           "DataType": "uri",  # 必选。图片地址类型，支持取值 uri 和 url。
           "DataList": ["a.png", "uridemo.png"],  # 必选。图片 URI 或 URL 列表（URI 不包含 tos-*-i-* 前缀）。
           "CallbackConf": {  # 可选。回调配置。
               "Method": "HTTP",  # 必选。回调方式，取值固定为 HTTP。
               "Endpoint": "https://demo.com",  # 必选。回调地址，用于接收处理结果。
               "DataFormat": "JSON",  # 可选。回调数据格式，支持取值 XML 和 JSON。
               "Args": "productid",  # 可选。业务自定义回调参数。
               "Type": "task"  # 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
           },
           "WorkflowParameter": "{\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}",  # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
           "WorkflowTemplateId": "system_workflow_ai_super_resolution"  # 必选。模板 ID。固定取值。
       }
   
       resp = service.create_image_ai_task(query, body)
       print(resp)
   \`\`\`

2. 通过以下任一方式获取图像处理结果。
   * 回调通知：如果您在上一步设置了回调地址，则当任务完成后，veImageX 会向该回调地址发送回调消息。详见[回调](https://www.volcengine.com/docs/508/1526662)。
   * 主动查询：如果您未设置回调地址，需主动获取图像处理结果。接口参数说明详见 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913)。
      \`\`\`Python
      # coding:utf-8
      from volcengine.imagex.v2.imagex_service import ImagexService
      
      if __name__ == '__main__':
          service = ImagexService()
      
          # 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
          # 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
          service.set_ak('ak')
          service.set_sk('sk')
      
          query = {
               "QueueId": "649a9dbc32**064d44cf5b0", # 必选。队列 ID。
               "TaskId": "67174744a**54449623155b9", # 必选。任务 ID。
               "StartTime": 1684713599, # 必选。查询开始时间。Unix 秒级时间戳。
               "EndTime": 1684913599, # 必选。查询结束时间。Unix 秒级时间戳。
               "Status": "Success", # 可选。任务执行状态。默认返回所有任务。
               "SearchPtn": "test", # 可选。图片 URI 或 URL 关键字。默认返回所有任务。
               "Limit": 10, # 必选。分页条数。取值范围为 (0, 100]。
               "Offset": 0, # 可选。分页偏移量。
               "ServiceId": "5s****fo" # 必选。服务 ID。
          }
      
          resp = service.get_image_ai_details(query)
          print(resp)
      \`\`\`

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="Java SDK" key="dHZkHjJAJc"><RenderMd content={`<span id="650ccfe7"></span>
#### 前提条件
调用接口前，请先完成 Java SDK 的[安装及初始化](https://www.volcengine.com/docs/508/66513)操作。
<span id="86fba742"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1518358#0b6bb58e)。
\`\`\`Java
package com.volcengine.example.imagex.v2.api;

import com.volcengine.model.imagex.v2.*;
import com.volcengine.service.imagex.v2.ImagexService;

public class AIProcessExample {
    public static void main(String[] args) {
        ImagexService service = ImagexService.getInstance();
         // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
        // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。       
        service.setAccessKey("ak");
        service.setSecretKey("sk");

        AIProcessBody body = new AIProcessBody();
         body.setServiceId("91**2g"); // 必选。服务 ID。
         body.setWorkflowTemplateId("system_workflow_ai_super_resolution"); // 必选。模板 ID。固定取值。
         body.setWorkflowParameter("{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
 
        try {
            AIProcessRes resp = service.aIProcess(body);
            System.out.println(resp);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
\`\`\`

<span id="f135807d"></span>
#### 异步处理

1. 创建批量处理任务。接口参数说明详见 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916)。
   \`\`\`Java
   package com.volcengine.example.imagex.v2.api;
   
   import com.volcengine.model.imagex.v2.*;
   import com.volcengine.service.imagex.v2.ImagexService;
   
   public class CreateImageAITaskExample {
       public static void main(String[] args) {
           ImagexService service = ImagexService.getInstance();
           // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
           // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
           service.setAccessKey("ak");
           service.setSecretKey("sk");
   
        // 1.（可选）构建回调配置（CallbackConf）。
        CreateImageAITaskBodyCallbackConf callbackConf = new CreateImageAITaskBodyCallbackConf();
        callbackConf.setMethod("HTTP"); // 必选。回调方式，取值固定为 HTTP。
        callbackConf.setEndpoint("https://demo.com"); // 必选。回调地址，用于接收处理结果。
        callbackConf.setDataFormat("JSON"); // 可选。回调数据格式，支持取值 XML 和 JSON。
        callbackConf.setArgs("productid"); // 可选。业务自定义回调参数。
        callbackConf.setType("task"); // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
       
        // 2. 构建请求体（CreateImageAITaskBody）。
        CreateImageAITaskBody body = new CreateImageAITaskBody();
        body.setServiceId("5s****fo"); // 必选。服务 ID。
        body.setQueueId("649a9dbc32**064d44cf5b0"); // 必选。队列 ID。
        body.setDataType("uri"); // 必选。图片地址类型，支持取值 uri 和 url。
        body.setDataList(Arrays.asList("a.png", "uridemo.png")); // 必选。图片 URI 或 URL 列表（URI 不包含 tos-*-i-* 前缀）。
        body.setCallbackConf(callbackConf); // 可选。回调配置。
        body.setWorkflowParameter("{" +
        "\\"GenDREnhanceParam\\":{" +
        "\\"ModelId\\":\\"ai_sr_model_v2\\"," +
        "\\"Multiple\\":2" +
        "}" +
        "}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        body.setWorkflowTemplateId("system_workflow_ai_super_resolution"); // 必选。模板 ID。固定取值。
       
           try {
               CreateImageAITaskRes resp = service.createImageAITask(body);
               System.out.println(resp);
           } catch (Exception e) {
               e.printStackTrace();
           }
       }
   }
   \`\`\`

2. 通过以下任一方式获取图像处理结果。
   * 回调通知：如果您在上一步设置了回调地址，则当任务完成后，veImageX 会向该回调地址发送回调消息。详见[回调](https://www.volcengine.com/docs/508/1526662)。
   * 主动查询：如果您未设置回调地址，需主动获取图像处理结果。接口参数说明详见 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913)。
      \`\`\`Java
      package com.volcengine.example.imagex.v2.api;
      
      import com.volcengine.model.imagex.v2.*;
      import com.volcengine.service.imagex.v2.ImagexService;
      
      public class GetImageAIDetailsExample {
          public static void main(String[] args) {
              ImagexService service = ImagexService.getInstance();
              // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
              // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
              service.setAccessKey("ak");
              service.setSecretKey("sk");
      
              GetImageAIDetailsQuery query = new GetImageAIDetailsQuery();
               // 必选参数。
               query.setQueueId("649a9dbc32**064d44cf5b0"); // 队列 ID。
               query.setTaskId("67174744a**54449623155b9"); // 任务 ID。
               query.setStartTime(1684713599L); // 查询开始时间。Unix 秒级时间戳。
               query.setEndTime(1684913599L); // 查询结束时间。Unix 秒级时间戳。
               query.setLimit(10L); // 分页条数。取值范围为 (0, 100]。
               query.setServiceId("5s****fo"); // 服务 ID。  
      
               // 可选参数。
               query.setStatus("Success"); // 任务执行状态。默认返回所有任务。
               query.setSearchPtn("test"); // 图片 URI 或 URL 关键字。默认返回所有任务。
               query.setOffset(0L); // 分页偏移量。
             
              try {
                  GetImageAIDetailsRes resp = service.getImageAIDetails(query);
                  System.out.println(resp);
              } catch (Exception e) {
                  e.printStackTrace();
              }
          }
      }
      \`\`\`

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="PHP SDK" key="YfDeBa86L2"><RenderMd content={`<span id="72202434"></span>
#### 前提条件
调用接口前，请先完成 PHP SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23778)操作。
<span id="4409e006"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1518358#0b6bb58e)。
\`\`\`PHP
<?php
include_once(__DIR__ . '../../../../vendor/autoload.php');

use Volc\\Service\\ImageX\\V2\\Imagex;

$client = Imagex::getInstance();

// 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
// 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
$client->setAccessKey("ak");
$client->setSecretKey("sk");

$body = [
     "ServiceId" => "91**2g", // 必选。服务 ID。
     "WorkflowTemplateId" => "system_workflow_ai_super_resolution", // 必选。模板 ID。固定取值。
     "WorkflowParameter" => "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
];
$query = [];

$response = $client->AIProcess($query, $body);
print_r($response);
\`\`\`

<span id="5bfe6811"></span>
#### 异步处理

1. 创建批量处理任务。接口参数说明详见 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916)。
   \`\`\`PHP
   <?php
   include_once(__DIR__ . '../../../../vendor/autoload.php');
   
   use Volc\\Service\\ImageX\\V2\\Imagex;
   
   $client = Imagex::getInstance();
   
   // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
   // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
   $client->setAccessKey("ak");
   $client->setSecretKey("sk");
   
   $body = [
        "ServiceId" => "5s****fo", // 必选。服务 ID。
        "QueueId" => "649a9dbc32**064d44cf5b0", // 必选。队列 ID。 
        "DataType" => "uri", // 必选。图片地址类型，支持取值 uri 和 url。
        "DataList" => ["a.png", "uridemo.png"], // 必选。图片 URI 或 URL 列表（URI 不包含 tos-*-i-* 前缀）。
        "CallbackConf" => [ // 可选。回调配置。
            "Method" => "HTTP", // 必选。回调方式，取值固定为 HTTP。
            "Endpoint" => "https://demo.com", // 必选。回调地址，用于接收处理结果。
            "DataFormat" => "JSON", // 可选。回调数据格式，支持取值 XML 和 JSON。
            "Args" => "productid", // 可选。业务自定义回调参数。
            "Type" => "task" // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
        ],
        "WorkflowParameter" => "{\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        "WorkflowTemplateId" => "system_workflow_ai_super_resolution" // 必选。模板 ID。固定取值。
   ];
   $query = [];
   
   $response = $client->CreateImageAITask($query, $body);
   print_r($response);
   \`\`\`

2. 通过以下任一方式获取图像处理结果。
   * 回调通知：如果您在上一步设置了回调地址，则当任务完成后，veImageX 会向该回调地址发送回调消息。详见[回调](https://www.volcengine.com/docs/508/1526662)。
   * 主动查询：如果您未设置回调地址，需主动获取图像处理结果。接口参数说明详见 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913)。
      \`\`\`PHP
      <?php
      include_once(__DIR__ . '../../../../vendor/autoload.php');
      
      use Volc\\Service\\ImageX\\V2\\Imagex;
      
      $client = Imagex::getInstance();
      
      // 强烈建议不要把 ak 和 sk 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
      // 本示例通过从环境变量中读取 ak 和 sk，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 ak 和 sk。
      $client->setAccessKey("ak");
      $client->setSecretKey("sk");
      
      $query = [
           "QueueId" => "649a9dbc32**064d44cf5b0", // 必选。队列 ID。
           "TaskId" => "67174744a**54449623155b9", // 必选。任务 ID。
           "StartTime" => 1684713599, // 必选。查询开始时间。Unix 秒级时间戳。
           "EndTime" => 1684913599, // 必选。查询结束时间。Unix 秒级时间戳。
           "Status" => "Success", // 可选。任务执行状态。默认返回所有任务。
           "SearchPtn" => "test", // 可选。图片 URI 或 URL 关键字。默认返回所有任务。
           "Limit" => 10, // 必选。分页条数。取值范围为 (0, 100]。
           "Offset" => 0, // 可选。分页偏移量。
           "ServiceId" => "5s****fo" // 必选。服务 ID。
      ];
      
      $response = $client->GetImageAIDetails($query);
      print_r($response);
      \`\`\`

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="Node.js SDK" key="mevPKISfjX"><RenderMd content={`<span id="8bef4a4e"></span>
#### 前提条件
调用接口前，请先完成 Node.js SDK 的[安装及初始化](https://www.volcengine.com/docs/508/1250175)操作。
<span id="f7438ae4"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1518358#0b6bb58e)。
\`\`\`JavaScript
import { imagex } from "@volcengine/openapi";

export async function AIProcessDemo() {
  try {
    const Client = new imagex.ImageXService({
      // 强烈建议不要把 VOLC_ACCESSKEY 和 VOLC_SECRETKEY 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
      // 本示例通过从环境变量中读取 VOLC_ACCESSKEY 和 VOLC_SECRETKEY，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 VOLC_ACCESSKEY 和 VOLC_SECRETKEY。
      accessKeyId: process.env.VOLC_ACCESSKEY,
      secretKey: process.env.VOLC_SECRETKEY,
    });

    const requestParam = {
      ServiceId: "91**2g", // 必选。服务 ID。
      WorkflowTemplateId: "system_workflow_ai_super_resolution",   // 必选。模板 ID。固定取值。
      WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    };

    const res = await Client.AIProcess(requestParam);
    console.log("res", res);
  } catch (err) {
    console.error(err);
  }
}
\`\`\`

<span id="fe1518fa"></span>
#### 异步处理

1. 创建批量处理任务。接口参数说明详见 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916)。
   \`\`\`JavaScript
   import { imagex } from "@volcengine/openapi";
   
   export async function CreateImageAITaskDemo() {
     try {
       const Client = new imagex.ImageXService({
         // 强烈建议不要把 VOLC_ACCESSKEY 和 VOLC_SECRETKEY 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
         // 本示例通过从环境变量中读取 VOLC_ACCESSKEY 和 VOLC_SECRETKEY，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 VOLC_ACCESSKEY 和 VOLC_SECRETKEY。
         accessKeyId: process.env.VOLC_ACCESSKEY,
         secretKey: process.env.VOLC_SECRETKEY,
       });
   
       const requestParam = {
         ServiceId: "5s****fo", // 必选。服务 ID。
         QueueId: "649a9dbc32**064d44cf5b0", // 必选。队列 ID。 
         DataType: "uri", // 必选。图片地址类型，支持取值 uri 和 url。
         DataList: ["a.png", "uridemo.png"], // 必选。图片 URI 或 URL 列表（URI 不包含 tos-*-i-* 前缀）。
         CallbackConf: { // 可选。回调配置。
           Method: "HTTP", // 必选。回调方式，取值固定为 HTTP。
           Endpoint: "https://demo.com", // 必选。回调地址，用于接收处理结果。
           DataFormat: "JSON",  // 可选。回调数据格式，支持取值 XML 和 JSON。
           Args: "productid",  // 可选。业务自定义回调参数。
           Type: "task",  // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
         },
         WorkflowParameter: "{\\"GenDREnhanceParam\\":{\\"ModelId\\":\\"ai_sr_model_v2\\",\\"Multiple\\":2}}",  // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
         WorkflowTemplateId: "system_workflow_ai_super_resolution", // 必选。模板 ID。固定取值。
       };
   
       const res = await Client.CreateImageAITask(requestParam);
       console.log("res", res);
     } catch (err) {
       console.error(err);
     }
   }
   \`\`\`

2. 通过以下任一方式获取图像处理结果。
   * 回调通知：如果您在上一步设置了回调地址，则当任务完成后，veImageX 会向该回调地址发送回调消息。详见[回调](https://www.volcengine.com/docs/508/1526662)。
   * 主动查询：如果您未设置回调地址，需主动获取图像处理结果。接口参数说明详见 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913)。
      \`\`\`JavaScript
      import { imagex } from "@volcengine/openapi";
      
      export async function GetImageAIDetailsDemo() {
        try {
          const Client = new imagex.ImageXService({
            // 强烈建议不要把 VOLC_ACCESSKEY 和 VOLC_SECRETKEY 保存到工程代码里，否则可能导致 AccessKey 泄露，威胁您账号下所有资源的安全。
            // 本示例通过从环境变量中读取 VOLC_ACCESSKEY 和 VOLC_SECRETKEY，来实现 API 访问的身份验证。运行代码示例前，请配置环境变量 VOLC_ACCESSKEY 和 VOLC_SECRETKEY。
            accessKeyId: process.env.VOLC_ACCESSKEY,
            secretKey: process.env.VOLC_SECRETKEY,
          });
      
          const requestParam = {
            QueueId: "649a9dbc32**064d44cf5b0", // 必选。队列 ID。
            TaskId: "67174744a**54449623155b9", // 必选。任务 ID。
            StartTime: 1684713599, // 必选。查询开始时间。Unix 秒级时间戳。
            EndTime: 1685913599, // 必选。查询结束时间。Unix 秒级时间戳。
            Status: "Success", // 可选。任务执行状态。默认返回所有任务。
            SearchPtn: "test", // 可选。图片 URI 或 URL 关键字。默认返回所有任务。
            Limit: 10, // 必选。分页条数。取值范围为 (0, 100]。
            Offset: 0, // 可选。分页偏移量。
            ServiceId: "5s****fo", // 必选。服务 ID。
          };
      
          const res = await Client.GetImageAIDetails(requestParam);
          console.log("res", res);
        } catch (err) {
          console.error(err);
        }
      }
      \`\`\`

`}></RenderMd></Tabs.TabPane></Tabs>);
 ```

<span id="dd29fe18"></span>
### 方式三：通过控制台操作
在[新建模板](/docs/508/8087)时，单击**附加组件-智能处理** > **AIGC大模型超分辨率**，并完成相关配置。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2962782c27d84c99b5954ff6c0c30442~tplv-goo7wpa0wc-image.image =513x)
<span id="66a75867"></span>
## 步骤二：查看结果图

```mixin-react
return (<Tabs>
<Tabs.TabPane title="方式一：默认公网加速域名访问结果图" key="OO3RdF54NZ"><RenderMd content={`<span id="b6c7e5f9"></span>
### 通过调用服务端 SDK 获取资源地址（推荐）
veImageX 提供了以下编程语言的 SDK，方便您调用 API。详见[方式一：通过调用服务端 SDK 获取资源地址（推荐）](/docs/508/2164787#0e6382e6)。
<span id="0b1fe26b"></span>
### 通过控制台获取资源地址
在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取资源地址。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/05522787ffc34892989c70216ad423df~tplv-goo7wpa0wc-image.image =2396x)

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式二：控制台预览结果图" key="WwK1zPGxqh"><RenderMd content={`

* 未新增自定义域名时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面搜索结果图的存储 URI。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f2b2412712a4d70b4d77641c9b1c2a5~tplv-goo7wpa0wc-image.image =2908x)
* 已[新增自定义域名](/docs/508/174565)时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取结果图的 URL 地址。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6707099e11a040babc2e8390eaa507c1~tplv-goo7wpa0wc-image.image =2904x)

:::tip
使用[方式三：通过控制台操作](/docs/508/1518358#dd29fe18)调用 AI 能力时，仅支持通过控制台预览结果图。
:::
`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式三：手动拼接结果图地址" key="ssE09IVQ9L"><RenderMd content={`拼接格式如下所示。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/85c2cdf85b1b463a99adf02beb4ea634~tplv-goo7wpa0wc-image.image =870x)
:::tip
* 确保已[新增自定义域名](/docs/508/174565)。
* 如无添加水印、调整分辨率等二次处理需求，使用服务下**获取原图**默认模板的名称拼接结果图地址即可。
* 如果存在中文字符，则以其 16 进制表示。
:::
`}></RenderMd></Tabs.TabPane></Tabs>);
 ```

<span id="e4e08ee3"></span>
# 模板说明
<span id="63e43e8e"></span>
## 模板 ID
`system_workflow_ai_super_resolution`
<span id="81c85791"></span>
## 输入参数
您需要将输入参数序列化为 JSON 字符串后，作为同步处理接口 [AIProcess](https://www.volcengine.com/docs/508/1515915) 或异步处理接口 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916) 的 `WorkflowParameter` 参数传入，或作为批量处理时的模板配置参数传入。 

```mixin-react
const properties = ({
  "columns": [{
    "title": "参数\n",
    "dataIndex": "column_0"
  }, {
    "title": "类型",
    "dataIndex": "column_1"
  }, {
    "title": "是否必选",
    "dataIndex": "column_2"
  }, {
    "title": "示例值",
    "dataIndex": "column_3"
  }, {
    "title": "说明",
    "dataIndex": "column_4"
  }],
  "data": [{
    "key": 1,
    "children": [{
      "key": 3,
      "children": [],
      "column_0": "DataType\n",
      "column_1": "String",
      "column_2": "是",
      "column_3": "uri",
      "column_4": <>输入图像的地址类型。支持传入 url 或 uri。</>
    }, {
      "key": 2,
      "children": [],
      "column_0": "ObjectKey\n",
      "column_1": "String",
      "column_2": "是",
      "column_3": "a.png",
      "column_4": <>输入图像的 URL 或 URI 地址。<ul><li>当 DataType 取值为 url 时：传入公网可访问的 URL 地址，例如 https://example.com/static/demo1.png。</li> <li>当 DataType 取值为 uri 时：传入指定服务 ID 下不包含 tos-*-i-* 前缀的存储 URI，例如存储 URI 为 tos-m*a-i-0ksq****qe/image-a/example.jpg，则传入 image-a/example.jpg。</li></ul></>
    }],
    "column_0": "Input\n",
    "column_1": "Object",
    "column_2": "否",
    "column_3": "-",
    "column_4": <>输入图像的信息。<br />仅在调用同步处理接口 <a href="https://www.volcengine.com/docs/508/1515915">AIProcess</a> 时必选。</>
  }, {
    "key": 4,
    "children": [{
      "key": 8,
      "children": [],
      "column_0": "ModelId\n",
      "column_1": "String",
      "column_2": "否",
      "column_3": "ai_sr_model_v2",
      "column_4": <>超分辨率模型。不传该参数，则使用 GDR1.1 模型。如需使用 GDR1.2 模型，则取值为 ai_sr_model_v2。推荐使用 GDR1.2。GDR1.2 相较于 GDR1.1，差异如下：<ul><li>生成更加真实，保留或生成更多细节，缓解油画感和 AI 感。</li><li>减少纹理丢失、生成错误、过锐等问题。</li><li>解决缩放到小分辨率的锯齿问题。</li></ul></>
    }, {
      "key": 5,
      "children": [],
      "column_0": "Multiple\n",
      "column_1": "Float",
      "column_2": "否",
      "column_3": "2",
      "column_4": <>图像处理后较原图的分辨率倍数，支持 2 位小数。取值最大不超过 30。不建议取值过大，以免超时。<br />适用于需要提升图像整体分辨率的场景，例如需要更高分辨率进行打印或在高分辨率屏幕上显示。<br />必须至少传入 Multiple 或 TargetWidth / TargetHeight，指定倍率或宽高。如果同时传入 Multiple 和 TargetWidth / TargetHeight，则 Multiple 生效。</>
    }, {
      "key": 6,
      "children": [],
      "column_0": "TargetWidth\n",
      "column_1": "Integer",
      "column_2": "否",
      "column_3": "1024",
      "column_4": <>图像处理后的宽度，单位为 px，取值不能超过 10240。<br />适用于需要将图像调整为特定尺寸的场景，例如适配某些固定尺寸的展示区域。<br />输出宽高的比例必须与原图保持一致，若不一致，则采用原图宽高比例，以缩放比例小的边为准，缩放比例指目标长度/原始长度，另一边自动缩放。若指定一边为 0，则以有数值的一边为准。<br />必须至少传入 Multiple 或 TargetWidth / TargetHeight，指定倍率或宽高。如果同时传入 Multiple 和 TargetWidth / TargetHeight，则 Multiple 生效。</>
    }, {
      "key": 7,
      "children": [],
      "column_0": "TargetHeight\n",
      "column_1": "Integer",
      "column_2": "否",
      "column_3": "1024",
      "column_4": <>图像处理后的高度，单位为 px，取值不能超过 10240。<br />适用于需要将图像调整为特定尺寸的场景，例如适配某些固定尺寸的展示区域。<br />输出宽高的比例必须与原图保持一致，若不一致，则采用原图宽高比例，以缩放比例小的边为准，缩放比例指目标长度/原始长度，另一边自动缩放。若指定一边为 0，则以有数值的一边为准。<br />必须至少传入 Multiple 或 TargetWidth / TargetHeight，指定倍率或宽高。如果同时传入 Multiple 和 TargetWidth / TargetHeight，则 Multiple 生效。</>
    }],
    "column_0": "GenDREnhanceParam\n",
    "column_1": "Object",
    "column_2": "是",
    "column_3": "-",
    "column_4": "AIGC 超分参数。\n"
  }]
}); 
return <Table border={{ cell: true, wrapper: true }} pagination={false} {...properties} />;
```

<span id="2fba069b"></span>
## 输出参数
veImageX 服务会将输出参数序列化为 JSON 字符串后作为 [AIProcess](https://www.volcengine.com/docs/508/1515915) 接口、[回调](https://www.volcengine.com/docs/508/1526662)或 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913) 接口的 `Output` 参数返回。
:::tip
生成的图像在控制台**资源管理**页面默认不展示，仅支持通过不包含 `tos-*-i-*` 前缀的存储 URI 搜索。
:::

| | | | | \
|参数 |类型 |示例值 |说明 |
|---|---|---|---|
| | | | | \
|ObjectKey |String |a.webp |生成图像在指定服务 ID 下不包含 `tos-*-i-*` 前缀的存储 URI。 |
| | | | | \
|Size |Integer |38656 |生成图像的大小，单位为字节。 |
| | | | | \
|Format |String |webp |生成图像的格式。 |


