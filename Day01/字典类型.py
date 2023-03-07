# 定义一个字典，字典中有四个key  分别是姓名  年龄  家庭住址，爱好
# 爱好需要对应多个，家庭住址，可以把上海的老家的，或者随便定义一个地方做成字典的形式。 城市名: 具体地址
li_dic = {
    "name": "Lykke",
    "age": 44,
    "hobby": ["编程", "Java", "Python"],
    "home_addr": {
        "city_province": "上海市",
        "city_city": "上海市",
        "city_county": "虹口区"
    }
}

print ( li_dic )
