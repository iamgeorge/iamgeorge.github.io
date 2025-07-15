import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin

# 目标网页
url = 'https://tafisa.ca/en/our-colours?f%5B0%5D=texture%3A864'
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# 获取页面内容
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 创建文件夹保存图片
os.makedirs('tafisa_texture_864', exist_ok=True)

# 匹配图片的正则：只下载颜色样本图
pattern = re.compile(r'/sites/default/files/styles/our_colours.*\.jpg')

# 提取并下载图片
downloaded = 0
for img in soup.find_all('img'):
    src = img.get('src')
    if src and pattern.search(src):
        full_url = urljoin('https://tafisa.ca', src)
        filename = os.path.join('tafisa_texture_864', os.path.basename(src))
        if not os.path.exists(filename):
            img_data = requests.get(full_url, headers=headers).content
            with open(filename, 'wb') as f:
                f.write(img_data)
            downloaded += 1
            print(f'Downloaded: {filename}')

print(f"\n✅ 下载完成，共保存 {downloaded} 张图片到 'tafisa_texture_864' 文件夹。")
