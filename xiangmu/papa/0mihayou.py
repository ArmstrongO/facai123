import urllib.request
import re
import time
import requests
from bs4 import BeautifulSoup


url = 'https://www.miyoushe.com/ys/article/37391667'
try:
    data = urllib.request.urlopen ( url ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
    r = requests.get ( url )
    soup = BeautifulSoup ( r.text, 'html.parser' )
    title = soup.select_one ('html body div#__nuxt div#__layout div.root.mhy-theme-ys div.root-page-container div.mhy-layout.mhy-main-page.mhy-article-page div.mhy-layout__main div.mhy-article-page__main.mhy-container div.mhy-article-page__header div.mhy-article-page__title h1' )
    # result = soup.select_one ('html body div#app div.container div.page-wrap div.main div.info div.info-head div.title h1' ).text
    print(title)

    # 在这里写匹配元素的代码
    # 如果在匹配的过程中出现异常，程序会跳转到except语句块中
except Exception as e:
    print("匹配元素时出现异常:", e)
    pass
# 其他的代码



def cc_mihayou():
    url = f"https://www.miyoushe.com/ys/home/49"  # 要爬取的url
    time.sleep ( 1 )
    tiqu_lianjie = 'https://upload-bbs.miyoushe.com/upload/2023/03/29/355224425/'  # 目标地址前缀
    pat = f'{tiqu_lianjie}(.*?)jpg'  # 正则匹配以PNG结尾的地址
    data = urllib.request.urlopen ( url ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
    relut = re.compile ( pat ).findall ( data )  # 会返回一个列表
    file = open ( r"C:\Users\Administrator\Desktop\1\mimi.txt", "a", encoding="utf-8" )  # 这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
    for i in relut:
        file.write ( f'{tiqu_lianjie}' )  # 先写进开头
        print ( i )
        file.write ( i )  # 将提取的内容写入文件
        file.write ( "jpg" )  # 将格式写入
        file.write ( "\n" )  # 表示换行
    print ( "end" )