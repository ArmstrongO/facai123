# 学生管理系统
# 用python实现学员的信息的增删改查。
# 所有的学员信息用一个列表保存， 用户可以输入学员的id，姓名，年龄，
# 新增之后，用户可以查询到已经新增过的学员的信息,如果没查到，输出查无此人
# 编辑，当用户输入想要编辑的学员id，先进行查询，如果查询到了，则让用户输入新的姓名，年龄。查询不到输出，该学员不存在
# 删除，先输出需要删除的学生学号，存在则删除，不存在则输出该学员不存在

students = []  # 定义一个最终保存学生的列表


# 新增学生
def add_student():
    id = input("请输入学员id:")
    name = input("请输入学员姓名:")
    age = input("请输入学员年龄:")
    # 将学生信息存入到字典中
    student_info = {
        "ID": id,
        "Name": name,
        "Age": age
    }
    students.append(student_info)
    print(students)


# 查询学生
def search_student():
    id = input("请输入需要查询的学员id:")
    for stu in students:
        if stu["ID"] == id:
            print(stu)
            return   # 结束函数
    print("查无此人")


while True:
    print("欢迎来带学生管理系统，请输入您要办理的业务：")
    number = input("1.新增学生   2.查询学生   3.修改学生   4.删除学生   5.退出")
    if number == "1":
        add_student()
    elif number == "2":
        search_student()