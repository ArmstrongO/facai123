"""
代码要求： 两个模块，  program.py 用来定义函数  call_pro.py  用来调用函数

业务需求：
1.定义注册和登录功能，用户名和密码用列表保存 [{"username":"xxx","password":""}]
2.注册好之后，使用用户名可以登录系统。 提示"欢迎来到图书管理系统，自己定义提示语"
如果用户名不存在，提示用户名不存在，重新选择业务。
如果用户名正确密码错误，提示密码错误，如果次数超过三次提示账号已被冻结，请联系管理员，随之退出系统。
3.输入1为注册，2为登录，3为退出
4.进入系统后，可以对于图书进行增删改查的处理，图书有四个属性，图书编号，书名，作者，出版社。
5.输入1为新增图书，2为查询，3为修改，4.为删除，5为退出，输入其他提示输入的内容不合法
6.新增图书成功后，可以查到该图书信息，图书编号不能重复
查询图书根据图书编号进行查询，如果输入的编号不存在，提示该图书不存在
修改图书根据图书编号进行修改，可供修改的信息有书名，作者，出版社。
删除图书后，再次查询应该没有相关内容
"""

yonghu = [{'ID': 'a', 'Pass': 'a'}]
def add_yonghu():
    id = input("请输入用户名：")
    for inf in yonghu:
        if inf["ID"] == id:
            print("用户名输入重复，系统退回主界面")
            return   # 结束函数
    passwd = input("请输入密码：")
    yonghu_info = {
        "ID": id,
        "Pass": passwd
    }
    yonghu.append(yonghu_info)

def denglu_yonghu():
    id = input("请输入用户名：")
    for inf in yonghu:
        ppp = 3
        while True:
            if inf["ID"] == id:
                passwd = input ( "请输入密码: " )
                if inf["Pass"] == passwd:
                    tushuguanli()
                else:
                    print ( "密码错误，请重新输入" )
                    if ppp < 2:
                        print ( "密码超过3次，系统冻结,请联系管理员" )
                        break
                    else:
                        ppp -= 1
                        print ( "当前可输入次数" + str ( ppp ) )
            else:
                print ( "用户名不存在，重新选择业务" )
                return


def admin():
    print(yonghu)


tushu = []
def add_tushu():
    id = input("请输入图书编号：")
    for inf in tushu:
        if inf["ID"] == id:
            print("图书编号输入重复，系统退回主界面")
            return   # 结束函数
    shuming = input ( "请输入书名：" )
    zuozhe = input ( "请输入作者：" )
    chubanshe = input ( "请输入出版社：" )
    yonghu_info = {
        "ID": id,
        "SHUMING": shuming,
        "ZUOHE": zuozhe,
        "CHUBANSHE": chubanshe
    }
    tushu.append(yonghu_info)
def search_tushu():
    id = input("请输入需要查询的图书编号:")
    for inf in tushu:
        if inf["ID"] == id:
            print(inf)
            return   # 结束函数
    print("未找到")

def xiugai_tushu():
    id = input("请输入需要修改的图书编号:")
    for inf in tushu:
        if inf["ID"] == id:
            shuming = input ( "请输入书名：" )
            zuozhe = input ( "请输入作者：" )
            chubanshe = input ( "请输入出版社：" )
            inf["SHUMING"]=shuming
            inf["ZUOZHE"]=zuozhe
            inf["CHUBANSHE"]=chubanshe
            print("修改信息成功!")
            return   # 结束函数
    print("未找到图书编号，请检查！")

def del_tushu():
    id = input("请输入需要删除的图书编号:")
    for inf in tushu:
        if inf["ID"] == id:
            tushu.remove(inf)
            print("图书删除成功")
            return
    print("未找到图书编号，请检查！")

def admin1():
    print(tushu)

def tushuguanli():
    while True:
        num =input("图书功能选项：\n1.新增图书\n2.查询\n3.修改\n4.删除\n5.退出\n6.显示书架")
        if num=="1":
            add_tushu()
        elif num == "2":
            search_tushu()
        elif num=="3":
            xiugai_tushu()
        elif num =="4":
            del_tushu()
        elif num == "5":
            break
        elif num =="6":
            admin1()
        else:
            print("输入不合法")
