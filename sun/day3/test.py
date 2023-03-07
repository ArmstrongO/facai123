students = []

# 新增学生

id = input("请输入学生学号:")
name = input("请输入学生姓名:")
age = input("请输入学生年龄:")
student_info = {
    "Id": id,
    "Name": name,
    "Age": age
}
students.append(student_info)
print(students)
