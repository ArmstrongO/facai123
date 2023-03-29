import urllib.request
import re
url = "http://www.886hh.buzz/AAtupian/AAAwz/"  #获取url
# http://www.886hh.buzz/AAtupian/AAAtb/meitui/
pat = "http://www.886hh.buzz/AAtupian/AAAwz/(.*?)html"  #获取url
# pat = 'https://wo-ai-tutu.com//meitui/20201108/(.*?)jpg'
# pat = 'https://wo-ai-tutu.com/shunv/20170818/(.*?)jpg'  #匹配规则
data = urllib.request.urlopen(url).read().decode("utf-8") #读取网页的内容并解码
relut = re.compile(pat).findall(data)       #会返回一个列表
file = open(r"C:\Users\Administrator\Desktop\1\url.txt", "w", encoding="utf-8")  #这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
for i in relut:
    file.write("http://www.886hh.buzz/AAtupian/AAAwz/")  #先写进开头
    file.write(i)        #将提取的内容写入文件
    file.write("jpg")    # 将格式写入
    file.write("\n")    #表示换行