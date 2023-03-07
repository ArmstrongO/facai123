# atm机的取款系统
# 需求：
"""
1. 让用户输入自己的用户名和密码， 正确的用户名 admin  密码 888888
2. 判断用户名和密码的正确与否，当用户名正确密码正确的时候，输出欢迎光临，提示用户请选择你需要办理的业务
业务： 1. 取款   2. 存款  3. 退出   （无论是123都是退出） 但是按3的时候 要提示，感谢使用！再见！
3. 当用户名错误的时候，提示用户不存在，系统直接退出
4. 当用户名正确，密码错误的时候，提示密码错误，请重新输入！当前剩余次数为X次。
5. 当用户输入密码错误的次数超过三次的时候，提示密码错误次数过多，系统冻结！   然后退出
"""


def atm_test():
    print("-----------------欢迎光临小孙ATM银行取款----------------------")
    number = 0
    while True:
        username = input("请输入您的账号：")
        password = input("请输入您的密码：")
        if username == "admin" and password == "888888":
            print("密码正确！欢迎光临,请选择你需要办理的业务：")
            business = input("1.取款 2.存款 3.退出")
            if business == "1":
                break
            elif business == "2":
                break
            elif business == "3":
                print("感谢使用，再见！")
                break
        elif username != "admin":
            print("用户不存在！")
            break
        elif username == "admin" and password != "888888":
            number += 1
            if number > 2:
                print("密码错误次数过多，系统冻结！")
                break
            print(f"密码错误，请重新输入！当前剩余次数为{3 - number}次!")
