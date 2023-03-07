# for循环
# 循环的概念。
# for循环也分为两种写法和模式

# 1. 序列循环 （遍历） 每一个元素都访问一遍。
# 序列可以理解为是一串字符或者元素
# 字符串
# name = "fanmaoxueyuan"
# 列表
# name_list = ["fan", "mao", "xue", "yuan"]
# for na in name_list:  # 要在name_list中遍历循环元素，每一个元素都要拿出来单独的去使用，这个元素 就是na
#     if na == "mao":
#         print(f"这是{na}")
#     else:
#         print(na)
#     print(na)
# print(na)


"""
for 关键字 固定写法
na 是自己起的一个变量名 
in  关键字  固定写法
name 序列的名称 序列可以是一个字符串，也可以是一个列表，当然也可以是元组，字典...
"""
# 现有列表 li = ["a", "b", "c", "b", "m", "b"] 将列表中不是b的元素取出，形成一个字符串acm
# li = ["a", "b", "c", "b", "m", "b"]
# end_str = ""   # end_str = "a"  "ac"
# for l in li:
#     if l == "b":
#         pass
#     else:
#         end_str += l  # end_str = end_str + l
# print(end_str)

# for l in li:
#     if l == "b":
#         li.remove(l)
# print("".join(li))

# 现有列表 li = [56,231,654,7,68], 通过控制台输入两个数字追加进列表中。判断哪些该列表哪些数字大于100，将大于100的数字重新
# 形成一个新的列表。[大于100的数字]
# li = [56, 231, 654, 7, 68]
# num1 = input("第一个数字：")
# num2 = input("第二个数字：")
# li.append(int(num1))
# li.append(int(num2))
# end_li = [] # 用来接收最终的结果
# for i in li:
#     if i > 100:
#         # 这个i就是我要的值
#         end_li.append(i)
#     else:
#         pass
# print(end_li)

# 现有字符串 str1 = "fsdf3fsdf5gsdgs7gdgs9gd" 将字符串中的数字取出形成一个新的字符串  3579
# str1 = "fsdf3fsdf5gsdgs7gdgs9gd"
# str2 = ""
# for s in str1:
#     if s.isdigit():
#         str2 += s
# print(str2)

# 2. range()函数循环
# range()也是一个内置函数，range的用法就是用来去造一个int类型数字的区间。
# range(start, end) start如果不写，默认是0  range()函数中有可能不直接写数字，而是通过一个表达式得到的数字。
# 获取列表的长度当做range的最大长度，就能获取列表的索引值。遍历索引，也可以访问元素。
# li = [56, 231, 654, 7, 68]
# for i in range(0, len(li)):  # 左闭右开   len() 获取序列的长度
#     # for i in range(0, 5)    len(li) == 5    取值范围： 0 1 2 3 4
#     if li[i] > 100:
#         print(li[i])
#     else:
#         pass

# 现有列表 li = ["a", "b", "c", "b", "m", "b"]  将所有b元素的索引取出，形成新的列表[1,3,5]
# li = ["a", "b", "c", "b", "m", "b"]
# end_list = []
# for l in range(0, len(li)):
#     if li[l] == "b":
#         end_list.append(l)
# print(end_list)


# 现有列表a = ["a","b","c"] b = ["1","2","3"] 将列表形成一个新的列表 ["a","1","b","2","c","3"]
# a = ["a","b","c"]
# b = ["1","2","3"]
# ab = []
# for i in range(0, len(a)):   # i的取值范围  0 1 2
#     ab.append(a[i])
#     ab.append(b[i])
# print(ab)

# 求 1/1 + 1/3 + 1/5 + ... 1/99 的和
# sum = 0
# for i in range(1, 100):
#     if i % 2 == 1:
#         sum += 1/i
# print(sum)

'''''
num = 0
ii = 0
while num % 2 == 0:
    ii = ii + num
    num += 2
    if num > 100:
        break
print(ii)
'''''

sum = 0
i = 2
while i <= 100:
    sum += i
    i += 2
print(sum)



#
#
#











# 3. 循环嵌套
# li = ["x", "n", "y", "k"]
# for i in li:
#     for j in range(1,5):
#         newli = [i, j]
#         print(newli)

# 定义一副扑克牌， 四个花色 红桃，梅花，方块，黑桃。 一个花色13张。 13 * 4 == 52  大小王 两张 一共54张
# 扑克牌要以列表保存， ["红桃",1-13] [[],[],[],[],[]54个] 大小王 ["Big_Joker"] ["Small_Joker"]
# python中有内置的库，叫做随机库
# 导入随机库的方式 import
"""
color = ["♥", "♠", "♦", "♣"]
pk = [["Big_Joker"], ["Small_Joker"]]
for c in color:
    for n in range(1, 14):
        poke = [c, n]
        pk.append(poke)
print(pk)
import random
# 使用random库中的一个方法，随机抽取
# for i in range(1, 100):
#     print(random.choice(pk))


"""





