# encoding: utf-8
"""
MCP服务器 - 将FastAPI接口暴露为MCP工具
"""
import json
import os
from typing import Any, Dict, Optional
from fastmcp import FastMCP
from apis.xhs_pc_apis import XHS_Apis

# 创建MCP服务器实例
mcp = FastMCP("小红书API MCP服务器")

# 创建API实例
xhs_api = XHS_Apis()


def get_cookies_from_env() -> str:
    """
    从环境变量获取cookies
    """
    cookies = os.environ.get('XHS_COOKIES', '')
    if not cookies:
        raise ValueError("未设置cookies，请先调用 /api/set_cookies 接口设置")
    return cookies


@mcp.tool()
def get_homefeed_category(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取主页的所有频道

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_homefeed_all_channel(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_homefeed_recommend(
    category: str = "",
    cursor_score: str = "",
    refresh_type: int = 1,
    note_index: int = 0,
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    获取主页推荐的笔记

    Args:
        category: 频道
        cursor_score: cursor
        refresh_type: 刷新类型
        note_index: 笔记索引
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_homefeed_recommend(
            category, cursor_score, refresh_type, note_index, cookies, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_homefeed_recommend_by_num(category: str = "", num: int = 10, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    根据数量获取主页推荐的笔记

    Args:
        category: 频道
        num: 获取数量
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_homefeed_recommend_by_num(
            category, num, cookies, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_info(user_id: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取用户的信息

    Args:
        user_id: 用户ID
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_info(user_id, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_self_info(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取用户自己的信息

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_self_info(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_self_info2(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取用户自己的信息2

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_self_info2(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_notes(
    user_id: str,
    cursor: str = "",
    xsec_token: str = "",
    xsec_source: str = "",
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    获取用户指定位置的笔记

    Args:
        user_id: 用户ID
        cursor: cursor
        xsec_token: xsec_token
        xsec_source: xsec_source
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_note_info(
            user_id, cursor, cookies, xsec_token, xsec_source, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_all_notes(user_url: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取用户所有笔记

    Args:
        user_url: 用户主页URL
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_all_notes(user_url, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_likes(
    user_id: str,
    cursor: str = "",
    xsec_token: str = "",
    xsec_source: str = "",
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    获取用户指定位置喜欢的笔记

    Args:
        user_id: 用户ID
        cursor: cursor
        xsec_token: xsec_token
        xsec_source: xsec_source
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_like_note_info(
            user_id, cursor, cookies, xsec_token, xsec_source, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_all_likes(user_url: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取用户所有喜欢笔记

    Args:
        user_url: 用户主页URL
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_all_like_note_info(user_url, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_collects(
    user_id: str,
    cursor: str = "",
    xsec_token: str = "",
    xsec_source: str = "",
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    获取用户指定位置收藏的笔记

    Args:
        user_id: 用户ID
        cursor: cursor
        xsec_token: xsec_token
        xsec_source: xsec_source
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_collect_note_info(
            user_id, cursor, cookies, xsec_token, xsec_source, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_user_all_collects(user_url: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取用户所有收藏笔记

    Args:
        user_url: 用户主页URL
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_all_collect_note_info(user_url, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_note_info(url: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取笔记的详细信息

    Args:
        url: 笔记URL
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_info(url, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_note_no_watermark_video(note_id: str) -> Dict[str, Any]:
    """
    获取笔记无水印视频
    
    Args:
        note_id: 笔记ID
    
    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        success, msg, data = xhs_api.get_note_no_water_video(note_id)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_note_no_watermark_image(img_url: str) -> Dict[str, Any]:
    """
    获取笔记无水印图片
    
    Args:
        img_url: 图片URL
    
    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        success, msg, data = xhs_api.get_note_no_water_img(img_url)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_search_keyword(word: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取搜索关键词推荐

    Args:
        word: 关键词
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_search_keyword(word, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def search_notes(
    query: str,
    page: int = 1,
    sort_type: int = 0,
    note_type: int = 0,
    note_time: int = 0,
    note_range: int = 0,
    pos_distance: int = 0,
    geo: str = "",
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    搜索笔记

    Args:
        query: 搜索关键词
        page: 页码
        sort_type: 排序方式：0-综合排序，1-最新，2-最多点赞，3-最多评论，4-最多收藏
        note_type: 笔记类型：0-不限，1-视频笔记，2-普通笔记
        note_time: 笔记时间：0-不限，1-一天内，2-一周内，3-半年内
        note_range: 笔记范围：0-不限，1-已看过，2-未看过，3-已关注
        pos_distance: 位置距离：0-不限，1-同城，2-附近
        geo: 定位信息，JSON格式
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        geo_dict = json.loads(geo) if geo else ""
        success, msg, data = xhs_api.search_note(
            query, cookies, page, sort_type, note_type, note_time, note_range, pos_distance, geo_dict, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def search_some_notes(
    query: str,
    num: int = 10,
    sort_type: int = 0,
    note_type: int = 0,
    note_time: int = 0,
    note_range: int = 0,
    pos_distance: int = 0,
    geo: str = "",
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    指定数量搜索笔记

    Args:
        query: 搜索关键词
        num: 获取数量
        sort_type: 排序方式：0-综合排序，1-最新，2-最多点赞，3-最多评论，4-最多收藏
        note_type: 笔记类型：0-不限，1-视频笔记，2-普通笔记
        note_time: 笔记时间：0-不限，1-一天内，2-一周内，3-半年内
        note_range: 笔记范围：0-不限，1-已看过，2-未看过，3-已关注
        pos_distance: 位置距离：0-不限，1-同城，2-附近
        geo: 定位信息，JSON格式
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        geo_dict = json.loads(geo) if geo else ""
        success, msg, data = xhs_api.search_some_note(
            query, num, cookies, sort_type, note_type, note_time, note_range, pos_distance, geo_dict, proxies_dict
        )
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def search_users(query: str, page: int = 1, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    搜索用户

    Args:
        query: 搜索关键词
        page: 页码
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.search_user(query, cookies, page, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def search_some_users(query: str, num: int = 10, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    指定数量搜索用户

    Args:
        query: 搜索关键词
        num: 获取数量
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.search_some_user(query, num, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_note_comments(
    note_id: str,
    cursor: str = "",
    xsec_token: str = "",
    proxies: Optional[str] = None
) -> Dict[str, Any]:
    """
    获取指定位置的笔记一级评论

    Args:
        note_id: 笔记ID
        cursor: cursor
        xsec_token: xsec_token
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_out_comment(note_id, cursor, xsec_token, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_note_all_comments(note_id: str, xsec_token: str = "", proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取笔记的全部一级评论

    Args:
        note_id: 笔记ID
        xsec_token: xsec_token
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_all_out_comment(note_id, xsec_token, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}

@mcp.tool()
def get_note_all_comment(url: str, proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取一篇文章的所有评论（一级和二级）

    Args:
        url: 笔记URL
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_all_comment(url, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_unread_message(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取未读消息

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_unread_message(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_mentions(cursor: str = "", proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取评论和@提醒

    Args:
        cursor: cursor
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_metions(cursor, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_all_mentions(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取全部的评论和@提醒

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_all_metions(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_likes(cursor: str = "", proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取赞和收藏

    Args:
        cursor: cursor
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_likesAndcollects(cursor, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_all_likes(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取全部的赞和收藏

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_all_likesAndcollects(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_connections(cursor: str = "", proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取新增关注

    Args:
        cursor: cursor
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_new_connections(cursor, cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


@mcp.tool()
def get_all_connections(proxies: Optional[str] = None) -> Dict[str, Any]:
    """
    获取全部的新增关注

    Args:
        proxies: 代理服务器，JSON格式 (可选)

    Returns:
        包含成功状态、消息和数据的字典
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_all_new_connections(cookies, proxies_dict)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


if __name__ == "__main__":
    # 启动MCP服务器
    mcp.run(transport='stdio')
