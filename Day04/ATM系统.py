

ppp = 3
info =1
while True:
    name = input("请输入名字: ")
    if name != "admin":
        if name != "admin":
            print("用户不存在")
            break
        else:
            print("密码输入错误，请重新输入")
        break
    else:
        passwd = input("请输入密码: ")
        if passwd == "888888":
            while info<3:
                print("欢迎光临,请选择需要办理的业务")
                info = int(input("1.取款 2.存款 3.退出"))
                if info ==2:
                    print ( "选项为2" )
                elif info == 1:
                    print ( "选项为1" )
                else :
                    print("感谢使用！再见")
                # break
            break
        else:
            print("密码错误，请重新输入")
            if ppp < 2:
                print("密码超过3次，系统冻结")
                break
            else:
                ppp -= 1
                print ("当前可输入次数"+str(ppp))








