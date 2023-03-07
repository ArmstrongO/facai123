# 1. if if   if elif的区别

# age = 18
# if age > 20:
#     print("111")
# elif age < 30:
#     print("222")
# else:
#     print("333")

# 2. 控制台输入一句话"this is my python class room" 将这句话的前4个单词都单独的存入列表中，结果["this", "is", "my", "python"]
info = input("请输入一句话：")
print(info[0:-11].split(" "))

info = input("请输入一句话")
print(info.split(" ")[:4])
# 3. 定义一个列表，["nice", "good", "perfect", "excellence"] 计算f在perfect单词中的索引位置
info = ["nice", "good", "perfect", "excellence"]
print(info[2].index("f"))
# 4. 控制台输入两个数字，经过判断他们如果都是数字，则让他们相加求和。如果输入的第一个元素不是数字，则输出“你输入的第一个元素不是数字”
# 如果输入的第二个元素不是数字，则输出“你输入的第二个元素不是数字”
num1 = input("第一个数字：")
if num1.isdigit():
    num1 = int(num1)
    num2 = input("第二个数字：")
    if num2.isdigit():
        num2 = int(num2)
        print(num1 + num2)
    else:
        print("你输入的第二个元素不是数字！")
else:
    print("你输入的第一个元素不是数字！")

# num1 = input("请输入第一个数字：")
# num2 = input("请输入第二个数字：")
# if num1.isdigit():
#     if num2.isdigit():
#         print(int(num1)+int(num2))
#     else:
#         print("你输入的第二个元素不是数字")
# else:
#     print("你输入的第一个元素不是数字")

# 5. 定义一个列表["a", "b", "c"] 控制台输入一个d元素，将这个新的元素追加进列表中后，变成一个字符串 结果：abcd
li = ["a", "b", "c"]
d = input("输入一个d：")
li.append(d)  # ["a", "b", "c", "d"]   abcd
print("".join(li))













