# 学生管理系统
# 用python实现学员的信息的增删改查。
# 所有的学员信息用一个列表保存， 用户可以输入学员的id，姓名，年龄，
# 新增之后，用户可以查询到已经新增过的学员的信息
# 编辑，当用户输入想要编辑的学员id，先进行查询，如果查询到了，则让用户输入新的姓名，年龄。查询不到输出，该学员不存在
# 删除，先输出需要删除的学生学号，存在则删除，不存在则输出该学员不存在

students = []  # 定义一个最终保存学生的列表
def add_student():
    id = input("请输入id：")
    for stu in students:
        if stu["ID"] == id:
            print ( "学生id输入重复，系统退回主界面" )
            return   # 结束函数
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    students_info = {
        "ID" : id,
        "Name" :name,
        "Age":age
    }
    students.append(students_info)

def search_student():
    id = input("请输入需要查询的学员id:")
    for stu in students:
        if stu["ID"] == id:
            print(stu)
            return   # 结束函数
    print("查无此人")

def delete_student():
    id = input("输入id删除: ")
    for stu in students:
        if stu["ID"] == id:
            students.remove(stu)
            print("学生删除成功!")
            return
            # break
    print("没有找到信息.退回主页")

def edit_student():
    id=input("输入id修改: ")
    for stu in students:
        if stu["ID"] == id:
            name = input("输入新的姓名: ")
            age = input("输入新的年龄: ")
            stu["Age"] = age
            stu["Name"] = name
            print ( "修改信息成功!" )
            return
    print("没有找到信息.退回主页")

def admin():
    print ( students )

while 1:
    print("欢迎来带学生管理系统，请输入您要办理的业务：")
    number = input("\n1.新增学生   \n2.查询学生   \n3.修改学生   \n4.删除学生   \n5.退出 \n6.管理员后台")
    if number == "1":
        add_student()
    elif number == "2":
        search_student()
    elif number == "3":
        edit_student()
    elif number == "4":
        delete_student()
    elif number == "5":
        break
    elif number == "6":
        admin()
    else:
        pass











# while True:
#     print ( "\n1.增加学生信息""\n2.搜索学生信息""\n3.修改学生信息""\n4.删除学生""\n5.退出")
#     choice = input ( "请选择: " )
#     if choice == "1":
#         add_student ()
#     elif choice == "2":
#         view_students()
#     elif choice == "3":
#         edit_student()
#     elif choice == "4":
#         delete_student()
#     elif choice == "5":
#         break
#     else:
#         pass










# def add_student():
# #     id = input("请输入学员id:")
# #     name = input("请输入学员姓名:")
# #     age = input("请输入学员年龄:")
# #     # 将学生信息存入到字典中
# #     student_info = {
# #         "ID": id,
# #         "Name": name,
# #         "Age": age
# #     }
# #     students.append(student_info)
# #     print(students)
# while True:
#
#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         view_students()
#     elif choice == "3":
#         delete_student()
#     elif choice == "4":
#         edit_student()
#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice. Please try again.")



