# 现有列表 li = [56,231,654,7,68], 通过控制台输入两个数字追加进列表中。
# 判断哪些该列表哪些数字大于100，将大于100的数字重新
# 形成一个新的列表。[大于100的数字]
# li = [56,231,654,7,68]
# info =int(input("请输入一个数字"))
# info2 =int(input("请输入一个数字"))
# li.append(info2)
# li.append(info)
# li2=[]
# # ss=''
# li2 = [56,231,654,7,76,68,222]
# li3 = li2[:]
# for ii range(0,len(li2)):
#     if li2[ii]>100:
#         print(li2[ii])

# for no in li2:
#     if no > 100:
#         pass
#     else:
#         li3.remove(no)
#         print(li2)
#     # print(li2)
#     pass
# print(li3)

# 现有字符串 str1 = "fsdf3fsdf5gsdgs7gdgs9gd" 将字符串中的数字取出形成一个新的字符串  3579

# str1 = "fsdf3fsdf5gsdgs7gdgs9gd"
# str2 = ""
# for info in str1:
#     if info.isdigit():
#         # print(info)
#         str2=f"{str2}{info}"
#     else:
#         pass
#     pass
# # print ( info )
# print(str2)

# 现有列表 li = ["a", "b", "c", "b", "m", "b"]  将列表中b的索引取出来，形成一个新的列表。
# 结果：[1,3,5]
li = ["a", "b", "c", "b", "m", "b"]
li2=[]
for i in range(0,len(li)):
    if li.index("b"):
        li2.append(i)
    else:
        pass
# print(li.index("b"))
print(li2)






# for ss in li:
#     if ss : "b"
#         print(ss)
#     else:
#         pass
#     pass

