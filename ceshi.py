li = [56, 231, 654, 7, 76, 68, 222]

# str1=''
# for i in range(0,len(li)):
#     if li[i]>100:
#         # print(li[i])
#         # str1=f'{str1}{li[i]}'
#         str1 += str(li[i])
#     else:
#         pass
# print(str1)
#
# num1 = 0
# for i in range ( 0, 100 ):
#     if i % 2 ==1:
#      num1 = num1 + 1/i
# print ( num1 )

# li =["x","n","y","k"]
# for i in li:
#     for j in range(1,5):
#         newli = [i,j]
#         print(newli)
# 定义一副扑克牌， 四个花色 红桃，梅花，方块，黑桃。 一个花色13张。
# 13 * 4 == 52  大小王 两张 一共54张
# 扑克牌要以列表保存， ["红桃",1-13] [[],[],[],[],[]54个]
# 大小王 ["Big_Joker"] ["Small_Joker"]

list=["红桃","梅花","方块","黑桃"]
list1=[]
for i in range(list):
    for ii in range(1,14):
        list1 = [i,ii]
        # list1.append(list)
        # print(list1)
        list1.append ( list1 )
# print(list1)
# list1.append["Big_Joker"]
# list1.append["Small_Joker"]
print(list1)

# 现有列表a = ["a","b","c"] b = ["1","2","3"] 将列表形成一个新的列表
# ["a","1","b","2","c","3"]
# a = ["a", "b", "c"]
# b = ["1", "2", "3"]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append ( b[i] )
#     pass


# for i in range(0,3):
#     c.append(a[i])
#     for ii in range(0,3):
#         c.append(b[ii])
#         pass
#     pass
# for i in range(1,2):
#     c.append(a[i])
#     for ii in range(1,2):
#         c.append(b[ii])
#         pass
#     pass
# for i in range(2,3):
#     c.append(a[i])
#     for ii in range(2,3):
#         c.append(b[ii])
#         pass
#     pass


# print ( c )
# 现有列表 li = ["a", "b", "c", "b", "m", "b"]  将列表中b的索引取出来，形成一个新的列表。 结果：[1,3,5]
# li = ["a", "b", "c", "b", "m", "b"]
# li1 = []
# for info in range(0, len(li)):
#     if li[info] == "b":
#         li1.append(info)
#     else:
#         pass
# print(li1)
