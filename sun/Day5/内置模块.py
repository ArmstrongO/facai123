# 内置函数  print input  len  type dir range

# open() 函数用来进行文件读写的。  可以查看python的源码进行学习  按住ctrl 鼠标左键点击  源码就是python的开发者写的实现open函数的代码
# open(file=文件名,mode=权限,encoding="utf8") 文件名是可以带路径的。   权限： r:read读  w：write 覆盖写入  a：append 追加写入
# file = open(file=r"C:\Users\xiaosun\PycharmProjects\fanmao123\Day04\xiaosun.txt", mode="a", encoding="utf8")  # encoding 字符编码   utf-8 支持中文的字符编码
# for i in range(1, 101):
#     file.write(f"{i}:这是新增的内容！\n")  #\n 是转义换行的意思


# 内置模块
# random 处理随机的情况  一般导包的语句都放在当前模块的最上面
import random
int1 = random.randint(100000, 999999)  # 从一个int类型的区间取值
print(int1)
# 从一个列表中，从已有的数据随机抽选一个
li = ["x", "s", "i", "z", "m"]
li1 = random.choice(li)
print(li1)


# datetime 日期时间
from datetime import datetime


def get_now_time():
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H-%M-%S") # 进行由时间类型转换成字符串类型且格式化的
    # print(now_str)  # 切片
    return now_str


# 定义一副扑克牌，一共有54张牌。
# 定义四个玩家，分别是小孙，小兰，老赵，老王
# 随机抽取100次牌，不限制每人抽几次，也不限制抽取的顺序。
# 最后打印每次抽取牌的过程，这个过程是一句话： "XXX在时间：XXXXXXXX的时间，抽取到了一张XXX牌"
# 将这个过程打印到文件中。


