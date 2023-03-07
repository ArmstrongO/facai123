# 流程分支
# if ....else...
# if 如果   else 否则

age = 18
if age < 18:
    print("小屁孩！")
else:
    print("成年了！")
# 在if else中，条件的分支只会走一个。 也就是说如果满足了if后面的条件，则打印之后，程序结束。
"""
if 条件:     条件： 变量和一个值的比较。 < > <= >= == !=  ,  当事件为真。 python中默认是为真的。
    必须缩进。 缩进不是一个空格，而是四个空格，但是我也不建议你敲四个空格，缩进是一个tab键的距离。  q左边的
else: else后面一定是直接一个冒号，不能接条件。  因为else是收底的。
    else下面也需要缩进。
"""
# if ... elif...else...
# 如果...或者....否则...
# elif 可以有无数个。有多少条件，就可以写多少个。
age = 78
if age < 18:
    print("小屁孩！")
elif age >= 18 and age < 40:
    print("你已经是一个中年人了！")
elif age >= 40 and age < 65:
    print("可以准备晚年生活了！")
elif age >= 65 and age < 80:
    print("想吃点什么吃点什么吧！")
else:
    print("你可能不存在了！")

# 输入一个考试成绩
# 当考试成绩在0-59之间的时候，输出不及格
# 当考试成绩在60-84之间的时候，输出良
# 当考试成绩在85-99之间的时候，输出优秀
# 当考试成绩是100分的时候，输出满分
# 当考试成绩不在0-100范围内的时候，输出成绩不合法！

score = input("请输入你得考试成绩：")  # 通过input()函数所得到的的值，一定是字符串。
if score.isdigit():  # 判断用户输入的内容是否都是数字
    # 为什么score.isdigit()可以作为一个条件呢？   1. 变量和值的比较   2. 当事件为真
    # 布尔值直接可以当做if后面的条件
    score = int(score)
    if 0 <= score < 60:
        print("不及格")
    elif 60 <= score <= 84:
        print("良")
    elif 85 <= score < 100:
        print("优秀")
    elif score == 100:
        print("满分")
    else:
        print("成绩不合法")
else:
    print("你输入的不是数字！")

# input()内置函数
# 控制台交互
# info = input("欢迎光临！请输入你的账号：")
# print(info)

# 通过input输入两个值，分别是用户名和密码。
# 当用户名为admin 密码是 123456的时候，输出密码正确欢迎光临！
# 当用户名错误时，输出，该用户名不存在
# 当用户名正确，密码错误的时候，输出，密码错误！
# username = input("请输入用户名：")
# password = int(input("请输入密码："))
# if username == "admin" and password == 123456:
#     print("密码正确，欢迎光临！")
# elif username != "admin":
#     print("该用户名不存在！")
# elif username == "admin" and password != 123456:
#     print("密码错误！")
# else:
#     pass

# 不写else   和 写else 下面是pass
# 不写else 说明除了上面的情况，我不考虑其他情况，如果出现其他情况则报错。
# 写else下面是pass。 我考虑其他情况，但是如果程序产生了其他情况，我什么也不做。


# 用input输入三个数字的值，判断这个三个值能否形成一个三角形
# 如果能，判断出这是什么三角形？

# 勾股定理
# a = int(input("请输入第一个边："))
# b = int(input("请输入第二个边："))
# c = int(input("请输入第三个边："))
# 先判断这三个边能否形成三角形
# 等边，等腰，直角， 等腰直角， 普通三角形
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("等边三角形")
#     elif a == b or a == c or b == c:
#         if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
#             print("等腰直角三角形")
#         else:
#             print("等腰三角形")
#     elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("对不起，不是三角形！")
