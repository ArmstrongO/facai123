import requests
import re
from bs4 import BeautifulSoup

def save(title, content):
    # 使用 with 语句自动关闭文件
    with open('1.txt', mode='a', encoding='utf-8') as f:
        # 写入标题和内容，并加上换行
        f.write(title + "\n")
        f.write(content + "\n")

def get_content(url):
    # 获取网页并解析
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    # 使用 find 函数代替 select 函数
    title = soup.find('h1').text
    content = soup.find(id='content').text
    # 将内容中的空格、制表符和换行符替换为空字符串
    content = re.sub('\s+', '', content)
    return title, content

def get_title_url(text):
    # 优化正则表达式，使用 \d+ 替换 .*?
    title_list = re.findall('/168\d+.html', text)
    # 使用列表推导式，将 https://www.31xiaoshuo.com/ 和 title_list 中的元素拼接
    return ['https://www.31xiaoshuo.com/' + i for i in title_list]

url = 'https://www.31xiaoshuo.com'
html = requests.get(url)
title_url_list = get_title_url(html.text)
# 遍历所有标题链接，并获取并保存内容
for title_url in title_url_list:
    title, content = get_content(title_url)
    print(save(title, content))
