ImageX-SeeDream 生图方案附加组件通过 SeeDream 4.0 模型，根据提示词和参考图，生成一张或多张图像，适用于广告、游戏、网站设计等场景。本文介绍如何使用 ImageX-SeeDream 生图方案附加组件。
<span id="08ad06b7"></span>
# 使用限制
为确保能够生成图像，请满足以下限制。

* **输入格式**：.jpeg、.png。
   * 如果格式为 .webp、.awebp、.gif、.tiff、.bmp、.ico、.heic 或 .heif，请将 `EnableImageConversion` 设置为 `true`。详见[输入参数](/docs/508/1962138#c76e66af)。
   * 如果为其他格式，请先通过模板变更图片格式。
* **输入大小**：单张图 <= 10 MB。如果大于 10 MB，请将 `EnableImageConversion` 设置为 `true`。详见[输入参数](/docs/508/1962138#c76e66af)。
* **输入宽高**：(14x14, 6000x6000]。单位为 px。如果为其他宽高，请先通过模板变更图片宽高。
* **输入宽高比**：[1/3, 3]
* **输出格式**：.jpeg。可通过模板二次处理为其他格式。
* **输出分辨率**：1k - 4k。可通过模板二次处理为更高分辨率。
* **输出宽高**：[1280x720, 4096x4096]。单位为 px。可通过模板二次处理为其他宽高。
* **输出宽高比**：[1/16, 16]
* **限流 IPM**：500 张 / 分钟。

<span id="0b63ddc4"></span>
# 使用方法
您可以选择仅使用提示词，或结合提示词与参考图来生成图像。
根据您选择的处理方式，支持的参考图和生成图像数量有所不同。

* **同步处理**：支持传入 0-1 张参考图，并生成 1 张图像。
* **异步处理**：支持传入 0-10 张参考图，并生成 1 张图像或一组内容关联的图像。传入的参考图数量和输出的图像数量总和最多为 15 张。

<span id="e5cbb59d"></span>
## 前提条件

* 已[开通 veImageX 产品服务](https://www.volcengine.com/docs/508/8084#%E5%BC%80%E9%80%9A-veimagex-%E4%BA%A7%E5%93%81%E6%9C%8D%E5%8A%A1)并[创建服务](https://www.volcengine.com/docs/508/357114)。
* 已开通[智能处理计费配置](https://www.volcengine.com/docs/508/1262340#%E5%BC%80%E9%80%9A%E6%99%BA%E8%83%BD%E5%A4%84%E7%90%86%E8%AE%A1%E8%B4%B9%E9%85%8D%E7%BD%AE)。
* （可选）如需完成以下操作，确保已[新建模板](/docs/508/8087)。
   * 处理参考图：如果参考图不符合输入限制，您可以通过模板来变更图片格式、宽高等，再将处理后的图片作为输入的参考图。
   * 处理生成图像：对生成的图像进行二次处理，例如添加水印或调整分辨率。

<span id="3cefdfcf"></span>
## 步骤一：调用 AI 能力
<span id="d9c95093"></span>
### 方式一：通过 API 调用
<span id="d718d336"></span>
#### 同步处理
调用同步处理接口 [AIProcess](https://www.volcengine.com/docs/508/1515915)，提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。
**请求示例**
```JSON
POST https://imagex.volcengineapi.com/?Action=AIProcess&Version=2023-05-01
{
    "ServiceId": "91**2g", // 必选。服务 ID。
    "WorkflowTemplateId": "system_workflow_ark_seedream", // 必选。模板 ID。
    "WorkflowParameter": "{\"Input\":{\"ObjectKey\":\"a.png\",\"DataType\":\"uri\"},\"ArkSeedreamParam\":{\"ModelId\":\"seedream4\",\"Prompt\":\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\",\"Size\":\"2048x2048\",\"Watermark\":true,\"EnableImageConversion\":false,\"OptimizePromptOptions\":{\"Mode\":\"standard\"}}}" // 必选。模板参数。
}
```

其中，

* `ServiceId`：服务 ID，可从[服务管理](https://console.volcengine.com/imagex/service_manage/)页面获取。
* `WorkflowTemplateId`：取值固定为 `system_workflow_ark_seedream`。
* `WorkflowParameter`：根据[输入参数](/docs/508/1962138#c76e66af)，设置该参数取值。

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
        "Output": "{\"Model\":\"doubao-seedream-4-0-250828\",\"Data\":{\"Uri\":\"a.jpeg\",\"Size\":\"2048x2048\"},\"Usage\":{\"GeneratedImages\":1}}"
    }
}
```

`Output` 的参数含义详见[输出参数](/docs/508/1962138#d3c99caf)。
<span id="c48535bb"></span>
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
       "DataType": "uri", // 必选。图片数据类型，支持取值 uri 和 url。
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
       "WorkflowParameter": "{\"ArkSeedreamParam\":{\"ModelId\":\"seedream4\",\"Prompt\":\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\",\"Size\":\"2048x2048\",\"Watermark\":true,\"EnableImageConversion\":false,\"SequentialImageGeneration\":\"auto\",\"SequentialImageGenerationOptions\":{\"MaxImages\":3},\"OptimizePromptOptions\":{\"Mode\":\"standard\"}}}", // 必选。模板参数。
       "WorkflowTemplateId": "system_workflow_ark_seedream", // 必选。模板 ID。
       "QueueId": "62f224ce61****826e38c29a" // 必选。队列 ID。
   }
   ```

   其中，
   * `WorkflowTemplateId`：取值必须为 `system_workflow_ark_seedream`。
   * `WorkflowParameter`：根据[输入参数](/docs/508/1962138#c76e66af)，设置该参数取值。
   * `DataType`：如不传入参考图，仅根据提示词生成图像时，必须将取值设置为 `url`。 
   * `DataList`：参考图的 URL 或 URI 地址，可辅助生成图像。
      * 当仅根据提示词生成图像时：参数取值为空字符串。例如 `[""]` 表示一次文生图请求，`["", ""]` 表示两次文生图请求，以此类推。
      * 当根据提示词和参考图生成图像时：参数取值为字符串数组，数组长度为 1-10,000。每个字符串中最多包含 10 张图片的地址，且每个地址之间使用英文逗号（,）分隔。每个字符串代表一次生图请求传入的参考图，例如 `["a.png,uridemo.png"]` 表示根据提示词和参考图 a.png、uridemo.png 生成一次图像，`["a.png","uridemo.png"]` 表示根据提示词和参考图 a.png 生成一次图像，再根据提示词和参考图 uridemo.png 生成一次图像。
      :::tip
      地址不可包含英文逗号（,），且 URI 地址不包含 `tos-*-i-*`  前缀，例如图片的 URI 地址为 `tos-m*a-i-0ksq****qe/image-a/example.png`，则传入 `image-a/example.png`。
      :::
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

<span id="5121d681"></span>
### 方式二：通过服务端 SDK 调用
veImageX 提供了以下编程语言的 SDK，方便您调用 API。

```mixin-react
return (<Tabs>
<Tabs.TabPane title="Golang SDK" key="ytvcfxmc92"><RenderMd content={`<span id="d30c7e16"></span>
#### 前提条件
调用接口前，请先完成 Golang SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23757)操作。
<span id="4dd4b147"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1962138#d718d336)。
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
                  WorkflowTemplateID: "system_workflow_ark_seedream",   // 必选。模板 ID。固定取值。
                  WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
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

<span id="0968117f"></span>
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
                  DataType:  "uri",                            // 必选。参考图的地址类型。支持传入 url 或 uri。详见本文的方式一：通过 API 调用 > 异步处理部分。
                  DataList:  []string{"a.png", "uridemo.png"}, // 必选。参考图的 URL 或 URI 地址，可辅助生成图像。详见本文的方式一：通过 API 调用 > 异步处理部分。
                  CallbackConf: &imagex.CreateImageAITaskBodyCallbackConf{ // 可选。回调配置。
                     Method:     "HTTP",             // 必选。回调方式，取值固定为 HTTP。
                     Endpoint:   "https://demo.com", // 必选。回调地址，用于接收处理结果。
                     DataFormat: "JSON",             // 可选。回调数据格式，支持取值 XML 和 JSON。
                     Args:       "productid",        // 可选。业务自定义回调参数。
                     Type:       "task",             // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
                  },
                  WorkflowParameter:  "{\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"SequentialImageGeneration\\":\\"auto\\",\\"SequentialImageGenerationOptions\\":{\\"MaxImages\\":3},\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
                  WorkflowTemplateID: "system_workflow_ark_seedream",                                                // 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Python SDK" key="X7lZWhVwvd"><RenderMd content={`<span id="2e1ef650"></span>
#### 前提条件
调用接口前，请先完成 Python SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23774)操作。
<span id="461af637"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1962138#d718d336)。
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
        "WorkflowTemplateId": "system_workflow_ark_seedream",  # 必选。模板 ID。固定取值。
        "WorkflowParameter": "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}" # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    }
    query = {}

    resp = service.ai_process(query, body)
    print(resp)
\`\`\`

<span id="4661b5ed"></span>
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
           "DataType": "uri",  # 必选。参考图的地址类型。支持传入 url 或 uri。详见本文的方式一：通过 API 调用 > 异步处理部分。
           "DataList": ["a.png", "uridemo.png"],  # 必选。参考图的 URL 或 URI 地址，可辅助生成图像。详见本文的方式一：通过 API 调用 > 异步处理部分。
           "CallbackConf": {  # 可选。回调配置。
               "Method": "HTTP",  # 必选。回调方式，取值固定为 HTTP。
               "Endpoint": "https://demo.com",  # 必选。回调地址，用于接收处理结果。
               "DataFormat": "JSON",  # 可选。回调数据格式，支持取值 XML 和 JSON。
               "Args": "productid",  # 可选。业务自定义回调参数。
               "Type": "task"  # 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
           },
           "WorkflowParameter": "{\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"SequentialImageGeneration\\":\\"auto\\",\\"SequentialImageGenerationOptions\\":{\\"MaxImages\\":3},\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}",  # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
           "WorkflowTemplateId": "system_workflow_ark_seedream"  # 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Java SDK" key="X9CHBgF89d"><RenderMd content={`<span id="43153ad9"></span>
#### 前提条件
调用接口前，请先完成 Java SDK 的[安装及初始化](https://www.volcengine.com/docs/508/66513)操作。
<span id="156a2371"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1962138#d718d336)。
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
         body.setWorkflowTemplateId("system_workflow_ark_seedream"); // 必选。模板 ID。固定取值。
         body.setWorkflowParameter("{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
 
        try {
            AIProcessRes resp = service.aIProcess(body);
            System.out.println(resp);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
\`\`\`

<span id="ffb47941"></span>
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
        body.setDataType("uri"); // 必选。参考图的地址类型。支持传入 url 或 uri。详见本文的方式一：通过 API 调用 > 异步处理部分。
        body.setDataList(Arrays.asList("a.png", "uridemo.png")); // 必选。参考图的 URL 或 URI 地址，可辅助生成图像。详见本文的方式一：通过 API 调用 > 异步处理部分。
        body.setCallbackConf(callbackConf); // 可选。回调配置。
        body.setWorkflowParameter("{" +
        "\\"ArkSeedreamParam\\":{" +
        "\\"ModelId\\":\\"seedream4\\"," +
        "\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\"," +
        "\\"Size\\":\\"2048x2048\\"," +
        "\\"Watermark\\":true," +
        "\\"EnableImageConversion\\":false," +
        "\\"SequentialImageGeneration\\":\\"auto\\"," +
        "\\"SequentialImageGenerationOptions\\":{\\"MaxImages\\":3}," +
        "\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}" +
        "}" +
        "}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        body.setWorkflowTemplateId("system_workflow_ark_seedream"); // 必选。模板 ID。固定取值。
       
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
<Tabs.TabPane title="PHP SDK" key="o95Mlp8Rif"><RenderMd content={`<span id="d865736b"></span>
#### 前提条件
调用接口前，请先完成 PHP SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23778)操作。
<span id="c48d7401"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1962138#d718d336)。
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
     "WorkflowTemplateId" => "system_workflow_ark_seedream", // 必选。模板 ID。固定取值。
     "WorkflowParameter" => "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
];
$query = [];

$response = $client->AIProcess($query, $body);
print_r($response);
\`\`\`

<span id="3785b54a"></span>
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
        "DataType" => "uri", // 必选。参考图的地址类型。支持传入 url 或 uri。详见本文的方式一：通过 API 调用 > 异步处理部分。
        "DataList" => ["a.png", "uridemo.png"], // 必选。参考图的 URL 或 URI 地址，可辅助生成图像。详见本文的方式一：通过 API 调用 > 异步处理部分。
        "CallbackConf" => [ // 可选。回调配置。
            "Method" => "HTTP", // 必选。回调方式，取值固定为 HTTP。
            "Endpoint" => "https://demo.com", // 必选。回调地址，用于接收处理结果。
            "DataFormat" => "JSON", // 可选。回调数据格式，支持取值 XML 和 JSON。
            "Args" => "productid", // 可选。业务自定义回调参数。
            "Type" => "task" // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
        ],
        "WorkflowParameter" => "{\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"SequentialImageGeneration\\":\\"auto\\",\\"SequentialImageGenerationOptions\\":{\\"MaxImages\\":3},\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        "WorkflowTemplateId" => "system_workflow_ark_seedream" // 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Node.js SDK" key="S2zwsHDdgw"><RenderMd content={`<span id="52e9513f"></span>
#### 前提条件
调用接口前，请先完成 Node.js SDK 的[安装及初始化](https://www.volcengine.com/docs/508/1250175)操作。
<span id="73de3403"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1962138#d718d336)。
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
      WorkflowTemplateId: "system_workflow_ark_seedream",   // 必选。模板 ID。固定取值。
      WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    };

    const res = await Client.AIProcess(requestParam);
    console.log("res", res);
  } catch (err) {
    console.error(err);
  }
}
\`\`\`

<span id="6e9f7218"></span>
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
         DataType: "uri", // 必选。参考图的地址类型。支持传入 url 或 uri。详见本文的方式一：通过 API 调用 > 异步处理部分。
         DataList: ["a.png", "uridemo.png"], // 必选。参考图的 URL 或 URI 地址，可辅助生成图像。详见本文的方式一：通过 API 调用 > 异步处理部分。
         CallbackConf: { // 可选。回调配置。
           Method: "HTTP", // 必选。回调方式，取值固定为 HTTP。
           Endpoint: "https://demo.com", // 必选。回调地址，用于接收处理结果。
           DataFormat: "JSON",  // 可选。回调数据格式，支持取值 XML 和 JSON。
           Args: "productid",  // 可选。业务自定义回调参数。
           Type: "task",  // 可选。回调触发类型，支持取值 task 和 entry。默认值为 entry。
         },
         WorkflowParameter: "{\\"ArkSeedreamParam\\":{\\"ModelId\\":\\"seedream4\\",\\"Prompt\\":\\"星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。\\",\\"Size\\":\\"2048x2048\\",\\"Watermark\\":true,\\"EnableImageConversion\\":false,\\"SequentialImageGeneration\\":\\"auto\\",\\"SequentialImageGenerationOptions\\":{\\"MaxImages\\":3},\\"OptimizePromptOptions\\":{\\"Mode\\":\\"standard\\"}}}",  // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
         WorkflowTemplateId: "system_workflow_ark_seedream", // 必选。模板 ID。固定取值。
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

<span id="371f8045"></span>
## 步骤二：查看结果图

```mixin-react
return (<Tabs>
<Tabs.TabPane title="方式一：默认公网加速域名访问结果图" key="EvI5aNOgXm"><RenderMd content={`<span id="e5a9a7c3"></span>
### 通过调用服务端 SDK 获取资源地址（推荐）
veImageX 提供了以下编程语言的 SDK，方便您调用 API。详见[方式一：通过调用服务端 SDK 获取资源地址（推荐）](/docs/508/2164787#0e6382e6)。
<span id="e6f1b5e7"></span>
### 通过控制台获取资源地址
在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取资源地址。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5ef7b5739f364dc080c80c0456452a21~tplv-goo7wpa0wc-image.image =2396x)

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式二：控制台预览结果图" key="bTxv3ZAfhf"><RenderMd content={`

* 未新增自定义域名时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面搜索结果图的存储 URI。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f2b2412712a4d70b4d77641c9b1c2a5~tplv-goo7wpa0wc-image.image =2908x)
* 已[新增自定义域名](/docs/508/174565)时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取结果图的 URL 地址。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6707099e11a040babc2e8390eaa507c1~tplv-goo7wpa0wc-image.image =2904x)


`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式三：手动拼接结果图地址" key="qEOmvYd0mq"><RenderMd content={`拼接格式如下所示。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/85c2cdf85b1b463a99adf02beb4ea634~tplv-goo7wpa0wc-image.image =870x)
:::tip
* 确保已[新增自定义域名](/docs/508/174565)。
* 如无添加水印、调整分辨率等二次处理需求，使用服务下**获取原图**默认模板的名称拼接结果图地址即可。
* 如果存在中文字符，则以其 16 进制表示。
:::
`}></RenderMd></Tabs.TabPane></Tabs>);
 ```

<span id="7cf3ab1d"></span>
# 模板说明
<span id="115b6703"></span>
## 模板 ID
`system_workflow_ark_seedream`
<span id="c76e66af"></span>
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
  },{
    "title": "是否必选",
    "dataIndex": "column_2"
  },{
  title: "示例值",
  dataIndex: "column_3"
},{
  title: "说明",
  dataIndex: "column_4"
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
  "column_4": <>参考图的地址类型。支持传入 url 或 uri。</>,
    }, {
      "key": 2,
      "children": [],
      "column_0": "ObjectKey\n",
      "column_1": "String",
  "column_2": "是",
  "column_3": "a.png",
  "column_4": <>参考图的 URL 或 URI 地址。<ul><li>当 DataType 取值为 url 时：传入公网可访问的 URL 地址，例如 https://example.com/static/demo1.png。</li> <li>当 DataType 取值为 uri 时：传入指定服务 ID 下不包含 tos-*-i-*  前缀的存储 URI，例如存储 URI 为 tos-m*a-i-0ksq****qe/image-a/example.jpg，则传入 image-a/example.jpg。</li></ul></>,
    }],
    "column_0": "Input\n",
    "column_1": "Object",
  "column_2": "否",
  "column_3": "-",
  "column_4": <>输入的参考图信息，可辅助生成图像。<br />仅在调用同步处理接口 <a href="https://www.volcengine.com/docs/508/1515915">AIProcess</a> 且需根据参考图生成图像时必选。</>
  }, {
    "key": 4,
    "children": [{
      "key": 8,
      "children": [],
      "column_0": "ModelId\n",
      "column_1": "String",
  "column_2": "否",
  "column_3": "seedream4",
  "column_4":<>模型 ID。目前固定取值为 seedream4，即使用 doubao-seedream-4-0-250828 模型。默认值为 seedream4。</>
    }, {
      "key": 5,
      "children": [],
      "column_0": "Prompt\n",
      "column_1": "String",
  "column_2": "是",
  "column_3": "星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬。",
  "column_4":<>用于生成图像的提示词。<br />建议不超过 300 个汉字或 600 个英文单词。字数过多信息容易分散，模型可能因此忽略细节，只关注重点，造成图片缺失部分元素。详情可参见<a href="https://www.volcengine.com/docs/82379/1829186"> Seedream 4.0 提示词指南</a> 。</>
    }, {
      "key": 6,
      "children": [],
      "column_0": "Size\n",
      "column_1": "String",
  "column_2": "否",
  "column_3": "2048x2048",
  "column_4":<>生成图像的尺寸信息。支持以下两种方式，不可混用。默认使用方式二，并指定生成图像的宽度和高度为 2048x2048 px。<ul><li>方式一：指定生成图像的分辨率，并在提示词中用自然语言描述图片宽高比、图片形状或图片用途，最终由模型判断生成图片的大小。可选值：1K、2K、4K。</li><li>方式二：指定生成图像的宽度和高度，单位为 px。默认值为 2048x2048，取值范围为 [1280x720, 4096x4096]，宽高比范围为 [1/16, 16]。</li></ul></>
    }, {
      "key": 7,
      "children": [],
      "column_0": "Watermark\n",
      "column_1": "Boolean",
  "column_2": "否",
  "column_3": "true",
  "column_4":<>是否在生成的图像中添加水印。默认值为 true。<ul><li>true：在图像右下角添加“AI生成”字样的水印标识。</li><li>false：不添加水印。</li></ul></>
    }, {
      "key": 9,
      "children": [],
      "column_0": "SequentialImageGeneration\n",
      "column_1": "String",
  "column_2": "否",
  "column_3": "disabled",
  "column_4":<>是否关闭组图（一组内容关联的图像）功能。默认值为 disabled。在调用同步处理接口 <a href="https://www.volcengine.com/docs/508/1515915">AIProcess</a> 时，仅支持取值 disabled。<ul><li>auto：自动判断模式，模型会根据用户提供的提示词自主判断是否返回组图以及组图包含的图片数量。</li><li>disabled：关闭组图功能，模型只会生成一张图。</li></ul></>,
    }, {
      "key": 8,
      "children": [],
      "column_0": "EnableImageConversion\n",
      "column_1": "Boolean",
  "column_2": "否",
  "column_3": "false",
  "column_4":<>是否转换参考图的格式或大小。该参数在满足以下任一条件时生效。<ul><li>参考图格式为 .webp、.awebp、.gif、.tiff、.bmp、.ico、.heic 或 .heif。</li><li>参考图大于 10 MB。</li></ul>默认值为 false。取值如下：<ul><li>true：转换。将参考图转换为不超过 10 MB 的 .jpeg 格式后传入。动图会截取第一帧转换为 .jpeg 格式。</li><li>false：不进行转换，满足条件时直接报错。</li></ul></>
    },{
      "key": 10,
      "children": [{
        "key": 11,
        "children": [],
        "column_0": "MaxImages\n",
        "column_1": "Integer",
  "column_2": "否",
  "column_3": "3",
  "column_4":<>本次请求最多可生成的图像数量。取值范围为 [1, 15]。<br />默认无数量限制，但参考图数量和生成的图像数量总和最多为 15 张。<br />仅在调用异步处理接口 <a href="https://www.volcengine.com/docs/508/1515916">CreateImageAITask</a> 或使用批量处理功能时生效。</>
      }],
      "column_0": "SequentialImageGenerationOptions\n",
      "column_1": "Object",
  "column_2": "否",
  "column_3": "-",
  "column_4":<>组图功能配置。仅在 SequentialImageGeneration 取值为 auto 时生效。</>
    }, {
      "key": 12,
      "children": [{
        "key": 13,
        "children": [],
        "column_0": "Mode\n",
        "column_1": "String",
  "column_2": "否",
  "column_3": "standard",
  "column_4":<>对用户输入的提示词进行优化的模式。默认值为 standard。<ul><li>standard：标准模式，生成图像的质量更高，耗时较长。</li><li>fast：快速模式，生成图像的耗时更短，质量一般。</li></ul></>
      }],
      "column_0": "OptimizePromptOptions\n",
      "column_1": "Object",
  "column_2": "否",
  "column_3": "-",
  "column_4":<>提示词优化功能配置。</>
    }],
    "column_0": "ArkSeedreamParam\n",
    "column_1": "Object",
  "column_2": "是",
  "column_3": "-",
  "column_4":"SeeDream 生图参数。\n"
  }]
}); 
return <Table border={{ cell: true, wrapper: true }} pagination={false} {...properties} />;
```

<span id="d3c99caf"></span>
## 输出参数
veImageX 服务会将输出参数序列化为 JSON 字符串后作为 [AIProcess](https://www.volcengine.com/docs/508/1515915) 接口、[回调](https://www.volcengine.com/docs/508/1526662)或 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913) 接口的 `Output` 参数返回。
:::tip
生成的图像在控制台**资源管理**页面默认不展示，仅支持通过不包含 `tos-*-i-*` 前缀的存储 URI 搜索。
:::

```mixin-react
const properties = ({
columns: [{
  title: "参数",
  dataIndex: "column_0"
}, {
  title: "类型",
  dataIndex: "column_1"
}, {
  title: "示例值",
  dataIndex: "column_2"
}, {
  title: "说明",
  dataIndex: "column_3"
}],
data: [{
  key: 1,
  children: [],
  column_0: "Model",
  column_1: "String",
  column_2: "doubao-seedream-4-0-250828",
  column_3: "模型 ID，格式为模型名称-版本。目前固定取值为 doubao-seedream-4-0-250828。"
}, {
  key: 2,
  children: [{
    key: 3,
    children: [],
    column_0: "Uri",
    column_1: "String",
    column_2: "a.jpeg",
    column_3: "指定服务 ID 下不包含 tos-*-i-*  前缀的存储 URI。"
  }, {
    key: 4,
    children: [],
    column_0: "Size",
    column_1: "String ",
    column_2: "2048x2048",
    column_3: "生成图像的宽度和高度，单位为 px。"
  }, {
    key: 5,
    children: [{
      key: 6,
      children: [],
      column_0: "Code",
      column_1: "String",
      column_2: "InvaildAccountStatus",
      column_3: <>错误码。详见<a href="https://www.volcengine.com/docs/82379/1299023">错误码</a>。</>
    }, {
      key: 7,
      children: [],
      column_0: "Message",
      column_1: "String",
      column_2: "There is an issue with your account status. If you need assistance, please contact the platform administrators.",
      column_3: "错误提示信息。"
    }],
    column_0: "Error",
    column_1: "Object",
    column_2: "-",
    column_3: "某张图像生成失败时的错误信息。仅在生成多张图像时可能返回该参数。"
  }],
  column_0: "Data",
  column_1: "Array of Object",
  column_2: "-",
  column_3: "生成图像的信息。"
}, {
  key: 5,
  children: [{
    key: 6,
    children: [],
    column_0: "GeneratedImages",
    column_1: "Integer",
    column_2: "3",
    column_3: "成功生成的图像张数。"
  }],
  column_0: "Usage",
  column_1: "Object",
  column_2: "-",
  column_3: "本次请求的用量信息。"
}, {
  key: 7,
  children: [{
    key: 8,
    children: [],
    column_0: "Code",
    column_1: "String",
    column_2: "InvaildAccountStatus",
    column_3: <>错误码。详见<a href="https://www.volcengine.com/docs/82379/1299023">错误码</a>。</>
  }, {
    key: 9,
    children: [],
    column_0: "Message",
    column_1: "String",
    column_2: "There is an issue with your account status. If you need assistance, please contact the platform administrators.",
    column_3: "错误提示信息。"
  }],
  column_0: "Error",
  column_1: "Object ",
  column_2: "- ",
  column_3: "本次请求，如发生错误，对应的错误信息。"
}]
}); 
return <Table border={{ cell: true, wrapper: true }} pagination={false} {...properties} />;
```


