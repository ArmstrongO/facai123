
# name = input("请输入用户名")
# if name == "admin":
#     passwd = input("请输入密码")
#     if passwd == "123456":
#         print("欢迎光临")
#     else:
#         print("密码错误")
# else:
#     print("该用户不存在")
# if passwd == "123456":
#     if name == "admin":
#         print("欢迎光临")
#     else:
#         print("该用户不存在")
# else:
#     print("密码错误")
# 用input输入三个数字的值，判断这个三个值能否形成一个三角形
# # 如果能，判断出这是什么三角形？
# angle1 = input("请输入角度")
# angle2 = input("请输入角度")
# angle3 = input("请输入角度")
# angle1 = int(angle1)
# angle2 = int(angle2)
# angle3 = int(angle3)
# value = angle3+angle2+angle1

a=int(input("第一个边"))
b=int(input("第二个边"))
c=int(input("第三个边"))
# 等边，直角，等腰，等腰直角，其他三角
if a+b>c and a+c>b and b+c> a:
    if  a==b==c:
        print("等边三角形")
    elif a==b or a==c or b==c:
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print("等腰直角三角形")
        else:
            print("等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("直角三角形")
    else:
        print("其他三角形")
else:
    print("不是一个三角形")

