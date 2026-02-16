#!/usr/bin/env python3
"""
修复 CSDN 迁移文章：
1. 删除 frontmatter 中有问题的 description
2. 转义正文中代码围栏外的 HTML 标签
"""
import os
import re
import glob

CSDN_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "posts", "csdn")


def split_frontmatter(content):
    """按行正确分割 frontmatter"""
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, None, content

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return None, None, content

    fm_lines = lines[1:end_idx]
    body_lines = lines[end_idx + 1:]
    return fm_lines, True, '\n'.join(body_lines)


def fix_frontmatter_lines(fm_lines):
    """清理 frontmatter：删除 description 行"""
    changed = False
    new_lines = []
    for line in fm_lines:
        if line.startswith('description:'):
            changed = True
            continue  # 直接删掉 description
        new_lines.append(line)
    return new_lines, changed


def fix_body(body):
    """转义正文中代码围栏外的 HTML 标签"""
    segments = re.split(r'(```[\s\S]*?```)', body)
    changed = False

    for i, seg in enumerate(segments):
        if seg.startswith('```'):
            continue

        original = seg

        # 转义 #include <xxx.h>（包括已有的 \&lt; 修正）
        seg = re.sub(r'#include\s*(?:\\?&lt;|<)([^>;&]+)(?:\\?&gt;|>)', r'#include `<\1>`', seg)

        # 转义未闭合的 HTML 标签（非安全标签）
        def escape_tag(m):
            tag = m.group(0)
            inner = m.group(1)
            safe_tags = ['br', 'hr', 'img', 'a', 'p', 'div', 'span', 'ul', 'ol', 'li',
                         'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'em', 'strong', 'code',
                         'pre', 'blockquote', 'table', 'tr', 'td', 'th', 'thead', 'tbody']
            tag_name = inner.split()[0].split('/')[0].lower().strip()
            if tag_name in safe_tags:
                return tag
            if inner.startswith('http') or inner.startswith('//'):
                return tag
            return tag.replace('<', '&lt;').replace('>', '&gt;')

        seg = re.sub(r'<(/?\w[^>]*)>', escape_tag, seg)

        # 清理之前修复遗留的 \&lt; \&gt;
        seg = seg.replace('\\&lt;', '&lt;').replace('\\&gt;', '&gt;')

        if seg != original:
            segments[i] = seg
            changed = True

    return ''.join(segments), changed


def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_lines, has_fm, body = split_frontmatter(content)
    if not has_fm:
        return False

    fm_fixed, fm_changed = fix_frontmatter_lines(fm_lines)
    body_fixed, body_changed = fix_body(body)

    if fm_changed or body_changed:
        fm_str = '\n'.join(fm_fixed)
        new_content = '---\n' + fm_str + '\n---\n' + body_fixed
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def main():
    md_files = glob.glob(os.path.join(CSDN_DIR, "*.md"))
    fixed = 0
    for fp in sorted(md_files):
        name = os.path.basename(fp)
        if name.startswith('_'):
            continue
        try:
            if fix_file(fp):
                print(f"  fixed: {name}")
                fixed += 1
        except Exception as e:
            print(f"  error: {name} - {e}")

    print(f"\n共修复 {fixed} 个文件")


if __name__ == "__main__":
    main()
