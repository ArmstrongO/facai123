
# 现有列表 li = ["a", "b", "c", "b", "m", "b"]  将列表中b的索引取出来，形成一个新的列表。
# 结果：[1,3,5]
# li = ["a", "b", "c", "b", "m", "b"]
# print(li.index("b"))

# 现有列表 li = ["a", "b", "c", "b", "m", "b"] 将列表中不是b的元素取出，形成一个字符串acm
li = ["a", "b", "c", "b", "m", "b"]
info=[]
for no in li :
    if no == "b":
        pass
    else:
        info.append(no)
        pass
    # print(no)
    pass
print("".join(info))

# 现有列表 li = [56,231,654,7,68], 通过控制台输入两个数字追加进列表中。
# 判断哪些该列表哪些数字大于100，将大于100的数字重新
# 形成一个新的列表。[大于100的数字]
li = [56,231,654,7,68]
info =int(input("请输入一个数字"))
info2 =int(input("请输入一个数字"))
li.append(info2)
li.append(info)
li2=[]
for no in li:
    if no > 100:
        li2.append(no)
    else:
        # print(no)
        pass
        # li.remove ( no )
    # print(no)
    pass
print(li2)
    # li.remove ( no )



