# 自定义函数

# 什么是函数？
# print() len() type() input() append() split() remove()
# 函数其实就是开发者已经把你封装好了一个独有的功能，当你想用到这个功能的时候，不需要自己去编写程序了。
# 直接使用这个已经封装好的函数名即可。

# 因为函数必须使用才有结果。
# 定义函数
def add():
    x = 10
    y = 20
    print(x + y)

"""
def  define 定义
函数名():  这个函数名自己取，自己想叫什么都行。
函数体内部的逻辑代码必须缩进。
"""


# 调用函数
# add()

# 将add1函数中x设置成全局变量供add2使用。

# def test_add1():
#     global x  # 上下游传参。
#     x = 10
#     y = 20
#     print(x + y)
#
#
# def test_add2():
#     y = 15
#     print(x + y)
#
#
# test_add2()

def test01():
    s = "小孙"
    y = "班班"
    return s

    # 1. return代表函数的结束。
    # 2. return代表函数的返回值，可以更改函数本身的数据类型，return什么类型，该函数就是什么类型。
    # 3. 函数中return是可有可无的，想对于一个函数有返回值，就写return。没有返回值就不写。


print(type(test01()))
















