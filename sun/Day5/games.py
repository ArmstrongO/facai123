# 定义一副扑克牌，一共有54张牌。
# 定义四个玩家，分别是小孙，小兰，老赵，老王
# 随机抽取100次牌，不限制每人抽几次，也不限制抽取的顺序。
# 最后打印每次抽取牌的过程，这个过程是一句话： "XXX在时间：XXXXXXXX的时间，抽取到了一张XXX牌"
# 将这个过程打印到文件中。

import random, datetime


# 获取时间函数
def get_now_time():
    now = datetime.datetime.now()
    str_now = now.strftime("%Y-%m-%d %H-%M-%S")
    # print(str_now) # 打印是给自己进行调试看的。
    return str_now


# 定义出一副扑克牌  [[],[],[],大王,小王]
def get_poke():
    pk = ["b_king", "s_king"]
    color = ["红桃", "黑桃", "方片", "梅花"]
    for i in color:
        for j in range(1, 14):
            poke = [i, j]
            # print(poke)
            pk.append(poke)
    return pk


def games():
    players = ["小孙", "小兰", "老赵", "老王"]
    file = open(file="result.txt", mode="a", encoding="utf8")
    for i in range(1, 101):
        file.write(f"{random.choice(players)}在时间：{get_now_time()}的时间，抽取到了一张{random.choice(get_poke())}牌\n")

games()
