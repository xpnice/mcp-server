文字识别 OCR 附加组件利用 AI 能力，可将图片中的文字信息转换为可编辑文本。该组件支持通用印刷体和营业执照识别场景，为您提供文字内容（支持简体中文和英文）及文字框坐标，从而提高您的信息处理效率。本文介绍如何使用文字识别 OCR 附加组件。
![Image](https://p3-imagex.byteimg.com/imagex-common/fb03608fd18d4136b519cf8f54782b26~tplv-j7r2secxx9-resize:1080:q75.image =500x)
<span id="应用场景"></span>
# 使用场景

* **资质审查**：在银行、信贷、零售和电商等行业中，识别并核验营业执照、商标注册证等证件。这有助于节省人力成本、提高审核效率，并有效降低业务风险。
* **内容审核与管理**：在社交、电商等平台，识别图片中的违规文字，例如不文明用语、涉黄、涉暴等内容。这有助于快速定位问题图片并进行审核，从而有效规避业务风险。
* **纸质文件内容电子化**：将书本、论文、档案、PPT 等印刷文件内容快速电子化。识别并整理纸质文件中的文本，可方便学校、图书馆、企事业单位等进行资料录入，进而提高内容整理的效率。

<span id="c688d46e"></span>
# 使用限制
为确保能够生成图像，请满足以下限制。

* **输入分辨率**：短边 ≤ 2160 px，长边 ≤ 3840 px。如果为其他分辨率，请先通过模板变更图片分辨率。
* **输入大小**：单张图 ≤ 10 MB。如果超出 10 MB，请先通过模板压缩图片大小。
* **输入格式**：.png、.jpg、.jpeg、.webp、.heic、.avif。如果为其他格式，请先通过模板变更图片格式。

<span id="6909299d"></span>
# 使用方法
<span id="a6efdc98"></span>
## 前提条件

* 已[开通 veImageX 产品服务](https://www.volcengine.com/docs/508/8084#%E5%BC%80%E9%80%9A-veimagex-%E4%BA%A7%E5%93%81%E6%9C%8D%E5%8A%A1)并[创建服务](https://www.volcengine.com/docs/508/357114)。
* 已开通[智能处理计费配置](https://www.volcengine.com/docs/508/1262340#%E5%BC%80%E9%80%9A%E6%99%BA%E8%83%BD%E5%A4%84%E7%90%86%E8%AE%A1%E8%B4%B9%E9%85%8D%E7%BD%AE)。
* （可选）如需完成以下操作，确保已[新建模板](/docs/508/8087)。
   * 处理输入图像：如果输入图像不符合输入限制，您可以通过模板来压缩图片大小或变更图片格式等，再将处理后的图片作为输入图像。
   * 处理生成图像：对生成的图像进行二次处理，例如添加水印或调整分辨率。

<span id="7fbabf2c"></span>
## 步骤一：调用 AI 能力
<span id="c31c95b4"></span>
### 方式一：通过 API 调用
<span id="fd1df771"></span>
#### 同步处理
调用同步处理接口 [AIProcess](https://www.volcengine.com/docs/508/1515915)，提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。
**请求示例**
```JSON
POST https://imagex.volcengineapi.com/?Action=AIProcess&Version=2023-05-01
{
    "ServiceId": "91**2g", // 必选。服务 ID。
    "WorkflowTemplateId": "system_workflow_image_ocr", // 必选。模板 ID。
    "WorkflowParameter": "{\"Input\":{\"ObjectKey\":\"example.webp\",\"DataType\":\"uri\"},\"OCRParam\":{\"ModelId\":\"default\",\"Scene\":\"general\"}}" // 必选。模板参数。
}
```

其中，

* `ServiceId`：服务 ID，可从[服务管理](https://console.volcengine.com/imagex/service_manage/)页面获取。
* `WorkflowTemplateId`：取值固定为 `system_workflow_image_ocr`。
* `WorkflowParameter`：根据[输入参数](/docs/508/136550#1daba5fd)，设置该参数取值。

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
        "Output": "{\"Scene\":\"general\",\"GeneralResult\":{\"Content\":\"TEST\",\"Location\":[[64,57],[140,57],[140,87],[64,87]],\"Confidence\":0.999030}}"
    }
}
```

`Output` 的参数含义详见[输出参数](/docs/508/136550#4e889bf7)。
<span id="9b679552"></span>
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
       "WorkflowParameter": "{\"OCRParam\":{\"ModelId\":\"default\",\"Scene\":\"general\"}}", // 必选。模板参数。
       "WorkflowTemplateId": "system_workflow_image_ocr", // 必选。模板 ID。
       "QueueId": "62f224ce61****826e38c29a" // 必选。队列 ID。
   }
   ```

   其中，
   * `WorkflowTemplateId`：取值固定为 `system_workflow_image_ocr`。
   * `WorkflowParameter`：根据[输入参数](/docs/508/136550#1daba5fd)，设置该参数取值。
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

<span id="e0a11ed1"></span>
### 方式二：通过服务端 SDK 调用
veImageX 提供了以下编程语言的 SDK，方便您调用 API。

```mixin-react
return (<Tabs>
<Tabs.TabPane title="Golang SDK" key="VIwxKz0KKt"><RenderMd content={`<span id="7c56be81"></span>
#### 前提条件
调用接口前，请先完成 Golang SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23757)操作。
<span id="6822b3d9"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/136550#fd1df771)。
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
                  WorkflowTemplateID: "system_workflow_image_ocr",   // 必选。模板 ID。固定取值。
                  WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
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

<span id="6006d010"></span>
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
                  WorkflowParameter:  "{\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
                  WorkflowTemplateID: "system_workflow_image_ocr",                                                // 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Python SDK" key="d3d0QbOaE8"><RenderMd content={`<span id="1e362cd6"></span>
#### 前提条件
调用接口前，请先完成 Python SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23774)操作。
<span id="8f2a591b"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/136550#fd1df771)。
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
        "WorkflowTemplateId": "system_workflow_image_ocr",  # # 必选。模板 ID。固定取值。
        "WorkflowParameter": "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}" # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    }
    query = {}

    resp = service.ai_process(query, body)
    print(resp)
\`\`\`

<span id="014a4534"></span>
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
           "WorkflowParameter": "{\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}",  # 必选。根据本文模板说明 > 输入参数，设置该参数取值。
           "WorkflowTemplateId": "system_workflow_image_ocr"  # 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Java SDK" key="SqKeZeQHZ6"><RenderMd content={`<span id="4d4c1267"></span>
#### 前提条件
调用接口前，请先完成 Java SDK 的[安装及初始化](https://www.volcengine.com/docs/508/66513)操作。
<span id="a22be72b"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/136550#fd1df771)。
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
         body.setWorkflowTemplateId("system_workflow_image_ocr"); // 必选。模板 ID。固定取值。
         body.setWorkflowParameter("{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
 
        try {
            AIProcessRes resp = service.aIProcess(body);
            System.out.println(resp);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
\`\`\`

<span id="239d0a34"></span>
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
        "\\"OCRParam\\":{" +
        "\\"ModelId\\":\\"default\\"," +
        "\\"Scene\\":\\"general\\"" +
        "}" +
        "}"); // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        body.setWorkflowTemplateId("system_workflow_image_ocr"); // 必选。模板 ID。固定取值。
       
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
<Tabs.TabPane title="PHP SDK" key="PvNuXvubK2"><RenderMd content={`<span id="1850d77f"></span>
#### 前提条件
调用接口前，请先完成 PHP SDK 的[安装及初始化](https://www.volcengine.com/docs/508/23778)操作。
<span id="7c34d3d6"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/136550#fd1df771)。
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
     "WorkflowTemplateId" => "system_workflow_image_ocr", // 必选。模板 ID。固定取值。
     "WorkflowParameter" => "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
];
$query = [];

$response = $client->AIProcess($query, $body);
print_r($response);
\`\`\`

<span id="7a4eb071"></span>
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
        "WorkflowParameter" => "{\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}", // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
        "WorkflowTemplateId" => "system_workflow_image_ocr" // 必选。模板 ID。固定取值。
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
<Tabs.TabPane title="Node.js SDK" key="yrLnbqxXoF"><RenderMd content={`<span id="74d304ce"></span>
#### 前提条件
调用接口前，请先完成 Node.js SDK 的[安装及初始化](https://www.volcengine.com/docs/508/1250175)操作。
<span id="cd9a8ed8"></span>
#### 同步处理
提交一条 URL 或 URI 资源执行同步 AI 图像处理任务。详见[同步处理](/docs/508/136550#fd1df771)。
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
      WorkflowTemplateId: "system_workflow_image_ocr",   // 必选。模板 ID。固定取值。
      WorkflowParameter: "{\\"Input\\":{\\"ObjectKey\\":\\"a.png\\",\\"DataType\\":\\"uri\\"},\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}" // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
    };

    const res = await Client.AIProcess(requestParam);
    console.log("res", res);
  } catch (err) {
    console.error(err);
  }
}
\`\`\`

<span id="2cad2a0c"></span>
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
         WorkflowParameter: "{\\"OCRParam\\":{\\"ModelId\\":\\"default\\",\\"Scene\\":\\"general\\"}}",  // 必选。根据本文模板说明 > 输入参数，设置该参数取值。
         WorkflowTemplateId: "system_workflow_image_ocr", // 必选。模板 ID。固定取值。
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

<span id="4d576f4c"></span>
## 步骤二：查看结果图

```mixin-react
return (<Tabs>
<Tabs.TabPane title="方式一：默认公网加速域名访问结果图" key="jCsNgaxuD9"><RenderMd content={`<span id="181c2749"></span>
### 通过调用服务端 SDK 获取资源地址（推荐）
veImageX 提供了以下编程语言的 SDK，方便您调用 API。详见[方式一：通过调用服务端 SDK 获取资源地址（推荐）](/docs/508/2164787#0e6382e6)。
<span id="43845b8e"></span>
### 通过控制台获取资源地址
在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取资源地址。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/21f69c86fc9e4e93ad8fd89c22952b10~tplv-goo7wpa0wc-image.image =2396x)

`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式二：控制台预览结果图" key="Xxk158iNFS"><RenderMd content={`

* 未新增自定义域名时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面搜索结果图的存储 URI。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f2b2412712a4d70b4d77641c9b1c2a5~tplv-goo7wpa0wc-image.image =2908x)
* 已[新增自定义域名](/docs/508/174565)时：在[资源管理](https://console.volcengine.com/imagex/resource_manage/)页面完成以下操作，获取结果图的 URL 地址。
   ![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6707099e11a040babc2e8390eaa507c1~tplv-goo7wpa0wc-image.image =2904x)


`}></RenderMd></Tabs.TabPane>
<Tabs.TabPane title="方式三：手动拼接结果图地址" key="pQTbaTV3T5"><RenderMd content={`拼接格式如下所示。
![Image](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/85c2cdf85b1b463a99adf02beb4ea634~tplv-goo7wpa0wc-image.image =870x)
:::tip
* 确保已[新增自定义域名](/docs/508/174565)。
* 如无添加水印、调整分辨率等二次处理需求，使用服务下**获取原图**默认模板的名称拼接结果图地址即可。
* 如果存在中文字符，则以其 16 进制表示。
:::
`}></RenderMd></Tabs.TabPane></Tabs>);
 ```

<span id="68740fe9"></span>
# 模板说明
<span id="2c6f8414"></span>
## 模板 ID
`system_workflow_image_ocr`
<span id="1daba5fd"></span>
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
  key: 4,
  children: [{
    key: 5,
    children: [],
    column_0: "ModelId",
    column_1: "String",
    column_2: "是",
    column_3: "default",
    column_4: "图像处理模型。目前仅支持取值 default。"
  }, {
    key: 6,
    children: [],
    column_0: "Scene",
    column_1: "String",
    column_2: "是",
    column_3: "general",
    column_4: <>图像 OCR 的识别场景。<br />目前仅支持识别图像中的简体中文和英文文本。取值如下：<ul><li>general：通用场景，用于识别通用印刷体文本。</li><li>license：营业执照场景，用于识别营业执照中的社会信用代码等文本信息。</li></ul></>
  }],
  column_0: "OCRParam",
  column_1: "Object",
  column_2: "是",
  column_3: "-",
  column_4: "文字识别 OCR 参数。"
}]
}); 
return <Table border={{ cell: true, wrapper: true }} pagination={false} {...properties} />;
```

<span id="4e889bf7"></span>
## 输出参数
veImageX 服务会将输出参数序列化为 JSON 字符串后作为 [AIProcess](https://www.volcengine.com/docs/508/1515915) 接口、[回调](https://www.volcengine.com/docs/508/1526662)或 [GetImageAIDetails](https://www.volcengine.com/docs/508/1515913) 接口的 `Output` 参数返回。

| | | | | \
|参数 |类型 |示例值 |说明 |
|---|---|---|---|
| | | | | \
|Scene |String |`general` |图像 OCR 的识别场景。取值如下： |\
| | | | |\
| | | |* `general`：通用场景，用于识别通用印刷体文本。 |\
| | | |* `license`：营业执照场景，用于识别营业执照中的社会信用代码等文本信息。 |
| | | | | \
|GeneralResult |List of <[GeneralTextInfo](/docs/508/136550#036b8789)> |{"Content":"TEST","Location":[[64,57],[140,57],[140,87],[64,87]],"Confidence":"0.999030"} |`Scene` 取值为 `general` 时的返回结果。 |
| | | | | \
|LicenseResult |Map<String,[GeneralTextInfo](/docs/508/136550#036b8789)> |\
| | |{"USCC":{"Content":"91330100****100Y43","Location":[[100, 50], [300, 50], [300, 80], [100, 80]]}, "address":{"Content":"北京市海淀区xx科技园","Location":[[100, 90], [400, 90], [400, 120], [100, 120]]}, "capital":{"Content":"1000万元人民币","Location":[[100, 130], [300, 130], [300, 160], [100, 160]]}, "corporation":{"Content":"张三","Location":[[100, 170], [200, 170], [200, 200], [100, 200]]}, "expiry_date":{"Content":"2030-12-31","Location":[[100, 210], [250, 210], [250, 240], [100, 240]]}, "name":{"Content":"北京市某某科技有限公司","Location":[[100, 20], [450, 20], [450, 50], [100, 50]]}, "register_date":{"Content":"2010-01-01","Location":[[100, 250], [250, 250], [250, 280], [100, 280]]}, "scope":{"Content":"技术开发、技术咨询、技术服务","Location":[[100, 290], [500, 290], [500, 350], [100, 350]]}} |当 `Scene` 取值为 `license` 时，返回一个包含以下字段的 Map 集合，其中每个字段值的结构均与 [GeneralTextInfo](/docs/508/136550#036b8789) 相同。 |\
| | | | |\
| | | |* `USCC`：统一社会信用代码，是企业的唯一身份标识码。  |\
| | | |* `address`：企业注册地址。 |\
| | | |* `capital`：注册资本。 |\
| | | |* `corporation`：法定代表人姓名。 |\
| | | |* `expiry_date`：营业执照的有效期截止日期。 |\
| | | |* `name`：企业名称。 |\
| | | |* `register_date`：企业注册日期。 |\
| | | |* `scope`：企业经营范围。 |

<span id="036b8789"></span>
### GeneralTextInfo

| | | | | \
|参数 |类型 |示例值 |说明 |
|---|---|---|---|
| | | | | \
|Content |String |TEST |文字内容。 |
| | | | | \
|Location |[][]int |[[64,57],[140,57],[140,87],[64,87]] |以图片左上角为坐标原点，按左上、右上、右下、左下的顺序提供文字框的坐标。 |
| | | | | \
|Confidence |Float |0.999030 |识别结果的可信度，取值范围为 [0,1]。数值越高，表示结果越可信。 |\
| | | |:::tip |\
| | | |仅在 `Scene` 取值为 `general` 时会返回该字段。 |\
| | | |::: |










