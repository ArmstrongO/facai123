


import random
# def chouka():
with open(file="puke.txt",encoding="utf8") as f:
    lines = f.readlines()
    for sou in lines:
        if sou =='[花色：红桃 点数：10]\n':
            print ( sou )
        else:
            pass



        # sou = str(sou)
        # if sou[2] =="Small_Joker ":
        #     return  lines
    # random_line1=f"{(random_line)}"
    # return random_line1
    # print(type(random_list))

# print(chouka())
#
# def s_s():
#     id = input("请输入需要查询的学员id:")
#     for stu in students:
#         if stu["ID"] == id:
#             print(stu)
#             return   # 结束函数
#     print("查无此人")