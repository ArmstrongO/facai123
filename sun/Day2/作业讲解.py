# 编程题
# 1.# 现有列表
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
info = str(input("请输入一句话："))
num = list1[2]
num2 = list1[4][1]['age']
if info =="int":
    # str.isdigit()
    # 将列表中int类型数字取出求和
    # 定义函数num和num2，并取值，
    # 值为int类型，再相加
    print ( num + num2 )
    pass
elif info =="str":
    # int类型值转为str类型，再相加
    num = str ( num )
    num2 = str ( num2 )
    print ( num + num2 )
    pass
elif info =="split":
    pass
else:
    pass
print(info)


# 字符串转换拼接
print(f"{num}{num2}")
# str类型转换为列表，再相加
n=num+num2
num=num.split()
num2=num2.split()
print(n.split())
print(num+num2)

# print("".join(n))


# 将txt取出，统计里面有几个t元素
t = list1[3]
print(t.count("t"))
# 从列表中取出元素，形成一个文件名"nice.txt"
print(f"{list1[4][2]}.{list1[3]}")
# 2xy和2xn判断他们是否相等
print(list1[4][0] == list1[4][3][1])
# 2.定义字符串"fanmao123"
#     求字符串中第3到最后一位的字符
#     求字符串的英文部分
#     求字符串中的三个数字，并把这三个数字求和
#     求mao
cl = "fanmao123"
print(cl[2:])
print(cl[:-3])
print(int(cl[-3]) + int(cl[-2]) + int(cl[-1]))
# 3. 定义列表 name_list = ["苹果","香蕉","西瓜","葡萄"],将西瓜取出后，形成一句话，"我最喜欢吃的水果是西瓜"。
name_list = ["苹果", "香蕉", "西瓜", "葡萄"]
print(f"我最喜欢吃的水果是{name_list[-2]}")
# 4. 手写字典，定义4个key，分别是，手机型号，手机内存，手机品牌，手机的app。其中手机品牌需要定义列表存储多个品牌
#    app需要定义键值对，"app名称"："类型"  类型比如：游戏，社交，理财...
phone = {
    "model": "iphone镶钻99",
    "memory": "512G",
    "brand": ["苹果", "oppo", "小米", "华为", "Nokia"],
    "application": {
        "wechat": "社交",
        "League of Legends": "游戏",
        "zfb": "支付宝"
    }
}
