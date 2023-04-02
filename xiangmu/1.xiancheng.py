# IO密集操作_网络处理_多线程
import requests
import threading
import time
# from requests.packages import target

url="http://119.91.224.105:3000/api/v1/"
accesstoken = "39c620f5-e979-48b4-8790-f79b511ad8d3"


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
        return res.text

def _add_pinglun():
    while 1:
        global reply_id
        date = {
            "accesstoken": accesstoken,
            "content": f"threading_1:{yiyan1 ()}"
        }
        try:
            res= requests.post(url=f"{url}topic/64293913c16f1543e053ae42/replies",json=date)
            res.raise_for_status ()
        except requests.exceptions.RequestException as e:
            print ( "网络连接出现问题: threading_1", e )
            time.sleep(9)
            return None
        else:
            reply_id = res.json()["reply_id"]

def _add_pinglun2():
    while 1:
        date = {
            "accesstoken": accesstoken,
            "content": f"threading_2:{yiyan1 ()}"
        }
        try:
            res= requests.post(url=f"{url}topic/64293912c16f1543e053ae40/replies",json=date)
            res.raise_for_status ()
        except requests.exceptions.RequestException as e:
            print ( "网络连接出现问题: threading_2", e )
            time.sleep ( 9 )
            return None
        else:
            pass

def _add_pinglun3():
    while 1:
        date = {
            "accesstoken": accesstoken,
            "content": f"threading_3:{yiyan1 ()}"
        }
        try:
            res= requests.post(url=f"{url}topic/6429258cc16f1543e052161c/replies",json=date)
            res.raise_for_status ()
        except requests.exceptions.RequestException as e:
            print ( "网络连接出现问题: threading_3", e )
            time.sleep ( 9 )
            return None
        else:
            pass
def _add_pinglun4():
    while 1:
        date = {
            "accesstoken": accesstoken,
            "content": f"threading_4:{yiyan1 ()}"
        }
        try:
            res= requests.post(url=f"{url}topic/64293912c16f1543e053ae41/replies",json=date)
            res.raise_for_status ()
        except requests.exceptions.RequestException as e:
            print ( "网络连接出现问题: threading_4", e )
            time.sleep ( 9 )
            return None
        else:
            pass





t1=threading.Thread(target=_add_pinglun)
t1.start()
t2=threading.Thread(target=_add_pinglun2)
t2.start()
t3=threading.Thread(target=_add_pinglun3)
t3.start()
t4=threading.Thread(target=_add_pinglun4)
t4.start()
t5=threading.Thread(target=_add_pinglun2)
t5.start()
t6=threading.Thread(target=_add_pinglun3)
t6.start()
t7=threading.Thread(target=_add_pinglun4)
t7.start()
t8=threading.Thread(target=_add_pinglun2)
t8.start()
t9=threading.Thread(target=_add_pinglun3)
t9.start()
t10=threading.Thread(target=_add_pinglun4)
t10.start()
t11=threading.Thread(target=_add_pinglun2)
t11.start()
t12=threading.Thread(target=_add_pinglun3)
t12.start()
t13=threading.Thread(target=_add_pinglun4)
t13.start()
t14=threading.Thread(target=_add_pinglun2)
t14.start()
t15=threading.Thread(target=_add_pinglun3)
t15.start()
t16=threading.Thread(target=_add_pinglun4)
t16.start()




t1.join()



for n in range ( 1, 30000 ):

    _add_pinglun()