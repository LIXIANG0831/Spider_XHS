# 小红书API FastAPI服务器

基于小红书PC端API的FastAPI封装，提供用户信息、笔记搜索、评论获取等功能。

## 功能特性

- **首页接口**：获取主页所有频道、推荐笔记
- **用户接口**：获取用户信息、笔记、点赞、收藏
- **笔记接口**：获取笔记详情、无水印视频/图片
- **搜索接口**：搜索笔记和用户
- **评论接口**：获取笔记评论
- **消息接口**：获取未读消息、点赞、关注等通知

## 环境要求

- Python 3.7+
- FastAPI
- Uvicorn

## 安装依赖

```bash
pip install fastapi uvicorn
```

## 配置cookies

在使用任何API之前，需要先设置cookies。可以通过以下方式：

### 方法1：通过接口设置（推荐）

启动服务器后，调用设置接口：

```bash
curl -X POST "http://localhost:8000/api/set_cookies" \
  -H "Content-Type: application/json" \
  -d '{"cookies": "你的cookies字符串"}'
```

### 方法2：通过环境变量

```bash
export XHS_COOKIES="你的cookies字符串"
```

然后启动服务器：

```bash
python fastapi_server.py
```

## 启动服务

```bash
python fastapi_server.py
```

服务将在 `http://localhost:8000` 启动。

访问 `http://localhost:8000/docs` 查看自动生成的API文档。

## API接口文档

### 首页相关接口

#### 获取主页所有频道

```http
GET /api/homefeed/category
```

#### 获取主页推荐笔记

```http
POST /api/homefeed/recommend

Query参数:
- category: 频道（可选，默认""）
- cursor_score: cursor（可选，默认""）
- refresh_type: 刷新类型（可选，默认1）
- note_index: 笔记索引（可选，默认0）
- proxies: 代理服务器，JSON格式（可选）
```

#### 根据数量获取主页推荐笔记

```http
GET /api/homefeed/recommend/by-num

Query参数:
- category: 频道（可选，默认""）
- num: 获取数量（可选，默认10）
- proxies: 代理服务器，JSON格式（可选）
```

### 用户相关接口

#### 获取用户信息

```http
GET /api/user/info/{user_id}

Path参数:
- user_id: 用户ID

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户自己的信息

```http
GET /api/user/self/info

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户自己的信息2

```http
GET /api/user/self/info2

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户指定位置的笔记

```http
GET /api/user/{user_id}/notes

Path参数:
- user_id: 用户ID

Query参数:
- cursor: cursor（可选，默认""）
- xsec_token: xsec_token（可选，默认""）
- xsec_source: xsec_source（可选，默认""）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户所有笔记

```http
GET /api/user/notes/all

Query参数:
- user_url: 用户主页URL（必需）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户指定位置喜欢的笔记

```http
GET /api/user/{user_id}/likes

Path参数:
- user_id: 用户ID

Query参数:
- cursor: cursor（可选，默认""）
- xsec_token: xsec_token（可选，默认""）
- xsec_source: xsec_source（可选，默认""）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户所有喜欢笔记

```http
GET /api/user/likes/all

Query参数:
- user_url: 用户主页URL（必需）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户指定位置收藏的笔记

```http
GET /api/user/{user_id}/collects

Path参数:
- user_id: 用户ID

Query参数:
- cursor: cursor（可选，默认""）
- xsec_token: xsec_token（可选，默认""）
- xsec_source: xsec_source（可选，默认""）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取用户所有收藏笔记

```http
GET /api/user/collects/all

Query参数:
- user_url: 用户主页URL（必需）
- proxies: 代理服务器，JSON格式（可选）
```

### 笔记相关接口

#### 获取笔记详细信息

```http
GET /api/note/info

Query参数:
- url: 笔记URL（必需）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取笔记无水印视频

```http
GET /api/note/video/no-watermark/{note_id}

Path参数:
- note_id: 笔记ID（必需）
```

#### 获取笔记无水印图片

```http
GET /api/note/image/no-watermark

Query参数:
- img_url: 图片URL（必需）
```

### 搜索相关接口

#### 获取搜索关键词推荐

```http
GET /api/search/keyword

Query参数:
- word: 关键词（必需）
- proxies: 代理服务器，JSON格式（可选）
```

#### 搜索笔记

```http
GET /api/search/notes

Query参数:
- query: 搜索关键词（必需）
- page: 页码（可选，默认1）
- sort_type: 排序方式（可选，默认0）
  - 0: 综合排序
  - 1: 最新
  - 2: 最多点赞
  - 3: 最多评论
  - 4: 最多收藏
- note_type: 笔记类型（可选，默认0）
  - 0: 不限
  - 1: 视频笔记
  - 2: 普通笔记
- note_time: 笔记时间（可选，默认0）
  - 0: 不限
  - 1: 一天内
  - 2: 一周内
  - 3: 半年内
- note_range: 笔记范围（可选，默认0）
  - 0: 不限
  - 1: 已看过
  - 2: 未看过
  - 3: 已关注
- pos_distance: 位置距离（可选，默认0）
  - 0: 不限
  - 1: 同城
  - 2: 附近
- geo: 定位信息，JSON格式（可选）
- proxies: 代理服务器，JSON格式（可选）
```

#### 指定数量搜索笔记

```http
GET /api/search/notes/some

Query参数:
- query: 搜索关键词（必需）
- num: 获取数量（可选，默认10）
- sort_type: 排序方式（可选，默认0）
- note_type: 笔记类型（可选，默认0）
- note_time: 笔记时间（可选，默认0）
- note_range: 笔记范围（可选，默认0）
- pos_distance: 位置距离（可选，默认0）
- geo: 定位信息，JSON格式（可选）
- proxies: 代理服务器，JSON格式（可选）
```

#### 搜索用户

```http
GET /api/search/users

Query参数:
- query: 搜索关键词（必需）
- page: 页码（可选，默认1）
- proxies: 代理服务器，JSON格式（可选）
```

#### 指定数量搜索用户

```http
GET /api/search/users/some

Query参数:
- query: 搜索关键词（必需）
- num: 获取数量（可选，默认10）
- proxies: 代理服务器，JSON格式（可选）
```

### 评论相关接口

#### 获取指定位置的笔记一级评论

```http
GET /api/note/{note_id}/comments

Path参数:
- note_id: 笔记ID

Query参数:
- cursor: cursor（可选，默认""）
- xsec_token: xsec_token（必需）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取笔记的全部一级评论

```http
GET /api/note/{note_id}/comments/all

Path参数:
- note_id: 笔记ID

Query参数:
- xsec_token: xsec_token（必需）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取一篇文章的所有评论

```http
GET /api/note/comments/all

Query参数:
- url: 笔记URL（必需）
- proxies: 代理服务器，JSON格式（可选）
```

### 消息相关接口

#### 获取未读消息

```http
GET /api/message/unread

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取评论和@提醒

```http
GET /api/message/mentions

Query参数:
- cursor: cursor（可选，默认""）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取全部的评论和@提醒

```http
GET /api/message/mentions/all

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取赞和收藏

```http
GET /api/message/likes

Query参数:
- cursor: cursor（可选，默认""）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取全部的赞和收藏

```http
GET /api/message/likes/all

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取新增关注

```http
GET /api/message/connections

Query参数:
- cursor: cursor（可选，默认""）
- proxies: 代理服务器，JSON格式（可选）
```

#### 获取全部的新增关注

```http
GET /api/message/connections/all

Query参数:
- proxies: 代理服务器，JSON格式（可选）
```

### Cookies管理接口

#### 设置cookies

```http
POST /api/set_cookies

Body参数:
- cookies: cookies字符串（必需）
```

#### 获取cookies状态

```http
GET /api/get_cookies

返回:
{
  "success": true,
  "message": "获取cookies成功",
  "data": {
    "has_cookies": true,
    "cookies_length": 1234
  }
}
```

### 健康检查

```http
GET /

返回:
{
  "name": "小红书API接口",
  "version": "1.0.0",
  "status": "running"
}
```

## 响应格式

所有API响应都遵循统一格式：

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

## 代理配置

所有接口都支持可选的`proxies`参数，用于配置HTTP代理。格式为JSON字符串：

```json
{
  "http": "http://proxy.example.com:8080",
  "https": "https://proxy.example.com:8080"
}
```

## 错误处理

- 如果未设置cookies，所有需要认证的接口将返回400错误
- 所有接口都包含完整的错误处理，会返回具体的错误信息
- 服务器错误返回500状态码，包含错误详情

## 示例

### 获取用户信息

```bash
curl -X GET "http://localhost:8000/api/user/info/123456" \
  -H "accept: application/json"
```

### 搜索笔记

```bash
curl -X GET "http://localhost:8000/api/search/notes?query=美食&sort_type=1&note_type=0" \
  -H "accept: application/json"
```

## 许可证

MIT