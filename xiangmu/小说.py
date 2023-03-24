import requests
import re
from bs4 import BeautifulSoup

#文件保存函数
def save(title, content):
    with open('1.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write(content)

#获取每一章的文本内容和标题
def get_content(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    title = soup.find('h1').text
    content = soup.find(id="content").text
    return title, content

def get_title_url(text):
    # 优化正则表达式，将 .*? 替换为 \d+
    title_list = re.findall("/168\d+.html", text)
    # 使用列表推导式，将 https://www.31xiaoshuo.com/ 和 title_list 的元素拼接
    return ["https://www.31xiaoshuo.com/" + i for i in title_list]

url = "https://www.31xiaoshuo.com/168/168168/"
html = requests.get(url)
titleurl = get_title_url(html.text)
for i in titleurl:
    title, content = get_content(i)
    save(title, content)
