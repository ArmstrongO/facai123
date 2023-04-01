# import requests
# from bs4 import BeautifulSoup
#
# # 要抓取链接的网站
# url = "http://tfapi.top/API/nypic.php"
#
# # 要保存链接的文件名
# filename = r"C:\Users\Administrator\Desktop\1\ppurl2.txt"
#
# # 发送HTTP请求并获取响应
# response = requests.get(url)
#
# # 获取所有的跳转URL
# redirect_urls = []
# for url in response.history:
#     redirect_urls.append(url.url)
# redirect_urls.append(response.url)
#
# # 将所有跳转URL保存到文件
# with open(filename, "w") as f:
#     for url in redirect_urls:
#         f.write(url + "\n")
import time

from bs4 import BeautifulSoup
import requests


def yiyan():
    # 要抓取链接的网站
    url = "https://cdn.seovx.com/d/?mom=302"
    # 要保存链接的文件名
    filename = r"C:\Users\Administrator\Desktop\1\erci.txt"
    # 发送HTTP请求并获取响应
    # time.sleep(1)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B08C390B",
        "Referer": url
    }
    response = requests.get(url, headers=headers)
    redirect_urls = []
    for url in response.history:
        if url.url.endswith(".jpg"):
            redirect_urls.append(url.url)
    if response.url.endswith(".jpg"):
        redirect_urls.append(response.url)

    # 将所有以".jpg"结尾的URL保存到文件
    with open(filename, "a") as f:
        for url in redirect_urls:
            f.write(url + "\n")
for n in range ( 1, 599 ):
    yiyan ()



