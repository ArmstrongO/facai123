
import requests
import time
import threading #si'ruai'di



url="http://119.91.224.105:3000/api/v1/"

def yiyan():
    date = {
        "c": "j",
        "encode": "text"
    }
    res = requests.get(url="https://v1.hitokoto.cn/", params=date)
    return res.text
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
        print("网络连接出现问题: ", e)
        return None
    else:
        return res.text
accesstoken = "39c620f5-e979-48b4-8790-f79b511ad8d3"
topic_id = ""
reply_id = ""
x=yiyan()
y=0
def add_zt():
    global topic_id
    date = {
        "accesstoken": accesstoken,
        "title": f"{yiyan()}",
        "tab": "ask",
        "content": f"内容:{yiyan1()}"
    }
    try:
        res = requests.post ( url=f"{url}topics", json=date )
    except requests.exceptions.RequestException as e:
        print("网络连接出现问题: ", e)
        return None
    else:
        topic_id = res.json ()["topic_id"]
        print ( topic_id )
        print({yiyan()})
        return res.text

def add_pinglun():
    global reply_id
    date = {
        "accesstoken": accesstoken,
        "content": f"threading_1:{yiyan1 ()}"
    }
    try:
        res= requests.post(url=f"{url}topic/{reply_id}/replies",json=date)
        res.raise_for_status ()
    except requests.exceptions.RequestException as e:
        print ( "网络连接出现问题: threading_1", e )
        time.sleep(9)
        return None
    else:
        reply_id = res.json()["reply_id"]


def eeee():
    while 1:
        add_zt()
t1=threading.Thread(target=eeee())
t1.start()
t2=threading.Thread(target=eeee())
t2.start()
t3=threading.Thread(target=eeee())
t3.start()
t4=threading.Thread(target=eeee())
t4.start()



t1.join()
# for n in range ( 1, 30000 ):
#     y+=1
#     add_zt ()
#     time.sleep(1)
    # print(yiyan())


# # 主题首页
# def shouye():
#     date={
#         "page": 1,
#         "tab": "ask",
#         "limit": 1
#     }
#     res = requests.get(url=f"{url}topics", params=date)
#     print(f"返回状态码{res.status_code}")
#     print(res.json()["success"])
#
#     file = open ( file="puke.txt", mode="a", encoding="utf8" )
#     file.write ( f"{res.json ()['date']}" )
#
#     # print (f"{res.json ()['date']}")
#     # print(res.json())
# #     断言
#     assert res.status_code==200
#     assert res.json()["success"]==True
#     # assert res.json()["date"][0].tab==date["tab"]
#     for aa in res.json()["data"]:
#         assert aa["tab"]==date["tab"]
#     assert len(res.json()["data"]) == date["limit"]
# # shouye()
#
#
#
#
#
#
#
#
#
# # 编辑主题
# def edit_zt():
#     date={
#         "accesstoken":accesstoken,
#         "topic_id":topic_id,
#         "title": "青青草原大大",
#         "tab":"ask",
#         "content":"这是主题内容"
#     }
#
#
#
#
#
#
#
#
#
#
#

    # return res

