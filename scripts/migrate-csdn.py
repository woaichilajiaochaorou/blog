#!/usr/bin/env python3
"""
CSDN 博客迁移脚本
将 CSDN 博客文章批量导出为 VitePress 兼容的 Markdown 文件
"""

import os
import re
import json
import time
import ssl
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import html2text
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CSDN_USERNAME = "weixin_46050018"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "posts", "csdn")
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", ".vitepress", "config.ts")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": f"https://blog.csdn.net/{CSDN_USERNAME}",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

LIST_API = "https://blog.csdn.net/community/home-api/v1/get-business-list"

MAX_RETRIES = 3


def create_session():
    """创建带重试和 SSL 容错的请求 session"""
    session = requests.Session()
    retry = Retry(total=MAX_RETRIES, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(HEADERS)
    session.verify = False  # 跳过 SSL 验证
    return session


SESSION = create_session()


def slugify(title):
    """将中文标题转为 URL 友好的文件名"""
    slug = re.sub(r'[^\w\u4e00-\u9fff-]', '-', title)
    slug = re.sub(r'-+', '-', slug).strip('-').lower()
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    return slug


def fetch_article_list():
    """获取所有文章列表"""
    articles = []
    page = 1
    while True:
        params = {
            "page": page,
            "size": 20,
            "businessType": "blog",
            "orderby": "",
            "no498": "false",
            "username": CSDN_USERNAME,
        }
        print(f"  获取文章列表第 {page} 页...")
        try:
            resp = SESSION.get(LIST_API, params=params, timeout=30)
            data = resp.json()
        except Exception as e:
            print(f"  请求失败: {e}，重试中...")
            time.sleep(3)
            try:
                resp = SESSION.get(LIST_API, params=params, timeout=30)
                data = resp.json()
            except Exception as e2:
                print(f"  重试仍然失败: {e2}")
                break

        if data.get("code") != 200:
            print(f"  API 返回错误: {data.get('message', 'unknown')}")
            break

        blog_list = data.get("data", {}).get("list", [])
        if not blog_list:
            break

        for item in blog_list:
            articles.append({
                "title": item.get("title", "").strip(),
                "url": item.get("url", ""),
                "date": item.get("postTime", item.get("createTime", ""))[:10],
                "description": item.get("description", ""),
                "views": item.get("viewCount", 0),
                "likes": item.get("diggCount", 0),
            })

        page += 1
        time.sleep(1)

    return articles


def fetch_article_content(url):
    """获取单篇文章的 HTML 内容，带重试"""
    for attempt in range(MAX_RETRIES):
        try:
            resp = SESSION.get(url, timeout=30)
            resp.encoding = 'utf-8'
            soup = BeautifulSoup(resp.text, 'html.parser')

            content_div = soup.find('div', id='content_views')
            if not content_div:
                content_div = soup.find('article')
            if not content_div:
                return None

            # 移除 CSDN 的广告和无关元素
            for tag in content_div.find_all(['script', 'style', 'iframe']):
                tag.decompose()
            for tag in content_div.find_all('div', class_=re.compile(r'(hide-article|recommend|toolbar|comment)')):
                tag.decompose()

            return str(content_div)
        except Exception as e:
            wait = (attempt + 1) * 3
            print(f"    第 {attempt+1} 次请求失败: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"    等待 {wait}s 后重试...")
                time.sleep(wait)
            else:
                print(f"    已达最大重试次数，跳过")
                return None


def html_to_markdown(html_content):
    """将 HTML 转为 Markdown"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # 不自动换行
    h.unicode_snob = True
    h.skip_internal_links = False
    h.inline_links = True
    h.protect_links = True
    h.ignore_tables = False

    md = h.handle(html_content)

    # 清理多余空行
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def save_article(article, markdown_content):
    """保存文章为 VitePress 格式的 Markdown"""
    slug = slugify(article['title'])
    if not slug:
        slug = f"article-{article['date']}"

    filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")

    # 文件名去重
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(OUTPUT_DIR, f"{slug}-{counter}.md")
        counter += 1

    safe_title = article['title'].replace('"', "'")
    safe_desc = article.get('description', '')[:200].replace('"', "'")
    frontmatter = f"""---
title: "{safe_title}"
date: {article['date']}
description: "{safe_desc}"
tags:
  - CSDN迁移
---
"""
    content = f"{frontmatter}\n# {article['title']}\n\n{markdown_content}\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def generate_sidebar_items(articles_saved):
    """生成侧栏配置片段"""
    items = []
    for art in articles_saved:
        slug = os.path.splitext(os.path.basename(art['path']))[0]
        items.append(f"            {{ text: '{art['title'][:50]}', link: '/posts/csdn/{slug}' }},")
    return "\n".join(items)


def main():
    print(f"=== CSDN 博客迁移工具 ===")
    print(f"用户: {CSDN_USERNAME}")
    print()

    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 获取文章列表
    print("[1/3] 获取文章列表...")
    articles = fetch_article_list()
    print(f"  共找到 {len(articles)} 篇文章\n")

    if not articles:
        print("没有找到文章，退出")
        return

    # 逐篇抓取并转换
    print("[2/3] 抓取文章内容并转换...")
    saved = []
    failed = []

    for i, article in enumerate(articles):
        print(f"  [{i+1}/{len(articles)}] {article['title'][:50]}...")

        html_content = fetch_article_content(article['url'])
        if not html_content:
            print(f"    ✗ 跳过（无法获取内容）")
            failed.append(article['title'])
            time.sleep(1)
            continue

        markdown = html_to_markdown(html_content)
        filepath = save_article(article, markdown)

        saved.append({
            'title': article['title'],
            'date': article['date'],
            'path': filepath,
        })
        print(f"    ✓ 已保存")
        time.sleep(1.5)  # 避免请求过快被封

    # 生成侧栏配置
    print(f"\n[3/3] 生成配置...")
    sidebar_snippet = generate_sidebar_items(saved)

    snippet_path = os.path.join(OUTPUT_DIR, "_sidebar_config.txt")
    with open(snippet_path, 'w', encoding='utf-8') as f:
        f.write("// 将以下内容添加到 config.ts 的 sidebar '/posts/' items 数组中:\n")
        f.write("{\n")
        f.write("  text: 'CSDN 迁移文章',\n")
        f.write("  collapsed: true,\n")
        f.write("  items: [\n")
        f.write(sidebar_snippet)
        f.write("\n  ],\n")
        f.write("},\n")

    print(f"\n=== 迁移完成 ===")
    print(f"  成功: {len(saved)} 篇")
    print(f"  失败: {len(failed)} 篇")
    if failed:
        print(f"  失败列表:")
        for t in failed:
            print(f"    - {t}")
    print(f"\n  文章保存在: {os.path.abspath(OUTPUT_DIR)}")
    print(f"  侧栏配置片段: {os.path.abspath(snippet_path)}")
    print(f"\n  下一步:")
    print(f"  1. 查看 {snippet_path} 中的配置")
    print(f"  2. 将配置粘贴到 docs/.vitepress/config.ts 的 sidebar 中")
    print(f"  3. git add . && git commit -m 'migrate: csdn articles' && git push")


if __name__ == "__main__":
    main()
