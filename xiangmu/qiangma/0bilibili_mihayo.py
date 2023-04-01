import cv2
from pyzbar.pyzbar import decode
import pyzbar.pyzbar as pyzbar
import numpy as np
from PIL import ImageGrab
import time
import tkinter as tk
import threading
import re
import http.client
import json

# 显示框框 启动线程


def my_function():
    import juxing


my_thread = threading.Thread(target=my_function)
my_thread.start()


# 获取坐标
root = tk.Tk()
win_width = 300
win_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (win_width // 2)
y_pos = (screen_height // 2) - (win_height // 2)


# 设置扫描区域左上角的坐标和宽高
left, top, width, height = x_pos, y_pos, win_width, win_height
right = left + width
bottom = top + height


# 创建窗口并设置窗口名称
cv2.namedWindow("QR Code Scanner", cv2.WINDOW_NORMAL)
cv2.resizeWindow("QR Code Scanner", win_width, win_height)


# 抢码开始
def Request(ticket):
    conn = http.client.HTTPSConnection("api-sdk.mihoyo.com")
    payload = json.dumps({
        "app_id": 4,
        "device": "",
        "ticket": ticket
    })
    headers = {}
    conn.request("POST", "/hk4e_cn/combo/panda/qrcode/scan", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    retcode = data["retcode"]
    return retcode


# 确认登陆
def ConfirmRequest(ticket):

    conn = http.client.HTTPSConnection("api-takumi.miyoushe.com")
    payload = ''
    headers = {
        'DS': '',
        'cookie': '',
        'x-rpc-client_type': '2',
        'x-rpc-app_version': '2.46.1',
        'x-rpc-sys_version': '9',
        'x-rpc-channel': '',
        'x-rpc-device_id': '',
        'x-rpc-device_fp': '',
        'x-rpc-device_name': '',
        'x-rpc-device_model': '',
        'Referer': ' https://app.mihoyo.co'
    }
    conn.request("GET", "/auth/api/getGameToken?uid=0000000",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))

    data = json.loads(data.decode("utf-8"))
    token = data["data"]["game_token"]

    conn = http.client.HTTPSConnection("api-sdk.mihoyo.com")
    payload = json.dumps({
        "app_id": 4,
        "device": "",
        "payload": {
            "proto": "Account",
            "raw": f"{{\"uid\":\"0000000\",\"token\":\"{token}\"}}"
        },
        "ticket": ticket
    })
    headers = {
        'DS': '',
        'cookie': '',
        'x-rpc-client_type': '2',
        'x-rpc-app_version': '2.46.1',
        'x-rpc-sys_version': '9',
        'x-rpc-channel': ' xiaomi',
        'x-rpc-device_id': '',
        'x-rpc-device_fp': '',
        'x-rpc-device_name': '',
        'x-rpc-device_model': '',
        'Referer': ' https://app.mihoyo.com',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/hk4e_cn/combo/panda/qrcode/confirm",
                 payload, headers)
    res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))


while True:
    # 截取指定区域的屏幕截图
    screenshot = cv2.cvtColor(
        np.array(ImageGrab.grab(bbox=(left, top, right, bottom))),
        cv2.COLOR_BGR2RGB
    )

    # 将截图转换为灰度图像
    gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # 尝试使用pyzbar库识别二维码
    codes = decode(gray, symbols=[pyzbar.ZBarSymbol.QRCODE])

    # 如果找到了二维码，输出其内容
    if codes:
        print(codes[0].data.decode())
        pattern = r"ticket=([a-f0-9]+)"
        match = re.search(pattern, codes[0].data.decode())
        # 正则请求地址
        if match:
            start_time = time.time()
            # 进入抢码
            retcode = Request(match.group(1))
            end_time = time.time()
            if retcode == 0:
                # 计算代码执行时间
                elapsed_time = end_time - start_time
                #  输出执行时间
                print("抢码成功耗时 %.3f 秒" % elapsed_time)
                # 确认登陆
                ConfirmRequest(match.group(1))
                time.sleep(1)

    # 等待一段时间再继续扫描
    time.sleep(0.05)

    # 在窗口中显示截图
    cv2.imshow("QR Code Scanner", screenshot)

    # 检查是否按下了键盘上的任意键
    if cv2.waitKey(1) != -1:
        break
# 关闭窗口
cv2.destroyAllWindows()

import tkinter as tk

# 创建一个Tkinter窗口
root = tk.Tk ()

# 隐藏窗口标题栏和边框
root.overrideredirect ( True )

# 将窗口置顶
root.wm_attributes ( "-topmost", True )

# 设置窗口大小和位置
win_width = 300
win_height = 300
screen_width = root.winfo_screenwidth ()
screen_height = root.winfo_screenheight ()
x_pos = (screen_width // 2) - (win_width // 2)
y_pos = (screen_height // 2) - (win_height // 2)
root.geometry ( '{}x{}+{}+{}'.format ( win_width, win_height, x_pos, y_pos ) )

# 将窗口背景设为透明
root.attributes ( '-transparentcolor', 'white' )

# 将窗口的画布设为透明
canvas = tk.Canvas ( root, bg='white', highlightthickness=0 )
canvas.pack ( fill='both', expand=True )

# 绘制一个绿色空心正方形
canvas.create_rectangle ( 5, 5, win_width - 5, win_height - 5, outline='red', width=2 )

# 进入循环让窗口保持打开状态
root.mainloop ()