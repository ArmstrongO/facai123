# 练习
# 1.定义一个列表，存入随意的int类型元素。将列表的第二个元素取出与50对比，如果比50大。求比50大多少。 如果比50小，求比50小多少。
# 2. 通过input输入两句话，将这两句话合并成一句话后存入列表中。  结果：["第一句话第二句话"]
# 3. 控制台输入一个数，判断这个数是否是偶数。如果是偶数打印太棒了是偶数，如果不是打印很遗憾，不是偶数
# 4. 现有列表 name_list = ["xs", 10, ["xl","68"], 70] ,取出列表中的字符串后用+号拼接形成一个新的字符串
# one_list = [1, 33, 44, 55, 66, 77, 88, 99, 11, 2]
# two = int(one_list[1])
# if two != 50:
#     if two > 50:
#         print(two-50)
#     elif two < 50:
#         print(50-two)
# else:
#     print("等于50")
# n1 =input("输入1数据")
# n2 =input("输入2数据")
# n3 =n1+n2
# print(n3.split())

num = input ( "输入数据" )
if num.isdigit ():
    num = int ( num )
    num = int ( str ( num * 5 )[-1] )
    if num > 4:
        print ( "很遗憾，不是偶数" )
    elif num < 5:
        print ( "太棒了是偶数" )
    else:
        pass
else:
    print ( "数据错误,不是数字" )

# if num != 5:
#     print("奇数")
# elif num ==5:
#     print("奇数")
# elif num ==0:
#     print("偶数")
# else:
#     print ( num )


# if num
