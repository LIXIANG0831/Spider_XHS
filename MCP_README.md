# 小红书API MCP服务器

基于小红书PC端API的MCP（Model Context Protocol）封装，将API接口暴露为MCP工具，方便与各种AI客户端集成。

## 功能特性

- **首页接口**：获取主页所有频道、推荐笔记
- **用户接口**：获取用户信息、笔记、点赞、收藏
- **笔记接口**：获取笔记详情、无水印视频/图片
- **搜索接口**：搜索笔记和用户
- **评论接口**：获取笔记评论
- **消息接口**：获取未读消息、点赞、关注等通知

## 环境要求

- Python 3.7+
- fastmcp
- MCP兼容的AI客户端

## 安装依赖

```bash
pip install fastmcp
```

## 配置cookies

在使用任何工具之前，需要先设置cookies。可以通过以下方式：

### 方法1：环境变量设置（推荐）

```bash
export XHS_COOKIES="你的cookies字符串"
```

### 方法2：通过其他方式设置后，工具会自动从环境变量读取
```bash
{
  "mcpServers": {
    "xhs-api": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "<YOUR PROJECT PATH>",
      "env": {
        "XHS_COOKIES": "<YOUR XHS_COOKIES>"
      },
      "disabled": false,
      "allowedEnv": ["*"]
    }
  }
}
```
## 启动MCP服务器

```bash
python mcp_server.py
```

服务器将使用标准输入输出（stdio）启动，等待MCP客户端连接。

## MCP工具列表

### 首页相关工具

#### get_homefeed_category

获取主页的所有频道

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

**返回值：**
```json
{
  "success": true,
  "message": "操作描述",
  "data": {
    // 频道数据
  }
}
```

#### get_homefeed_recommend

获取主页推荐的笔记

**参数：**
- `category` (string, 可选): 频道，默认""
- `cursor_score` (string, 可选): cursor，默认""
- `refresh_type` (integer, 可选): 刷新类型，默认1
- `note_index` (integer, 可选): 笔记索引，默认0
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_homefeed_recommend_by_num

根据数量获取主页推荐的笔记

**参数：**
- `category` (string, 可选): 频道，默认""
- `num` (integer, 可选): 获取数量，默认10
- `proxies` (string, 可选): 代理服务器，JSON格式

### 用户相关工具

#### get_user_info

获取用户的信息

**参数：**
- `user_id` (string, 必需): 用户ID
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_self_info

获取用户自己的信息

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_self_info2

获取用户自己的信息2

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_notes

获取用户指定位置的笔记

**参数：**
- `user_id` (string, 必需): 用户ID
- `cursor` (string, 可选): cursor，默认""
- `xsec_token` (string, 可选): xsec_token，默认""
- `xsec_source` (string, 可选): xsec_source，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_all_notes

获取用户所有笔记

**参数：**
- `user_url` (string, 必需): 用户主页URL
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_likes

获取用户指定位置喜欢的笔记

**参数：**
- `user_id` (string, 必需): 用户ID
- `cursor` (string, 可选): cursor，默认""
- `xsec_token` (string, 可选): xsec_token，默认""
- `xsec_source` (string, 可选): xsec_source，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_all_likes

获取用户所有喜欢笔记

**参数：**
- `user_url` (string, 必需): 用户主页URL
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_collects

获取用户指定位置收藏的笔记

**参数：**
- `user_id` (string, 必需): 用户ID
- `cursor` (string, 可选): cursor，默认""
- `xsec_token` (string, 可选): xsec_token，默认""
- `xsec_source` (string, 可选): xsec_source，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_user_all_collects

获取用户所有收藏笔记

**参数：**
- `user_url` (string, 必需): 用户主页URL
- `proxies` (string, 可选): 代理服务器，JSON格式

### 笔记相关工具

#### get_note_info

获取笔记的详细信息

**参数：**
- `url` (string, 必需): 笔记URL
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_note_no_watermark_video

获取笔记无水印视频

**参数：**
- `note_id` (string, 必需): 笔记ID

#### get_note_no_watermark_image

获取笔记无水印图片

**参数：**
- `img_url` (string, 必需): 图片URL

### 搜索相关工具

#### get_search_keyword

获取搜索关键词推荐

**参数：**
- `word` (string, 必需): 关键词
- `proxies` (string, 可选): 代理服务器，JSON格式

#### search_notes

搜索笔记

**参数：**
- `query` (string, 必需): 搜索关键词
- `page` (integer, 可选): 页码，默认1
- `sort_type` (integer, 可选): 排序方式，默认0
  - 0: 综合排序
  - 1: 最新
  - 2: 最多点赞
  - 3: 最多评论
  - 4: 最多收藏
- `note_type` (integer, 可选): 笔记类型，默认0
  - 0: 不限
  - 1: 视频笔记
  - 2: 普通笔记
- `note_time` (integer, 可选): 笔记时间，默认0
  - 0: 不限
  - 1: 一天内
  - 2: 一周内
  - 3: 半年内
- `note_range` (integer, 可选): 笔记范围，默认0
  - 0: 不限
  - 1: 已看过
  - 2: 未看过
  - 3: 已关注
- `pos_distance` (integer, 可选): 位置距离，默认0
  - 0: 不限
  - 1: 同城
  - 2: 附近
- `geo` (string, 可选): 定位信息，JSON格式，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### search_some_notes

指定数量搜索笔记

**参数：**
- `query` (string, 必需): 搜索关键词
- `num` (integer, 可选): 获取数量，默认10
- `sort_type` (integer, 可选): 排序方式，默认0
- `note_type` (integer, 可选): 笔记类型，默认0
- `note_time` (integer, 可选): 笔记时间，默认0
- `note_range` (integer, 可选): 笔记范围，默认0
- `pos_distance` (integer, 可选): 位置距离，默认0
- `geo` (string, 可选): 定位信息，JSON格式，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### search_users

搜索用户

**参数：**
- `query` (string, 必需): 搜索关键词
- `page` (integer, 可选): 页码，默认1
- `proxies` (string, 可选): 代理服务器，JSON格式

#### search_some_users

指定数量搜索用户

**参数：**
- `query` (string, 必需): 搜索关键词
- `num` (integer, 可选): 获取数量，默认10
- `proxies` (string, 可选): 代理服务器，JSON格式

### 评论相关工具

#### get_note_comments

获取指定位置的笔记一级评论

**参数：**
- `note_id` (string, 必需): 笔记ID
- `cursor` (string, 可选): cursor，默认""
- `xsec_token` (string, 可选): xsec_token，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_note_all_comments

获取笔记的全部一级评论

**参数：**
- `note_id` (string, 必需): 笔记ID
- `xsec_token` (string, 可选): xsec_token，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_note_sub_comments

获取指定位置的笔记二级评论

**参数：**
- `comment` (object, 必需): 一级评论信息（dict类型）
- `cursor` (string, 可选): cursor，默认""
- `xsec_token` (string, 可选): xsec_token，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_note_all_sub_comments

获取笔记的全部二级评论

**参数：**
- `comment` (object, 必需): 一级评论信息（dict类型）
- `xsec_token` (string, 可选): xsec_token，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_note_all_comment

获取一篇文章的所有评论（一级和二级）

**参数：**
- `url` (string, 必需): 笔记URL
- `proxies` (string, 可选): 代理服务器，JSON格式

### 消息相关工具

#### get_unread_message

获取未读消息

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_mentions

获取评论和@提醒

**参数：**
- `cursor` (string, 可选): cursor，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_all_mentions

获取全部的评论和@提醒

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_likes

获取赞和收藏

**参数：**
- `cursor` (string, 可选): cursor，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_all_likes

获取全部的赞和收藏

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_connections

获取新增关注

**参数：**
- `cursor` (string, 可选): cursor，默认""
- `proxies` (string, 可选): 代理服务器，JSON格式

#### get_all_connections

获取全部的新增关注

**参数：**
- `proxies` (string, 可选): 代理服务器，JSON格式

## 使用说明

### 工具调用方式

所有工具都从环境变量 `XHS_COOKIES` 自动获取cookies，无需在每次调用时手动传入。

### 工具返回格式

所有工具都返回统一的JSON格式：

```json
{
  "success": true,
  "message": "操作描述",
  "data": {
    // 具体数据
  }
}
```

- `success`: 是否成功（布尔值）
- `message`: 消息描述（字符串）
- `data`: 返回数据（对象或数组，失败时为null）

### 使用示例

#### 1. 设置cookies（通过环境变量）

```bash
export XHS_COOKIES="你的cookies字符串"
python mcp_server.py
```

#### 2. 在MCP客户端中使用工具

以Claude Desktop为例，在mcp_config.json中配置：

```json
{
  "mcpServers": {
    "xhs-api": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {
        "XHS_COOKIES": "你的cookies字符串"
      }
    }
  }
}
```

然后在对话中直接调用工具：

```
请帮我获取用户信息，用户ID是123456
```

MCP客户端会自动调用 `get_user_info` 工具。

## 代理配置

所有工具都支持可选的`proxies`参数，用于配置HTTP代理。格式为JSON字符串：

```json
{
  "http": "http://proxy.example.com:8080",
  "https": "https://proxy.example.com:8080"
}
```

## 错误处理

- 如果未设置cookies环境变量，所有需要认证的工具将抛出异常："未设置cookies，请先调用 /api/set_cookies 接口设置"
- 所有工具都包含完整的错误处理，会在返回的JSON中包含具体的错误信息
- 错误时 `success` 为 `false`，`data` 为 `null`

## 注意事项

1. **cookies安全**：请确保cookies字符串的安全性，不要在不安全的环境中暴露
2. **环境变量**：所有工具都使用环境变量 `XHS_COOKIES` 获取cookies，请确保已正确设置
3. **代理配置**：代理参数需要是有效的JSON格式字符串
4. **xsec_token**：某些评论相关接口需要提供xsec_token，这个值通常从之前的响应中获取

## 许可证

MIT