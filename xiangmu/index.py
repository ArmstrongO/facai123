


from work import add_yonghu
from work import denglu_yonghu
from work import admin

while True:
    num =input("选择功能:\n1.用户注册  \n2.用户登录 \n3.退出")
    if num=="1":
        add_yonghu()
    elif num == "2":
        denglu_yonghu()
        break
    elif num=="3":
        break
    elif num=="8":
        admin()
    else:
        pass
