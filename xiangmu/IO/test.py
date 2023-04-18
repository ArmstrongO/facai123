import requests


xfurl="http://1.15.124.181:28019/"
date_login=""
address_ID=""
userID=""

# 注册用户
def register():
    date={
        "loginName": "15212341212",
        "password": "123123"
    }
    res=requests.post(url=f"{xfurl}api/v1/user/register", json=date)
    print(res.json()["message"])
    print(res.text)
    assert res.status_code==200
    # assert res.json()["message"]=="用户名已存在！"

register()