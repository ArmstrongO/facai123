# 字符串的对象函数
# 1. count() 统计某一个字符在字符串中出现的次数

# 2. index() 统计某一个字符在字符串中的索引

# 3. isdigit() 判断一个字符串中是否都是数字
# name = "123n"
# print(name.isdigit())

# 4. split() 以指定的分隔符对字符串进行切割，将切割好的元素形成一个新的列表。
# 实现了由字符串向列表的转换。
# name = "fanmaoxueyuan"
# print(name.split("am"))

# 5. join() 以指定的连接符进行拼接，将一个字符串或者列表拼接形成一个新的字符串
# 由列表转换成字符串
# name = ["fan","mao","xue",]

# 练习
# 1.定义一个列表，存入随意的int类型元素。将列表的第二个元素取出与50对比，如果比50大。求比50大多少。 如果比50小，求比50小多少。
# li = [10, 60, 80, 45, 43, 75, 325, 23]
# if li[1] > 50:
#     print(li[1] - 50)
# elif li[1] < 50:
#     print(50 -li[1])
# else:
#     print("他们相等！")
# 2. 通过input输入两句话，将这两句话合并成一句话后存入列表中。  结果：["第一句话第二句话"]
# info1 = input("请输入第一句话")   # ctrl + d 快速复制一句话
# info2 = input("请输入第二句话")
# # info_all = info1 + info2
# print([info_all])
# print((info1 + info2).split())
# print("".join(info1 + info2).split())
# 3. 控制台输入一个数，判断这个数是否是偶数。如果是偶数打印太棒了是偶数，如果不是打印很遗憾，不是偶数
# number = int(input("请输入一个数："))
# if number % 2 == 0:
#     print("偶数")
# else:
#     print("很遗憾")
# 4. 现有列表 name_list = ["xs", 10, ["xl","68"], 70] ,取出列表中的字符串后用+号拼接形成一个新的字符串
# name_list = ["xs", 10, ["xl","68"], 70]
# # print(f"{name_list[0]}+{name_list[2][0]}+{name_list[2][1]}")
# print("+".join([name_list[0], name_list[2][0], name_list[2][1]]))


# 列表
# 1. append() 向列表的最后一位追加一个元素
name = ["fanmao","xueyuan"]
# name.append("xueyuan")  # append() 叫做追加，追加是一个过程，打印过程则为空。
# print(name)
# 2. remove() 删除列表中的某一个元素
name.remove("xue")
print(name)
# ValueError: list.remove(x): x not in list





