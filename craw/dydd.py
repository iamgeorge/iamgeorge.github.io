import os
import requests
from urllib.parse import urljoin

# 设置基础网址和保存目录
base_url = "https://newyorkdooranddrawer.allmoxy.com/data/catalog/"
output_dir = "downloaded_jpgs"

# 创建保存目录
os.makedirs(output_dir, exist_ok=True)

# 设置尝试的编号范围
start_id = 1
end_id = 2000  # 你可以根据需要扩大范围

for i in range(start_id, end_id + 1):
    filename = f"{i}.jpg"
    file_url = urljoin(base_url, filename)

    try:
        print(f"Trying: {file_url}")
        response = requests.get(file_url, timeout=5)

        # 如果状态码是200并且内容是图片，就保存
        if response.status_code == 200 and 'image' in response.headers['Content-Type']:
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Skipped: {filename} (not found or not an image)")

    except Exception as e:
        print(f"Error fetching {file_url}: {e}")
