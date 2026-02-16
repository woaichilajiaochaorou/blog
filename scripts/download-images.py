#!/usr/bin/env python3
"""
下载 CSDN 文章中的远程图片到本地，并更新 Markdown 中的引用路径
"""
import os
import re
import glob
import hashlib
import requests
from urllib.parse import urlparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CSDN_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "posts", "csdn")
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "public", "images", "csdn")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Referer": "https://blog.csdn.net/",
}

session = requests.Session()
retry = requests.adapters.HTTPAdapter(max_retries=3)
session.mount("https://", retry)
session.mount("http://", retry)
session.headers.update(HEADERS)
session.verify = False


def download_image(url):
    """下载图片，返回本地文件名"""
    # 用 URL hash 作为文件名，避免重复下载
    url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
    ext = os.path.splitext(urlparse(url).path)[1] or '.png'
    filename = f"{url_hash}{ext}"
    filepath = os.path.join(IMG_DIR, filename)

    if os.path.exists(filepath):
        return filename

    try:
        resp = session.get(url, timeout=30)
        if resp.status_code == 200 and len(resp.content) > 100:
            with open(filepath, 'wb') as f:
                f.write(resp.content)
            return filename
        else:
            print(f"    下载失败 (status={resp.status_code}): {url[:80]}")
            return None
    except Exception as e:
        print(f"    下载异常: {e}")
        return None


def process_file(filepath):
    """处理单个 Markdown 文件中的图片"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 Markdown 图片和 HTML img 标签中的 URL
    img_pattern = re.compile(
        r'(!\[[^\]]*\]\()(https?://[^)]+\.(png|jpg|jpeg|gif|webp|svg)[^)]*?)(\))'
        r'|'
        r'(src=")(https?://[^"]+\.(png|jpg|jpeg|gif|webp|svg)[^"]*?)(")',
        re.IGNORECASE
    )

    images_found = []
    for m in img_pattern.finditer(content):
        if m.group(2):
            images_found.append(m.group(2))
        elif m.group(6):
            images_found.append(m.group(6))

    if not images_found:
        return 0

    count = 0
    for url in images_found:
        filename = download_image(url)
        if filename:
            local_path = f"/images/csdn/{filename}"
            content = content.replace(url, local_path)
            count += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return count


def main():
    os.makedirs(IMG_DIR, exist_ok=True)

    md_files = glob.glob(os.path.join(CSDN_DIR, "*.md"))
    total_images = 0
    total_files = 0

    print(f"=== 下载 CSDN 文章图片 ===\n")

    for fp in sorted(md_files):
        name = os.path.basename(fp)
        if name.startswith('_'):
            continue

        count = process_file(fp)
        if count > 0:
            print(f"  {name}: {count} 张图片")
            total_images += count
            total_files += 1

    print(f"\n=== 完成 ===")
    print(f"  处理文件: {total_files}")
    print(f"  下载图片: {total_images}")
    print(f"  保存位置: {os.path.abspath(IMG_DIR)}")


if __name__ == "__main__":
    main()
