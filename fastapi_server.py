# encoding: utf-8
from fastapi import FastAPI, HTTPException, Query, Path
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
import uvicorn
import json
import os

from apis.xhs_pc_apis import XHS_Apis

# 创建FastAPI应用实例
app = FastAPI(
    title="小红书API接口",
    description="基于小红书PC端API的FastAPI封装，提供用户信息、笔记搜索、评论获取等功能",
    version="1.0.0"
)

# 创建API实例
xhs_api = XHS_Apis()


def get_cookies_from_env() -> str:
    """
    从参数或环境变量获取cookies
    """
    cookies = os.environ.get('XHS_COOKIES', '')
    if not cookies:
        raise HTTPException(status_code=400, detail="未设置cookies，请先调用 /api/set_cookies 接口设置")
    return cookies


# ============== 首页相关接口 ==============

@app.get("/api/homefeed/category", tags=["首页"])
async def get_homefeed_category(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取主页的所有频道
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_homefeed_all_channel(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/homefeed/recommend", tags=["首页"])
async def get_homefeed_recommend(
        category: str = Query("", description="频道"),
        cursor_score: str = Query("", description="cursor"),
        refresh_type: int = Query(1, description="刷新类型"),
        note_index: int = Query(0, description="笔记索引"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取主页推荐的笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_homefeed_recommend(
            category, cursor_score, refresh_type, note_index, cookies, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/homefeed/recommend/by-num", tags=["首页"])
async def get_homefeed_recommend_by_num(
        category: str = Query("", description="频道"),
        num: int = Query(10, description="获取数量"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    根据数量获取主页推荐的笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_homefeed_recommend_by_num(
            category, num, cookies, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 用户相关接口 ==============

@app.get("/api/user/info/{user_id}", tags=["用户"])
async def get_user_info(
        user_id: str = Path(..., description="用户ID"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户的信息
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_info(user_id, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/self/info", tags=["用户"])
async def get_user_self_info(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户自己的信息
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_self_info(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/self/info2", tags=["用户"])
async def get_user_self_info2(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户自己的信息2
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_self_info2(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/{user_id}/notes", tags=["用户"])
async def get_user_notes(
        user_id: str = Path(..., description="用户ID"),
        cursor: str = Query("", description="cursor"),
        xsec_token: str = Query("", description="xsec_token"),
        xsec_source: str = Query("", description="xsec_source"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户指定位置的笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_note_info(
            user_id, cursor, cookies, xsec_token, xsec_source, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/notes/all", tags=["用户"])
async def get_user_all_notes(
        user_url: str = Query(..., description="用户主页URL"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户所有笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_all_notes(user_url, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/{user_id}/likes", tags=["用户"])
async def get_user_likes(
        user_id: str = Path(..., description="用户ID"),
        cursor: str = Query("", description="cursor"),
        xsec_token: str = Query("", description="xsec_token"),
        xsec_source: str = Query("", description="xsec_source"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户指定位置喜欢的笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_like_note_info(
            user_id, cursor, cookies, xsec_token, xsec_source, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/likes/all", tags=["用户"])
async def get_user_all_likes(
        user_url: str = Query(..., description="用户主页URL"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户所有喜欢笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_all_like_note_info(user_url, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/{user_id}/collects", tags=["用户"])
async def get_user_collects(
        user_id: str = Path(..., description="用户ID"),
        cursor: str = Query("", description="cursor"),
        xsec_token: str = Query("", description="xsec_token"),
        xsec_source: str = Query("", description="xsec_source"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户指定位置收藏的笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_collect_note_info(
            user_id, cursor, cookies, xsec_token, xsec_source, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/user/collects/all", tags=["用户"])
async def get_user_all_collects(
        user_url: str = Query(..., description="用户主页URL"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取用户所有收藏笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_user_all_collect_note_info(user_url, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 笔记相关接口 ==============

@app.get("/api/note/info", tags=["笔记"])
async def get_note_info(
        url: str = Query(..., description="笔记URL"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取笔记的详细信息
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_info(url, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/note/video/no-watermark/{note_id}", tags=["笔记"])
async def get_note_no_watermark_video(
        note_id: str = Path(..., description="笔记ID")
):
    """
    获取笔记无水印视频
    """
    try:
        success, msg, data = xhs_api.get_note_no_water_video(note_id)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/note/image/no-watermark", tags=["笔记"])
async def get_note_no_watermark_image(
        img_url: str = Query(..., description="图片URL")
):
    """
    获取笔记无水印图片
    """
    try:
        success, msg, data = xhs_api.get_note_no_water_img(img_url)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 搜索相关接口 ==============

@app.get("/api/search/keyword", tags=["检索"])
async def get_search_keyword(
        word: str = Query(..., description="关键词"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取搜索关键词推荐
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_search_keyword(word, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/notes", tags=["检索"])
async def search_notes(
        query: str = Query(..., description="搜索关键词"),
        page: int = Query(1, description="页码"),
        sort_type: int = Query(0, description="排序方式：0-综合排序，1-最新，2-最多点赞，3-最多评论，4-最多收藏"),
        note_type: int = Query(0, description="笔记类型：0-不限，1-视频笔记，2-普通笔记"),
        note_time: int = Query(0, description="笔记时间：0-不限，1-一天内，2-一周内，3-半年内"),
        note_range: int = Query(0, description="笔记范围：0-不限，1-已看过，2-未看过，3-已关注"),
        pos_distance: int = Query(0, description="位置距离：0-不限，1-同城，2-附近"),
        geo: Optional[str] = Query(None, description="定位信息，JSON格式"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    搜索笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        geo_dict = json.loads(geo) if geo else ""
        success, msg, data = xhs_api.search_note(
            query, cookies, page, sort_type, note_type, note_time, note_range, pos_distance, geo_dict, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/notes/some", tags=["检索"])
async def search_some_notes(
        query: str = Query(..., description="搜索关键词"),
        num: int = Query(10, description="获取数量"),
        sort_type: int = Query(0, description="排序方式：0-综合排序，1-最新，2-最多点赞，3-最多评论，4-最多收藏"),
        note_type: int = Query(0, description="笔记类型：0-不限，1-视频笔记，2-普通笔记"),
        note_time: int = Query(0, description="笔记时间：0-不限，1-一天内，2-一周内，3-半年内"),
        note_range: int = Query(0, description="笔记范围：0-不限，1-已看过，2-未看过，3-已关注"),
        pos_distance: int = Query(0, description="位置距离：0-不限，1-同城，2-附近"),
        geo: Optional[str] = Query(None, description="定位信息，JSON格式"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    指定数量搜索笔记
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        geo_dict = json.loads(geo) if geo else ""
        success, msg, data = xhs_api.search_some_note(
            query, num, cookies, sort_type, note_type, note_time, note_range, pos_distance, geo_dict, proxies_dict
        )
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/users", tags=["检索"])
async def search_users(
        query: str = Query(..., description="搜索关键词"),
        page: int = Query(1, description="页码"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    搜索用户
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.search_user(query, cookies, page, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search/users/some", tags=["检索"])
async def search_some_users(
        query: str = Query(..., description="搜索关键词"),
        num: int = Query(10, description="获取数量"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    指定数量搜索用户
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.search_some_user(query, num, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 评论相关接口 ==============

@app.get("/api/note/{note_id}/comments", tags=["评论"])
async def get_note_comments(
        note_id: str = Path(..., description="笔记ID"),
        cursor: str = Query("", description="cursor"),
        xsec_token: str = Query(..., description="xsec_token"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取指定位置的笔记一级评论
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_out_comment(note_id, cursor, xsec_token, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/note/{note_id}/comments/all", tags=["评论"])
async def get_note_all_comments(
        note_id: str = Path(..., description="笔记ID"),
        xsec_token: str = Query(..., description="xsec_token"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取笔记的全部一级评论
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_all_out_comment(note_id, xsec_token, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/note/comments/all", tags=["评论"])
async def get_note_all_comment(
        url: str = Query(..., description="笔记URL"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取一篇文章的所有评论（一级和二级）
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_note_all_comment(url, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 消息相关接口 ==============

@app.get("/api/message/unread", tags=["消息"])
async def get_unread_message(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取未读消息
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_unread_message(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/message/mentions", tags=["消息"])
async def get_mentions(
        cursor: str = Query("", description="cursor"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取评论和@提醒
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_metions(cursor, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/message/mentions/all", tags=["消息"])
async def get_all_mentions(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取全部的评论和@提醒
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_all_metions(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/message/likes", tags=["消息"])
async def get_likes(
        cursor: str = Query("", description="cursor"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取赞和收藏
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_likesAndcollects(cursor, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/message/likes/all", tags=["消息"])
async def get_all_likes(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取全部的赞和收藏
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_all_likesAndcollects(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/message/connections", tags=["消息"])
async def get_connections(
        cursor: str = Query("", description="cursor"),
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取新增关注
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_new_connections(cursor, cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/message/connections/all", tags=["消息"])
async def get_all_connections(
        proxies: Optional[str] = Query(None, description="代理服务器，JSON格式")
):
    """
    获取全部的新增关注
    """
    try:
        cookies = get_cookies_from_env()
        proxies_dict = json.loads(proxies) if proxies else None
        success, msg, data = xhs_api.get_all_new_connections(cookies, proxies_dict)
        if not success:
            raise HTTPException(status_code=400, detail=msg)
        return {"success": success, "message": msg, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 设置cookies相关接口 ==============

class CookiesModel(BaseModel):
    cookies: str


@app.post("/api/set_cookies", tags=["Cookies写入"])
async def set_cookies(cookies_data: CookiesModel):
    """
    设置用户cookies到环境变量
    """
    try:
        os.environ['XHS_COOKIES'] = cookies_data.cookies
        return {"success": True, "message": "cookies设置成功", "data": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/get_cookies", tags=["Cookies写入"])
async def get_cookies():
    """
    获取当前环境变量中的cookies状态
    """
    try:
        cookies = os.environ.get('XHS_COOKIES', '')
        return {
            "success": True,
            "message": "获取cookies成功",
            "data": {
                "has_cookies": bool(cookies),
                "cookies_length": len(cookies) if cookies else 0
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============== 健康检查 ==============

@app.get("/")
async def root():
    """
    健康检查接口
    """
    return {
        "name": "小红书API接口",
        "version": "1.0.0",
        "status": "running"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
