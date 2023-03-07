# while 循环
# while 当...时候。

# 死循环
age = 18
while age < 20:
    print("我是小孙")
    age += 3  # 自增长

"""
while 条件:   什么是条件？ 一个变量和一个值的比较   当事件为真
    缩进，循环体内部
    控制条件语句
"""

# 求1-100的偶数和。 while循环来做
# sum = 0
# num = 1
# while num < 101:
#     if num % 2 == 0:
#         sum += num
#     num += 1
# print(sum)

sum = 0
num = 0
while num < 101:
    sum += num
    num += 2
print(sum)

# 有没有什么情况我们希望是死循环的？
# 如果你希望一个程序刚开始是一个死循环，那么这样写
# 如果想在循环中，直接退出，要写一个关键字 叫做： break  终止循环


# students = ["老高", "老莫", "小孙", "安欣"]
# for stu in students:
#     if stu == "老高":
#         print("告诉老莫，我想吃鱼了！")
#     elif stu == "小孙":
#         print("剧里没有我！")
#         break
#     else:
#         print("狂飙！")
















