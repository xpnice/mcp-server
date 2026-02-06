AIGC 图片翻译附加组件利用 AI 能力，通过集成图像识别、机器翻译、大模型翻译、图片修复与擦除等多项技术，支持识别并翻译图片中的文本内容，最终生成指定语言的图片。本文介绍如何使用 AIGC 图片翻译附加组件。
<span id="ce427b0c"></span>
# 效果示例

| | | | | \
|场景 |模型 |原图 |翻译效果 |
|---|---|---|---|
| | | | | \
|电商 |擦除 |![Image](https://p3-imagex.byteimg.com/imagex-common/oQdfAyCtAm1kRGDkAAgFs0IsIfn0oGECsA5tkC~tplv-obj.image =998x) |![Image](https://p3-imagex.byteimg.com/imagex-common/ocGA5IDfFAsH0nkqAt7SCC2mL6MIACAfgoknYE~tplv-obj.image =998x) |
| | | | | \
|电商 |非擦除 |![Image](https://p3-imagex.byteimg.com/imagex-common/ogrADAI4RTBOJAQgvAAapEaZT2SFpgdik6iNv~tplv-obj.image =998x) |![Image](https://p3-imagex.byteimg.com/imagex-common/osmLsHIgCLCFmEknGetk00fZA5DHACAAZAIoMk~tplv-obj.image =998x) |
| | | | | \
|漫画 |擦除 |![Image](https://p3-imagex.byteimg.com/imagex-common/oIA3Ei42gNIspTBgOgaaSurAA78JDRo4AAivk~tplv-obj.image =910x) |![Image](https://p3-imagex.byteimg.com/imagex-common/oMf0TSjBaBAiTTgEAARA5ABdhtcQk0JvBTWSiD~tplv-obj.image =910x) |
| | | | | \
|漫画 |非擦除 |![Image](https://p3-imagex.byteimg.com/imagex-common/oEfoMptDm4D0QS9EbTF5GEAkAeASAgC4kgAC0C~tplv-obj.image =910x) |![Image](https://p3-imagex.byteimg.com/imagex-common/owgglANyvDRAAAiTiavECS6JIrpaBgOukLYRA~tplv-obj.image =910x) |
| | | | | \
|文献 |擦除 |![Image](https://p3-imagex.byteimg.com/imagex-common/oYAHAfriBAD0iAZTkSiTS1EkaBBA8TlQynWtcB~tplv-obj.image =3000x) |![Image](https://p3-imagex.byteimg.com/imagex-common/oo0ABxSZkBSESBiW3A0AKkkAAaT6QxfDLcTBiR~tplv-obj.image =3000x) |
| | | | | \
|文献 |非擦除 |![Image](https://p3-imagex.byteimg.com/imagex-common/oADSACDGACL07EEQkftTmZyAl55XkgDfAYCAFo~tplv-obj.image =3000x) |![Image](https://p3-imagex.byteimg.com/imagex-common/osfoZltDmQD0oSjEmTF5JEAkA0AeAgC1kQACWC~tplv-obj.image =3000x) |

<span id="0829f23b"></span>
# 使用场景
<span id="2d48cd62"></span>
## 跨境电商
跨境电商从业者或消费者在浏览海外商品详情页、核对物流面单、查看商品说明书（如家电参数、美妆成分表）时，常面临图文混合的语言障碍，可以使用图片翻译能力解决问题。
<span id="deafb716"></span>
## 漫画翻译
漫画爱好者阅读海外原版漫画（如日漫、美漫、韩漫）时，对话框文字、场景注释、角色名称等多以图片形式呈现，手动输入翻译效率极低，可以使用图片翻译能力解决效率问题。
<span id="0440dbbd"></span>
## 行业文献
科研人员、企业从业者在查阅海外行业文献，常遇到图文结合的专业内容（如公式旁的外文注释、图表标题、技术术语），可以使用图片翻译能力解决问题。
<span id="0fff24ed"></span>
## 出境游学
学生或游客在出境游学、旅行时，会接触大量公共场景的图片类信息，如路牌、菜单、景区导览图、校园通知海报、地铁线路图等，可以使用图片翻译能力解决问题。
<span id="eb7001f4"></span>
# 使用限制
为确保能够生成图像，请满足以下限制。

* **输入大小**：单张图 <= 10 MB。如果超出 10 MB，请先通过模板压缩图片大小。
* **输入分辨率**：大于 10 x 10 像素且小于等于 1000 万像素。如果为其他分辨率，请先通过模板变更图片分辨率。
* **输入格式**：.jpeg、.webp、.png 等，不支持动图。
* **输出格式**：.jpeg、.webp、.png 等，不支持动图。

<span id="c672487a"></span>
# 使用方法
<span id="d5ba5eb4"></span>
## 前提条件

* 已[开通 veImageX 产品服务](https://www.volcengine.com/docs/508/8084#%E5%BC%80%E9%80%9A-veimagex-%E4%BA%A7%E5%93%81%E6%9C%8D%E5%8A%A1)并[创建服务](https://www.volcengine.com/docs/508/357114)。
* 已开通[智能处理计费配置](https://www.volcengine.com/docs/508/1262340#%E5%BC%80%E9%80%9A%E6%99%BA%E8%83%BD%E5%A4%84%E7%90%86%E8%AE%A1%E8%B4%B9%E9%85%8D%E7%BD%AE)。
* （可选）如需完成以下操作，确保已[新建模板](/docs/508/8087)。
   * 处理输入图像：如果输入图像不符合输入限制，您可以通过模板来压缩图片大小或变更图片格式等，再将处理后的图片作为输入图像。
   * 处理生成图像：对生成的图像进行二次处理，例如添加水印或调整分辨率。

<span id="5e1c5503"></span>
## 步骤一：调用 AI 能力
<span id="da165f37"></span>
### 方式一：通过 API 调用
<span id="0056beb1"></span>
#### 同步处理
调用同步处理接口 [AIProcess](https://www.volcengine.com/docs/508/1515915)，提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。
**请求示例**
```JSON
POST https://imagex.volcengineapi.com/?Action=AIProcess&Version=2023-05-01
{
    "ServiceId": "91**2g", // 必选。服务 ID。
    "WorkflowTemplateId": "system_workflow_image_translate", // 必选。模板 ID。
    "WorkflowParameter": "{\"Input\":{\"ObjectKey\":\"example.webp\",\"DataType\":\"uri\"},\"TranslateParam\":{\"ModelId\":\"seed-translation\",\"SourceLang\":\"zh\",\"TargetLang\":\"en\",\"OutputFormat\":\"png\"}}" // 必选。模板参数。
}
```

其中，

* `ServiceId`：服务 ID，可从[服务管理](https://console.volcengine.com/imagex/service_manage/)页面获取。
* `WorkflowTemplateId`：取值固定为 `system_workflow_image_translate`。
* `WorkflowParameter`：根据[输入参数](/docs/508/1856117#d23484f8)，设置该参数取值。

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
        "Output": "{\"ObjectKey\":\"a.png\",\"Size\":54509,\"Format\":\"png\"}"
    }
}
```

`Output` 的参数含义详见[输出参数](/docs/508/1856117#b9386675)。
<span id="bebae7d9"></span>
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
       "WorkflowParameter": "{\"TranslateParam\":{\"ModelId\":\"seed-translation\",\"SourceLang\":\"zh\",\"TargetLang\":\"en\",\"OutputFormat\":\"png\"}}", // 必选。模板参数。
       "WorkflowTemplateId": "system_workflow_image_translate", // 必选。模板 ID。
       "QueueId": "62f224ce61****826e38c29a" // 必选。队列 ID。
   }
   ```

   其中，
   * `WorkflowTemplateId`：取值固定为 `system_workflow_image_translate`。
   * `WorkflowParameter`：根据[输入参数](/docs/508/1856117#d23484f8)，设置该参数取值。
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

<span id="f8c1bc7c"></span>
### 方式二：通过服务端 SDK 调用
veImageX 提供了以下编程语言的 SDK，方便您调用 API。

```mixin-react
return (<Tabs>
<Tabs.TabPane title="Golang SDK" key="M8xY3t640u"><RenderMd content={`<span id="e93dd8e6"></span>
#### 前提条件
调用接口前，请先完成 Golang SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23757)操作。
<span id="4325964c"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1856117#0056beb1)。
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
                  WorkflowTemplateID: "system_workflow_image_translate",   // 必选。模板 ID。固定取值。
                  WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
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

<span id="bd32e0fd"></span>
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
                  WorkflowParameter:  "{\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
                  WorkflowTemplateID: "system_workflow_image_translate",                                                // 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Python SDK" key="fIPY8FlMty"><RenderMd content={`<span id="c6ea7bb0"></span>
#### 前提条件
调用接口前，请先完成 Python SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23774)操作。
<span id="bd186b4b"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1856117#0056beb1)。
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
        "WorkflowTemplateId": "system_workflow_image_translate",  # # 必选。模板 ID。固定取值。
        "WorkflowParameter": "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}" # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    }
    query = {}

    resp = service.ai_process(query, body)
    print(resp)
\`\`\`

<span id="6ca92b12"></span>
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
           "WorkflowParameter": "{\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}",  # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
           "WorkflowTemplateId": "system_workflow_image_translate"  # 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Java SDK" key="xu6mFghrTP"><RenderMd content={`<span id="c2a85eb7"></span>
#### 前提条件
调用接口前，请先完成 Java SDK 的[安装及初始化](https://www.volcengine.com/docs/508/66513)操作。
<span id="abd0152b"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1856117#0056beb1)。
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
         body.setWorkflowTemplateId("system_workflow_image_translate"); // 必选。模板 ID。固定取值。
         body.setWorkflowParameter("{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
 
        try {
            AIProcessRes resp = service.aIProcess(body);
            System.out.println(resp);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
\`\`\`

<span id="73fec12c"></span>
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
        "\\"TranslateParam\\":{" +
        "\\"ModelId\\":\\"seed-translation\\"," +
        "\\"SourceLang\\":\\"zh\\"," +
        "\\"TargetLang\\":\\"en\\"," +
        "\\"OutputFormat\\":\\"png\\"" +
        "}" +
        "}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        body.setWorkflowTemplateId("system_workflow_image_translate"); // 必选。模板 ID。固定取值。
       
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
<Tabs.TabPane title="PHP SDK" key="JSlXpvIs46"><RenderMd content={`<span id="25758c9a"></span>
#### 前提条件
调用接口前，请先完成 PHP SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23778)操作。
<span id="e58c7f37"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1856117#0056beb1)。
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
     "WorkflowTemplateId" => "system_workflow_image_translate", // 必选。模板 ID。固定取值。
     "WorkflowParameter" => "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
];
$query = [];

$response = $client->AIProcess($query, $body);
print_r($response);
\`\`\`

<span id="1cf5c6fd"></span>
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
        "WorkflowParameter" => "{\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        "WorkflowTemplateId" => "system_workflow_image_translate" // 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Node.js SDK" key="J4jDBMdiE7"><RenderMd content={`<span id="a7f2745f"></span>
#### 前提条件
调用接口前，请先完成 Node.js SDK 的[安装及初始化](https://www.volcengine.com/docs/508/1250175)操作。
<span id="25db7ca7"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/1856117#0056beb1)。
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
      WorkflowTemplateId: "system_workflow_image_translate",   // 必选。模板 ID。固定取值。
      WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"example.webp\\",\\"DataType\\":\\"uri\\"},\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    };

    const res = await Client.AIProcess(requestParam);
    console.log("res", res);
  } catch (err) {
    console.error(err);
  }
}
\`\`\`

<span id="68c107b3"></span>
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
         WorkflowParameter: "{\\"TranslateParam\\":{\\"ModelId\\":\\"seed-translation\\",\\"SourceLang\\":\\"zh\\",\\"TargetLang\\":\\"en\\",\\"OutputFormat\\":\\"png\\"}}",  // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
         WorkflowTemplateId: "system_workflow_image_translate", // 必选。模板 ID。固定取值。
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

<span id="74c8db0e"></span>
## 步骤二：查看结果图

```mixin-react
return (<Tabs>
<Tabs.TabPane title="方式一：默认公网加速域名访问结果图" key="Po5kO0bnLo"><RenderMd content={`<span id="39c1ebb3"></span>
### 通过调用服务端 SDK 获取资源地址（推荐）
veImageX 提供了以下编程语言的 SDK，方便您调用 API。详见[方式一：通过调用服务端 SDK 获取资源地址（推荐）](/docs/508/2164787#0e6382e6)。
<span id="ae70856e"></span>
### 通过控制台获取资源地址
在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取资源地址。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/61a09f12a7c7418f9db5f8c5090cfad5~tplv-goo7wpa0wc-image.image)

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式二：控制台预览结果图" key="EUK5fQmggp"><RenderMd content={`

* 未新增自定义域名时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面搜索结果图的存储 URI。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f2b2412712a4d70b4d77641c9b1c2a5~tplv-goo7wpa0wc-image.image =2908x)
* 已[新增自定义域名](/docs/508/174565)时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取结果图的 URL 地址。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6707099e11a040babc2e8390eaa507c1~tplv-goo7wpa0wc-image.image =2904x)


`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式三：手动拼接结果图地址" key="H2OW4CXVHj"><RenderMd content={`拼接格式如下所示。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/85c2cdf85b1b463a99adf02beb4ea634~tplv-goo7wpa0wc-image.image =870x)
:::tip
* 确保已[新增自定义域名](/docs/508/174565)。
* 如无添加水印、调整分辨率等二次处理需求，使用服务下**获取原图**默认模板的名称拼接结果图地址即可。
* 如果存在中文字符，则以其 16 进制表示。
:::
`}></RenderMd></Tabs.TabPane></Tabs>);
 ```

<span id="4ab00564"></span>
# 模板说明
<span id="2cc314e2"></span>
## 模板 ID
`system_workflow_image_translate`
<span id="d23484f8"></span>
## 输入参数
您需要将输入参数序列化为 JSON 字符串后，作为同步处理接口 [AIProcess](https://www.volcengine.com/docs/508/1515915) 或异步处理接口 [CreateImageAITask](https://www.volcengine.com/docs/508/1515916) 的 `WorkflowParameter` 参数传入，或作为批量处理时的模板配置参数传入。 

```mixin-react
const properties = ({
columns: [{
  title: "参数",
  dataIndex: "column_0"
}, {
  title: "类型",
  dataIndex: "column_1"
}, {
  title: "是否必选",
  dataIndex: "column_2"
}, {
  title: "示例值",
  dataIndex: "column_3"
}, {
  title: "说明",
  dataIndex: "column_4"
}],
data: [{
  key: 1,
  children: [{
    key: 2,
    children: [],
    column_0: "DataType",
    "column_1": "String",
      "column_2": "是",
      "column_3": "uri",
      "column_4": <>输入图像的地址类型。支持传入 url 或 uri。</>
  }, {
    key: 3,
    children: [],
    column_0: "ObjectKey",
        "column_1": "String",
      "column_2": "是",
      "column_3": "a.png",
      "column_4": <>输入图像的 URL 或 URI 地址。<ul><li>当 DataType 取值为 url 时：传入公网可访问的 URL 地址，例如 https://example.com/static/demo1.png。</li> <li>当 DataType 取值为 uri 时：传入指定服务 ID 下不包含 tos-*-i-* 前缀的存储 URI，例如存储 URI 为 tos-m*a-i-0ksq****qe/image-a/example.jpg，则传入 image-a/example.jpg。</li></ul></>
  }],
  column_0: "Input",
    "column_1": "Object",
    "column_2": "否",
    "column_3": "-",
    "column_4": <>输入图像的信息。<br />仅在调用同步处理接口 <a href="https://www.volcengine.com/docs/508/1515915">AIProcess</a> 时必选。</>
}, {
  key: 4,
  children: [{
    key: 5,
    children: [],
    column_0: "ModelId",
    column_1: "String",
    column_2: "是",
    column_3: "seed-translation",
    column_4: <>模型。取值如下：<ul><li>default：
非擦除翻译区域模型。在翻译图片时，不会对原图进行任何修改。翻译后的文本会直接叠加在原始文本上。</li><li>erase：擦除翻译区域模型。在翻译图片时，先擦除翻译区域，再将翻译后的文本放置在翻译区域中。</li><li>seed-translation：大模型版擦除模型。使用 <a href="https://www.volcengine.com/docs/82379/1820188">doubao-seed-translation 模型</a>翻译图片，先擦除翻译区域，再将翻译后的文本放置在翻译区域中。doubao-seed-translation 模型是字节跳动自研的多语言翻译模型，支持数十种语言互译，提供忠实、地道、流畅的译文，中英翻译效果逼近 Deepseek-R1，通用多语言翻译效果超越或持平 GPT-4o / Gemini-2.5-Pro，能精准适配办公和娱乐等多场景需求。</li><li>dense-text-translation：密集文本非擦除模型。适用于文字密集型翻译场景。翻译后的文本会直接叠加在原始文本上。</li><li>logo-retain-erase-translation：带品牌识别的擦除模型。在翻译图片时，保持品牌名称不被翻译。先擦除翻译区域，再将翻译后的文本放置在翻译区域中。</li></ul></>
  }, {
    key: 6,
    children: [],
    column_0: "SourceLang",
    column_1: "String",
    column_2: "否",
    column_3: "zh",
    column_4: <>源语言。不传该参数，则自动识别原图中的源语言。<ul><li>ModelId 取值非 seed-translation 时，源语言具体取值详见本文附录 > 源语言支持列表中的语种编号。</li><li>ModelId 取值为 seed-translation 时，源语言具体取值详见<a href="https://www.volcengine.com/docs/82379/1820188#%E6%94%AF%E6%8C%81%E7%BF%BB%E8%AF%91%E8%AF%AD%E7%A7%8D">支持翻译语种</a>中的语种编号（lang_code）。注意：中文（繁体）的语种编号请使用 zh_hant。</li></ul></>
  }, {
    key: 7,
    children: [],
    column_0: "TargetLang",
    column_1: "String",
    column_2: "是",
    column_3: "en",
    column_4: <>目标语言。<ul><li>ModelId 取值非 seed-translation 时，目标语言具体取值详见本文附录 >目标语言支持列表中的语种编号。</li><li>ModelId 取值为 seed-translation 时，目标语言具体取值详见<a href="https://www.volcengine.com/docs/82379/1820188#%E6%94%AF%E6%8C%81%E7%BF%BB%E8%AF%91%E8%AF%AD%E7%A7%8D">支持翻译语种</a>中的语种编号（lang_code）。注意：中文（繁体）的语种编号请使用 zh_hant。</li></ul></>
  }, {
    key: 8,
    children: [],
    column_0: "OutputFormat",
    column_1: "String",
    column_2: "否",
    column_3: "png",
    column_4: <>输出图片的格式。不传则与原图格式相同。支持以下取值：<ul><li>jpg 或 jpeg</li><li>png</li><li>webp</li></ul></>
  }],
  column_0: "TranslateParam",
  column_1: "Object",
  column_2: "是",
  column_3: "-",
  column_4: "生成图片参数。"
}]
}); 
return <Table border={{ cell: true, wrapper: true }} pagination={false} {...properties} />;
```

<span id="b9386675"></span>
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

<span id="54e7b87d"></span>
# 附录
<span id="fff28ee4"></span>
## 源语言支持列表

| | | \
|语种编号 |语种中文名 |
|---|---|
| | | \
|ar |阿拉伯语 |
| | | \
|fr |法语 |
| | | \
|en |英语 |
| | | \
|ca |加泰罗尼亚语 |
| | | \
|pt |葡萄牙语 |
| | | \
|es |西班牙语 |
| | | \
|nl |荷兰语 |
| | | \
|de |德语 |
| | | \
|sl |斯洛文尼亚语 |
| | | \
|az |阿塞拜疆语 |
| | | \
|bn |孟加拉语 |
| | | \
|ru |俄语 |
| | | \
|no |挪威语 |
| | | \
|ms |马来语 |
| | | \
|zh |中文 |
| | | \
|zh_hant |中文（繁体） |
| | | \
|cs |捷克语 |
| | | \
|sk |斯洛伐克语 |
| | | \
|pl |波兰语 |
| | | \
|hu |匈牙利语 |
| | | \
|vi |越南语 |
| | | \
|da |丹麦语 |
| | | \
|fi |芬兰语 |
| | | \
|sv |瑞典语 |
| | | \
|id |印尼语 |
| | | \
|he |希伯来语 |
| | | \
|it |意大利语 |
| | | \
|ja |日语 |
| | | \
|ko |韩语 |
| | | \
|ta |泰米尔语 |
| | | \
|th |泰语 |
| | | \
|tr |土耳其语 |

<span id="70e8add9"></span>
## 目标语言支持列表

| | | \
|语种编号 |语种中文名 |
|---|---|
| | | \
|zh |中文 |
| | | \
|zh_hant |中文（繁体） |
| | | \
|en |英语 |
| | | \
|ja |日语 |
| | | \
|ko |韩语 |
| | | \
|ar |阿拉伯语 |
| | | \
|pt |葡萄牙语 |
| | | \
|fr |法语 |
| | | \
|de |德语 |
| | | \
|es |西班牙语 |
| | | \
|id |印尼语 |
| | | \
|it |意大利语 |
| | | \
|ms |马来语 |
| | | \
|ru |俄语 |
| | | \
|th |泰语 |
| | | \
|vi |越南语 |


