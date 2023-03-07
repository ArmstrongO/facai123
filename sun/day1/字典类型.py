# 字典的类型和json非常相似。
# json 的最外层是 {键值对}  {"key":"value"}
# 字典就是这样定义的。
# 值可以是任何的数据类型。
name_dict = {
    "name": "老孙",
    "age": 18,
    "hobby": ["打篮球", "游泳", "打游戏", "上网冲浪"],
    "sex": {
        "s1": "男",
        "s2": "女"
    }
}

# 定义一个字典，字典中有四个key  分别是姓名  年龄  家庭住址，爱好
# 爱好需要对应多个，家庭住址，可以把上海的老家的，或者随便定义一个地方做成字典的形式。 城市名: 具体地址
info = {
    "name": "小孙",
    "age": 18,
    "hobby": ["s", "x", "y"],
    "address": {
        "city_name1": "上海虹口",
        "city_name2": "辽宁沈阳"
    }
}
# 快速格式化代码： ctrl + alt + l


# 字典中取值怎么取？ 原则还是通过名字来获取值
# print(name_dict["age"])

# 将年龄修改成48
# name_dict["age"] = 48
# print(name_dict)

# 字符串能不能替换？ 字符串不能替换，如果想要更改内容，重新赋值即可。
# name = "fanmaoxueyuan"
# name = "fanxaoxueyuan"
# print(name)


# 现有列表
list1 = [
    "abc", "2", 2, "txt", [
        "2xy", {
            "name": "xs",
            "age": 58
        },
        "nice"
        ,
        ["fnq","2xn"]
    ],
    "nf",
    "red"
]
# 将列表中int类型数字取出求和
# 将txt取出，统计里面有几个t元素
# 从列表中取出元素，形成一个文件名"nice.txt"
# 2xy和2xn判断他们是否相等

