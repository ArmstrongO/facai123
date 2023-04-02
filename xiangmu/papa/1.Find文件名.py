import os
import shutil

folder_path = r'C:\Users\Administrator\Desktop\index\hei'  # 文件夹路径
file_names = os.listdir(folder_path)  # 获取文件夹内的所有文件名

with open(r'C:\Users\Administrator\Desktop\1\hei.txt', 'w') as f:  # 打开或创建 .txt 文件
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)  # 获取文件路径
        if os.path.isfile(file_path):  # 判断是否是文件
            f.write ( 'https://gitcode.net/weixin_38503250/index/-/raw/master/hei/' )
            f.write(file_name + '\n')  # 写入文件名到 1.txt 中



import requests
import threading
def yiyan1():
    url = "https://v1.hitokoto.cn/"
    params = {
        "c": "f",
        "encode": "text"
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()  # 抛出异常
    except requests.exceptions.RequestException as e:
        print("网络连接出现问题: yiyan1", e)
        return None
    else:
        print("OK")
        return res.text

t1=threading.Thread(target=yiyan1)
t1.start()