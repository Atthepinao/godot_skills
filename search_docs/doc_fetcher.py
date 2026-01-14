import sys
import urllib.request
import re

# 配置：Godot 文档版本 (4.4 建议用 latest，如果是稳定版可以用 stable)
DOC_VERSION = "latest" 
BASE_URL = f"https://docs.godotengine.org/en/{DOC_VERSION}/classes/"

def clean_html(html_content):
    """简单的 HTML 清洗，提取正文文本"""
    # 提取 <div role="main"> 内容，这是文档核心区
    match = re.search(r'<div role="main"[^>]*>(.*?)</div>\s*<footer>', html_content, re.DOTALL)
    if match:
        content = match.group(1)
    else:
        content = html_content

    # 移除 <script> 和 <style>
    content = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
    # 将 HTML 标签替换为换行或空格
    text = re.sub(r'<li[^>]*>', '\n- ', content) # 列表项换行
    text = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n\n# \1\n', text) # 标题
    text = re.sub(r'<[^>]+>', '', text) # 移除其他标签
    
    # 压缩多余空行
    return re.sub(r'\n{3,}', '\n\n', text).strip()

def fetch_doc(class_name):
    # Godot 文档 URL 格式：class_node2d.html (全小写)
    target_name = class_name.lower()
    if not target_name.startswith("class_"):
        target_name = f"class_{target_name}"
    
    url = f"{BASE_URL}{target_name}.html"
    print(f"Fetching: {url}...")

    try:
        # 伪装 User-Agent 防止被 403 拒绝
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            text = clean_html(html)
            # 截取前 8000 字符防止 token 溢出，通常足够覆盖属性和方法列表
            print(text[:8000]) 
            if len(text) > 8000:
                print("\n... (Content truncated) ...")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Class '{class_name}' not found in Godot docs. Please check the spelling.")
        else:
            print(f"HTTP Error: {e.code}")
    except Exception as e:
        print(f"Error fetching docs: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python doc_fetcher.py <ClassName>")
        sys.exit(1)
    
    class_name = sys.argv[1]
    fetch_doc(class_name)