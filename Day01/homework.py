list1 = [
    "abc", "2", 2, "txt", [
        "2xy", {
            "name": "xs",
            "age": 58
        },
        "nice"
        ,
        ["fnq", "2xn"]
    ],
    "nf",
    "red"
]
# 将列表中int类型数字取出求和
print ( list1[2] + list1[4][1]["age"] )
# 将txt取出，统计里面有几个t元素
print ( list1[3].count ( "t" ) )
# 从列表中取出元素，形成一个文件名"nice.txt"
print ( list1[4][2] + list1[3] )
print ( f"{list1[4][2]}.{list1[3]}" )
# 2xy和2xn判断他们是否相等
print ( (list1[4][0]) == print ( list1[4][3][1] ) )

# 定义字符串"fanmao123"
#     求字符串中第3到最后一位的字符
#     求字符串的英文部分
#     求字符串中的三个数字，并把这三个数字求和
#     求mao
# str1 = "fanmao123"
# print ( str1[2:] )
# print ( str1[:6] )
# print ( str1[-3:] )
# print ( int ( str1[-3] ) + int ( str1[-2] ) + int ( str1[-1] ) )
# print ( str1[3:6] )

# 定义列表 name_list = ["苹果","香蕉","西瓜","葡萄"],将西瓜取出后，形成一句话，"我最喜欢吃的水果是西瓜"。
name_list = ["苹果", "香蕉", "西瓜", "葡萄"]
print ( "我最喜欢吃的水果是" + name_list[2] )

# 手写字典，定义4个key，分别是，手机型号，手机内存，手机品牌，手机的app。其中手机品牌需要定义列表存储多个品牌
# app需要定义键值对，"app名称"："类型"  类型比如：游戏，社交，理财...
mydir = {
    "mod": "iPhone 11 Pro Max",
    "mem": "512G",
    "brand": ["iPhone", "xiaomi", "huawei"],
    "app": {
        "name": "QQ",
        "lei": ["game", "wechat", "licai"],
    }
}
# print ( mydir )

info = False
if info:
    print ( "这是真!" )
else:
    print ( "这是假!" )

age = 77
if age > 18:
    if age > 40:
        if age > 65:
            print ( "大于65，该退休了" )
        else:
            print ( "小于65的中年人" )
    else:
        print ( "青壮年" )
else:
    print ( "未成年" )
# 输入一个考试成绩
# 当考试成绩在0-59之间的时候，输出不及格
# 当考试成绩在60-84之间的时候，输出良
# 当考试成绩在85-99之间的时候，输出优秀
# 当考试成绩是100分的时候，输出满分
# 当考试成绩不在0-100范围内的时候，输出成绩不合法！

# fs = input ( "请输入分数：" )
# fs = int ( fs )
# if fs > 59:
#     if fs > 84:
#         if fs > 99:
#             if fs > 100:
#                 print ( "不合法" )
#             else:
#                 print ( "满分" )
#         else:
#             print ( "优秀" )
#     else:
#         print ( "良好" )
# else:
#     print ( "不及格" )

# 通过input输入两个值，分别是用户名和密码。
# 当用户名为admin 密码是 123456的时候，输出密码正确欢迎光临！
# 当用户名错误时，输出，该用户名不存在
# 当用户名正确，密码错误的时候，输出，密码错误！


# cj = 88
# if cj < 60:
#     print ( "不及格" )
# elif 60 <= cj < 85:
#     print ( "良好" )
# elif 85 <= cj < 100:
#     print ( "优秀" )
# elif cj == 100:
#     print ( "满分" )
# else:
#     print ( "不合法" )
triangle1 = input("请输入数值")
triangle2 = input("请输入数值")
triangle3 = input("请输入数值")
triangle1 = int(triangle1)
triangle2 = int(triangle2)
triangle3 = int(triangle3)


if triangle1 + triangle2 + triangle3 == 180:
    if triangle1 == triangle2 == triangle3:
        print("等边三角形")
    elif triangle1 == 90 or triangle2 == 90 or triangle3 == 90:
        if triangle1 == 45 or triangle2 == 45 or triangle3 == 45:
            print("等腰直角三角形")
        else:
            print("直角三角形")
    elif triangle1 == triangle3 or triangle3 == triangle2 or triangle1 == triangle2:
        if triangle1 == 36 or triangle2 == 36 or triangle3 == 36:
            print("黄金三角形")
        else:
            print("等腰三角形")
    else:
        print("三角形")
else:
    print("bushi三角形")

