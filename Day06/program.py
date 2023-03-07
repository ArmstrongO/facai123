# """
# 代码要求： 两个模块，  program.py 用来定义函数  call_pro.py  用来调用函数
#
# 业务需求：
# 1.定义注册和登录功能，用户名和密码用列表保存 [{"username":"xxx","password":""}]
# 2.注册好之后，使用用户名可以登录系统。 提示"欢迎来到图书管理系统，自己定义提示语"
# 如果用户名不存在，提示用户名不存在，重新选择业务。
# 如果用户名正确密码错误，提示密码错误，如果次数超过三次提示账号已被冻结，请联系管理员，随之退出系统。
# 3.输入1为注册，2为登录，3为退出
# 4.进入系统后，可以对于图书进行增删改查的处理，图书有四个属性，图书编号，书名，作者，出版社。
# 5.输入1为新增图书，2为查询，3为修改，4.为删除，5为退出，输入其他提示输入的内容不合法
# 6.新增图书成功后，可以查到该图书信息，图书编号不能重复
# 查询图书根据图书编号进行查询，如果输入的编号不存在，提示该图书不存在
# 修改图书根据图书编号进行修改，可供修改的信息有书名，作者，出版社。
# 删除图书后，再次查询应该没有相关内容
# """


info = [{'username': '1', 'password': '1'}, {'username': '2', 'password': '2'}, {'username': '3', 'password': '3'}]


def np():
    name = input("请输入用户名:")
    for i in info:
        if i["username"] == name:
            print("用户已存在")
            return
    pw = input("请输入密码:")
    zl = {
        "username": name,
        "password": pw
    }
    info.append(zl)
    print("注册成功")


def dl():
    li = True
    name = input("请输入用户名:")
    for j in info:
        if name == j["username"]:
            num = 1
            while num <= 3:
                pw = input("请输入密码：")
                li = False
                if pw == j["password"]:
                    print("欢迎来到图书管理系统，祝您阅读愉快")
                    return "成功"
                elif num >= 3:
                    print("账号已被冻结，请联系管理员")
                    return
                elif pw != j["password"]:
                    print(f"您输入的密码错误，剩余{3 - num}次")
                num += 1
    if li:
        print("用户名不存在")
        return

# dl()
info2 = []


def book_add():
    num = input("请输入图书编号:")
    for b in info2:
        if num == b["id"]:
            print("图书已存在")
            return
    bn = input("请输入书名:")
    author = input("请输入作者:")
    press = input("请输入出版社:")
    bx = {
        "numbers": num,
        "book_name": bn,
        "book_author": author,
        "book_press": press
    }
    info2.append(bx)
    print("新增图书成功")


def inquire():
    num = input("请输入您要查询的图书编号：")
    for i in info2:
        if num == i["numbers"]:
            print(i)
            return
    print("该图书不存在")


def revamp():
    num = input("请输入您要查询的图书编号")
    for i in info2:
        if num == i["numbers"]:
            bn = input("请输入书名:")
            author = input("请输入作者:")
            press = input("请输入出版社:")
            i["book_name"] = bn
            i["book_author"] = author
            i["book_author"] = press
            print("修改成功")
            return
    print("该图书不存在")


def del_book():
    num = input("请输入图书编号:")
    for i in info2:
        if num == i["numbers"]:
            info2.remove(i)
            return
    print("该图书不存在")
