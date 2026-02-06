# veImageX MCP Server

veImageX 的 MCP Server 实现，为 MCP 客户端提供与火山引擎 veImageX 服务交互的能力。可以基于自然语言管理 veImageX 云端资源，查询服务信息，集成了包括文生图、AIGC 图片翻译、图像扩展等多项图像处理能力。

| 版本 | v0.2.0                   | 
|----|--------------------------|
| 描述 | 基于 MCP 管理 veImageX 资源，处理图片 |
| 分类 | 视频云                       |
| 标签 | 图像处理，素材托管              |

## 功能特性 (Tools)

本 MCP Server 提供以下核心工具：

### 基础管理工具
- **guide**: 获取 MCP 服务使用指南（**建议首次使用时调用**）。
- **get_all_imagex_services**: 获取所有服务信息（Service ID, Bucket, Domain 等）。
- **upload_images**: 上传本地图片到指定服务。
- **get_all_imagex_templates**: 获取指定服务下的所有图片模板。
- **get_imagex_storage_files**: 获取存储中的文件列表。
- **get_image_url_by_store_uri**: 获取指定资源的公共访问链接。

### AI 图像处理工具 (ai_image_process)
这是一个全能型工具，通过指定 `action_type` 来执行不同的 AI 任务。支持的能力包括：
- **cloud_sr**: 图像超分辨率（云端），支持 2-8 倍放大。
- **smart_expansion**: 智能图像拓展 (Outpainting)。
- **aigc_sr**: AIGC 图片超分（大模型细节增强）。
- **translate**: AIGC 图片翻译（支持 30+ 语言）。
- **quality_assessment**: 大模型画质评估。
- **product_creative**: 电商万创 (商品图生成)。
- **remove_text**: 电商牛皮鲜擦除。
- **ocr**: 文字识别 OCR。
- **remove_bg**: 智能背景移除 (抠图)。
- **seedream**: ImageX-SeeDream 生图方案。

## 动态配置与环境变量

除了传统的环境变量配置，本服务器还支持通过 HTTP Header 动态指定配置（仅限 SSE 和 Streamable HTTP 模式），这在多租户或代理场景下非常有用。

### 环境变量

您可以通过以下环境变量配置 MCP 服务器：

| 环境变量 | 描述 | 是否必需 |
| :--- | :--- | :--- |
| `VOLCENGINE_ACCESS_KEY` | 火山引擎账号 ACCESS KEY | 是 |
| `VOLCENGINE_SECRET_KEY` | 火山引擎账号 SECRET KEY | 是 |
| `VOLCENGINE_SESSION_TOKEN` | 临时安全令牌 (STS Token) | 否 |
| `SERVICE_ID` | 默认 veImageX 服务 ID | 建议配置 |
| `DOMAIN_NAME` | 默认 veImageX 域名 | 建议配置 |
| `CREATIVE_FLOW_ID` | 默认电商万创创意流 ID | 可选 |
| `MCP_TOOL_GROUPS` | 工具分组配置，支持二级分组加载 | 默认 `default,aiprocess` |

### 通过 HTTP Header 动态配置 (推荐)

在 SSE 或 Streamable HTTP 模式下，您可以通过在请求中添加以下 Header 来覆盖环境变量，实现动态身份切换：

| Header | 对应配置 |
| :--- | :--- |
| `x-tt-access-key` | 火山引擎 ACCESS KEY |
| `x-tt-secret-key` | 火山引擎 SECRET KEY |
| `x-tt-session-token` | 临时安全令牌 (STS Token) |
| `x-tt-service-id` | veImageX 服务 ID |
| `x-tt-domain` | veImageX 域名 |
| `x-tt-region` | 区域 (如 cn-north-1) |

**配置优先级：** HTTP Header > 启动参数 > 环境变量。

### API Gateway / 托管模式配置 (入站鉴权)

如果您是通过 API Gateway 或云端托管方式访问 MCP 服务（如方舟、Trae 等平台），通常需要配置入站鉴权（Authorization）以及动态业务凭证。

**配置示例：**

```json
{ 
   "mcpServers": { 
     "veimagex_cloud": { 
       "url": "https://your-gateway-url.com/mcp", 
       "headers": { 
         "Authorization": "Bearer YOUR_GATEWAY_TOKEN",
         "x-tt-access-key": "YOUR_VOLC_AK", 
         "x-tt-secret-key": "YOUR_VOLC_SK",
         "x-tt-service-id": "YOUR_SERVICE_ID",
         "x-tt-domain": "YOUR_DOMAIN_NAME"
       } 
     } 
   } 
}
```

### 二级分组加载说明
为了减轻客户端上下文压力，可以通过 `MCP_TOOL_GROUPS` 指定仅加载特定的 AI 能力：
- `aiprocess`: 加载全部 AI 能力。
- `aiprocess.ocr,aiprocess.translate`: 仅加载 OCR 和翻译能力。

## 安装部署

### 系统依赖
- Python 3.11 或更高版本。
- [uv](https://astral.sh/uv/)。

### 本地运行

**使用 uvx (推荐)**
如果您已安装 [uv](https://astral.sh/uv/)，可以直接运行：
```bash
# 启动标准输入输出模式 (Default)
uvx mcp-server-veimagex
# 启动 SSE 模式 (HTTP URL 访问)
uvx mcp-server-veimagex --transport sse --port 8000
# 启动 Streamable HTTP 模式
uvx mcp-server-veimagex --transport streamable-http --port 8000
```

**使用 uv 运行源码**
```bash
uv sync
# 启动标准输入输出模式 (Default)
uv run mcp-server-veimagex
# 启动 SSE 模式
uv run mcp-server-veimagex --transport sse --port 8000
# 启动 Streamable HTTP 模式
uv run mcp-server-veimagex --transport streamable-http --port 8000
```

## 客户端配置 (示例)

### Trae / Cursor / Claude Desktop
添加以下配置到您的 MCP settings 文件中：

**使用 uvx (推荐)**
```json
{
  "mcpServers": {
    "veimagex": {
      "command": "uvx",
      "args": ["mcp-server-veimagex"],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "您的火山引擎 AK",
        "VOLCENGINE_SECRET_KEY": "您的火山引擎 SK",
        "SERVICE_ID": "您的默认 Service ID",
        "DOMAIN_NAME": "您的默认域名",
        "CREATIVE_FLOW_ID": "您的默认创意流 ID",
        "MCP_TOOL_GROUPS": "default,aiprocess"
      }
    }
  }
}
```

**使用 Python 直接运行**

## 可适配平台
方舟，Trae，cursor

## 服务开通
<https://console.volcengine.cn/imagex>

## License
MIT
