import datetime
import random

# 获取当前时间
def get_now_time():
    now = datetime.datetime.now()   # 获取当前时间，但是当前时间的类型是时间类型。
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")  # 从时间类型过渡到字符串类型，并格式化
    return now_str  # 返回当前时间



def games():
    color = ["♥", "♠", "♦", "♣"]
    pk = [["Big_Joker"], ["Small_Joker"]]
    for c in color:
        for n in range(1, 14):
            poke = [c, n]
            pk.append(poke)
    # print(pk)

    # 使用random库中的一个方法，随机抽取
    for i in range(0, 10):
        print(f"小孙在{get_now_time()}抽到了一张：{random.choice(pk)}")


games()