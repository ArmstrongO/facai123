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
    assert res.status_code==200
    # assert res.json()["message"]=="用户名已存在！"

# 登录
register()
def login():
    global date_login
    date={
        "loginName": "15212341212",
        "passwordMd5": "4297f44b13955235245b2497399d7a93"
    }
    res = requests.post ( url=f"{xfurl}api/v1/user/login", json=date )
    print(res.text)
    print ( f"{'用户登录'}{res.json ()['message']}" )
    assert res.status_code==200
    assert res.json()["message"]=="SUCCESS"
    date_login = res.json()['data']

# print(date_login)
login()

# 获取用户信息
def get_user_message():
    res = requests.get ( url=f"{xfurl}api/v1/user/info",headers={'token':date_login} )
    print ( f"{'获取用户信息'}{res.json ()['message']}" )

# 修改用户信息
def update_user_message():
    date={
        "introduceSign": "mingzezuishuai",
        "nickName": "mingzezui",
        "passwordMd5": "4297f44b13955235245b2497399d7a93"
    }
    res = requests.put ( url=f"{xfurl}api/v1/user/info",headers={'token':date_login},json=date)
    print ( f"{'修改用户信息'}{res.json ()['message']}" )



# 新增地址
def add_address():
    date = {
        "cityName": "上海市",
        "defaultFlag": 0,
        "detailAddress": "天宝路999号",
        "provinceName": "上海市",
        "regionName": "虹口区",
        "userName": "宿舍",
        "userPhone": "16612341234"
    }
    res = requests.post ( url=f"{xfurl}api/v1/address",headers={'token':date_login},json=date)
    print ( f"{'新增地址'}{res.json ()['message']}" )





# 我的收货地址列表
def my_address_list():
    global address_ID
    global userID
    res = requests.get ( url=f"{xfurl}api/v1/address", headers={'token': date_login})
    # print ( res.json () )
    userID=res.json()["data"][0]['userId']
    address_ID=res.json()["data"][0]['addressId']
    print ( f"{'我的收货地址列表zhi'}{address_ID}" )

# 获取收货地址详情
def get_address_detail():
    res = requests.get ( url=f"{xfurl}api/v1/address/{address_ID}", headers={'token': date_login})
    print ( f"{'获取收货地址详情'}{res.json()['message']}" )
    # print(res.json()['message'])


# 获取默认收货地址
def get_default_address():
    res = requests.get ( url=f"{xfurl}api/v1/address/default", headers={'token': date_login} )
    print ( f"{'获取默认收货地址'}{res.json()['message']}" )
    # print(res.json())


# 修改地址
def update_address():
    date={
        "addressId": address_ID,
        "cityName": "上海市",
        "defaultFlag": 1,
        "detailAddress": "天宝路999号",
        "provinceName": "上海市",
        "regionName": "虹口区",
        "userId": userID,
        "userName": "宿舍",
        "userPhone": "16612341234"
    }
    res = requests.put( url=f"{xfurl}api/v1/address",headers={'token':date_login},json=date)
    print ( f"{'修改地址'}{res.json()['message']}" )

# update_address()
# 删除地址
def delete_address():
    res = requests.delete ( url=f"{xfurl}api/v1/address/{address_ID}", headers={'token': date_login})
    print ( f"{'删除地址'}{res.json()['message']}" )
    # return
# delete_address()

# 登出
def logout():
    res = requests.post ( url=f"{xfurl}api/v1/user/logout",headers={'token':date_login}  )
    print ( f"{'登出'}{res.json ()['message']}" )
# logout()
# logout()