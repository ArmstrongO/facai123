# 网址下载v1.0-1

import os
import time
import datetime
from urllib import request, error
import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

def t_time():
    now = datetime.datetime.now()
    now_str = now.strftime("%H.%M.%S")
    return now_str

dir_path = fr"D:\{t_time()}"
if not os.path.exists(dir_path):
    os.mkdir(dir_path) # 创建文件夹
os.startfile(dir_path)# 打开显示文件夹
read = open(r"C:\Users\Administrator\Desktop\1\sese5.txt", "r", encoding="utf-8")
s = read.readlines()
print("正在爬取，请稍后！")
q = 1  # 设置图片名称从1开始
ss = t_time()
os.chdir(dir_path)  # 指定存储路径
for i in s:
    filename = str('ArmstrongO')+str(q) + os.path.splitext(i)[-1]
    filename = filename.strip()  # 删除换行符
    try:
        request.urlretrieve(i, filename=filename)  # i为图片地址，filename是图片的名称
    except error.HTTPError as e:
        print('HTTP Error {0}: {1}'.format(e.code, e.reason))
    time.sleep(1)
    q += 1

print("爬取完成！")