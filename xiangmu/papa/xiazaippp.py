import os
import datetime
import time
from urllib import request, error
import requests
def t_time():
    now = datetime.datetime.now()
    now_str = now.strftime("%H.%M.%S")
    return now_str
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)


# 定义要下载的资源信息
owner = "weixin_38503250"  # 修改为仓库所有者的用户名
repo = "water_tu" # 修改为仓库的名称
branch = "main"  # 修改为仓库的分支
file_path = "meitu.txt"  # 修改为要下载的文件路径
file_pp = fr"D:\{file_path}"  # 修改为你要检测的文件路径

if os.path.exists(file_pp):
    os.remove(file_pp)
    pass
else:
    pass

time.sleep(2)
# 定义下载URL
url = f"https://gitcode.net/{owner}/{repo}/-/raw/{branch}/{file_path}?inline=false"

response = requests.get(url)# 发送HTTP请求并获取响应

# 将响应内容保存到本地文件
with open("D:\\" + file_path, 'wb') as f:
    f.write(response.content)

time.sleep(2)
dir_path = fr"D:\{t_time()}"  # 修改为你的文件夹路径
if not os.path.exists(dir_path):
    os.mkdir(dir_path) # 创建文件夹
os.startfile(dir_path)# 打开显示文件夹

#开始读取路径下文件
# read = open(r"D:meitu.txt", "r", encoding="utf-8")
read = open(r"C:\Users\Administrator\Desktop\1\sese8.txt", "r", encoding="utf-8")
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
    # time.sleep(1)
    q += 1

print("爬取完成！")
