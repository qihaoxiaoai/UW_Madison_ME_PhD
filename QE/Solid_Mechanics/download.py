import requests

def download_page_images(start_page, end_page, base_url):
    for page_number in range(start_page, end_page + 1):
        # 构建当前页的URL
        url = f"{base_url}{page_number}-2048.jpg"
        response = requests.get(url)
        # 确保请求成功
        if response.status_code == 200:
            file_path = f"page_{page_number}.jpg"  # 定义保存文件的名称
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded page {page_number}")
        else:
            print(f"Failed to download page {page_number}")

# 使用此函数下载2003页的图片
base_url = "https://image.slidesharecdn.com/beermat7solu-241023015345-c7f5f557/75/BEER-MAT-7-SOLUcionario-de-mecanica-de-materiales-"
start_page = 1
end_page = 2003

download_page_images(start_page, end_page, base_url)

