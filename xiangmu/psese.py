# 双层网站爬v1.0-1


import time
import urllib.request
import re

import requests

# url = "http://tfapi.top/API/nypic.php"  #获取url
# http://www.886hh.buzz/AAtupian/AAAtb/meitui/



def cc():
    url = f"https://gitcode.net/weixin_38503250/index/-/tree/master/bai"  # 获取url
    time.sleep(1)
    tiqu_lianjie='https://wo-ai-tutu.com/weimei/20201108/'
    pat = f'{tiqu_lianjie}(.*?)PNG'
    # pat = 'https://gw3.alicdn.com/tfscom/tuitui/O1CN011EQxtrlijjxqoLq_!!0-rate.jpg'  #匹配规则
    data = urllib.request.urlopen(url).read().decode("utf-8") #读取网页的内容并解码
    relut = re.compile(pat).findall(data)       #会返回一个列表
    file = open(r"C:\Users\Administrator\Desktop\1\sese.txt", "a", encoding="utf-8")  #这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
    for i in relut:
        file.write(f'{tiqu_lianjie}')  #先写进开头
        file.write(i)        #将提取的内容写入文件
        file.write("jpg")    # 将格式写入
        file.write("\n")    #表示换行
    print ( "end" )

def cc_c():
    urll = f"http://www.f32d.buzz/AAtupian/AAAtb/cartoon/"  # 获取url
    time.sleep(1)
    tiqu_lianjiee='/AAtupian/AAAwz/'
    patt = f'{tiqu_lianjiee}(.*?)jpg'
    dataa = urllib.request.urlopen(urll).read().decode("utf-8") #读取网页的内容并解码
    relutt = re.compile(patt).findall(dataa)       #会返回一个列表
    for ii in relutt:
        url = f"http://www.f32d.buzz{tiqu_lianjiee}{ii}html"
        print(url)
        time.sleep(1)
        tiqu_lianjie='https://wo-ai-tutu.com/'
        pat = f'{tiqu_lianjie}(.*?)jpg'
        data = urllib.request.urlopen(url).read().decode("utf-8") #读取网页的内容并解码
        relut = re.compile(pat).findall(data)       #会返回一个列表
        file = open(r"C:\Users\Administrator\Desktop\1\sese5.txt", "a", encoding="utf-8")  #这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
        time.sleep ( 1 )
        for i in relut:
            file.write(f'{tiqu_lianjie}')  #先写进开头
            file.write(i)        #将提取的内容写入文件
            file.write("jpg")    # 将格式写入
            file.write("\n")    #表示换行
    print ( "end" )

# cc()
# for n in range ( 1, 30 ):
#     time.sleep ( 1 )
#     y+=1
#     cc()
#     print ( "end2" )


# patt = '(.*?)jpg'
# string = 'test1.jpg abcd test2.jpg efgh test3.jpg ijkl'
#
# matches = re.findall(patt, string)
# for match in matches:
#     cc()
# http://www.886hh.buzz/AAtupian/AAAwz/118581.html
# https://wo-ai-tutu.com/shunv/20170818/621/1153.jpg
# https://wo-ai-tutu.com/shunv/20170818/656/944.jpg
# https://wo-ai-tutu.com//meitui/20201108/771/156662.jpg
    # https: // wo - ai - tutu.com / shunv / 20170818 / 621 / 1154.jpg

def get_default_address():
    res = requests.get ( url=f"http://tfapi.top/API/nypic.php")
    print ( res )
