from program import np, dl, book_add, inquire, revamp, del_book,info
while True:
    print("欢迎来到图书管理系统，请选择您要办理的业务：\n1.注册\n2.登录\n3.退出")
    yw = input("请输入您要办理的业务:")
    if yw == "1":
        np()
        print(info)
    elif yw == "3":
        break
    elif yw == "2":
        if dl() == "成功":
            while True:
                print("请选择您要办理的业务:\n1.新增图书\n2.查询图书\n3.修改信息\n4.删除信息\n5.退出")
                byw = input("请输入您要办理的业务")
                if byw == "1":
                    book_add()
                elif byw == "2":
                    inquire()
                elif byw == "3":
                    revamp()
                elif byw == "4":
                    del_book()
                elif byw == "5":
                    print("账户已退出")
                    break
                else:
                    print("输入的内容不合法")
            break
