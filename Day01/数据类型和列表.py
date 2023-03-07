# a = 1
# c = 1
# vv = 111
# qq = 1
# o = a + vv + qq
# print ( c )
# print ( o )
# cc = "true"
# cs = 80
# cc += cs
# print(cc)

# <  print("hello world")
# 张三 = 12
# 李四 = 55
# 王五=张三+李四
# print(王五)>

#
#
# name = "老孙"
# book = "孙子兵法"
# author = "孙老"
# sales = "100"
# friend = "老张"
# print(
#     "我叫：" + name +
#     "，我今天买了一本叫:" + book +
#     "，这本书的作者是:" + author +
#     "，这本书今年一共销售了:" + sales +
#     "，我会把他推荐给我的朋友" + friend
#     )
#
# info = "fanmaoxueyuan"
# print(info[3:-1])
# 从info的第一到第五位
# 从头到倒数第三位
# 取mao
# 从倒数第四位取到最后
# 从第五位到y
# print(info[:5])
# print(info[:-2])
# print(info[3:6])
# print(info[-4:])
# print(info[4:-3])
# info_list = (1,2,3,4,5)
# print(info.index(""))
# a = 1
# c = 1
# vv = 111
# qq = 1
# o = a + vv + qq
# print ( c )
# print ( o )
# cc = "true"
# cs = 80
# cc += cs
# print(cc)

# <  print("hello world")
# 张三 = 12
# 李四 = 55
# 王五=张三+李四
# print(王五)>

#
#
# name = "老孙"
# book = "孙子兵法"
# author = "孙老"
# sales = "100"
# friend = "老张"
# print(
#     "我叫：" + name +
#     "，我今天买了一本叫:" + book +
#     "，这本书的作者是:" + author +
#     "，这本书今年一共销售了:" + sales +
#     "，我会把他推荐给我的朋友" + friend
#     )
#
info = "fanmaoxueyuan"
# print(info[3:-1])
# 从info的第一到第五位
# 从头到倒数第三位
# 取mao
# 从倒数第四位取到最后
# 从第五位到y
# print(info[:5])
# print(info[:-2])
# print(info[3:6])
# print(info[-4:])
# print(info[4:-3])
# info_list = (1,20,3,4,5)
# print(info.index(""))
# print(info_list[1][0])

# 现有列表 ln = []
ln = ["2", "3", 2, ["老赵", "老孙"], "we", "['t']", 45, ["233"]]

# 取出老赵和老孙后，合并成 "老赵老孙"
# 计算列表中int类型的和
# 将233与3进行相乘。
print(ln[3][0]+ln[3][1])
print(f"{ln[3][0]}{ln[3][1]}")
print(int(ln[2]) + int(ln[6]))
print(int(ln[1]) * int(ln[-1][0]))
# print(f{ln[1])} ,f{ln[-1][0]})
print(ln[4] + ln[5][2])
ln[3][0] = "老王"
print(ln)
print(str(ln[-1][0]) + str(ln[-2]))