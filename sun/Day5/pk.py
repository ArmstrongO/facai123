# 定义一副扑克牌，将扑克牌的内容打印进文本中，文本名： joker.txt

# def joker_file():
#     # 定义出一副扑克牌  [[],[],[],大王,小王]
#     pk = ["b_king","s_king"]
#     color = ["红桃", "黑桃", "方片", "梅花"]
#     for i in color:
#         for j in range(1, 14):
#             poke = f"{[i, j]}\n"
#             # print(poke)
#             pk.append(poke)
#     return pk
#
#
# def write_poke():
#     file = open(file="joker.txt", mode="a",encoding="utf8")
#     file.write(f"{joker_file()}\n")


def joker_file():
# 定义出一副扑克牌  [[],[],[],大王,小王]
    color = ["红桃", "黑桃", "方片", "梅花"]
    for i in color:
        for j in range(1, 14):
            file = open(file="joker.txt", mode="a", encoding="utf8")
            file.write(f"{[i, j]}\n")
    file.write("大王\n")
    file.write("小王")

joker_file()

