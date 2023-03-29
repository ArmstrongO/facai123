
import requests
import time



url="http://119.91.224.105:3000/api/v1/"

def yiyan():
    date = {
        "c": "j",
        "encode": "text"
    }
    res = requests.get(url="https://v1.hitokoto.cn/", params=date)
    return res.text
def yiyan1():
    date = {
        "c": "f",
        "encode": "text"
    }
    res = requests.get(url="https://v1.hitokoto.cn/", params=date)
    return res.text
accesstoken = "39c620f5-e979-48b4-8790-f79b511ad8d3"
topic_id = ""
# 新建主题
x=yiyan()
y=0
def add_zt():
    global topic_id
    date={
        "accesstoken": accesstoken,
        "title": f"主题{y}:{yiyan()}",
        "tab":"ask",
        "content": f"内容:{yiyan1()}"
    }

    res = requests.post ( url=f"{url}topics", json=date )
    topic_id = res.json ()["topic_id"]


for n in range ( 1, 30000 ):
    y+=1
    add_zt ()
    time.sleep(1)
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

