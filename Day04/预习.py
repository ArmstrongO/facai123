# 这个程序使用一个名为students的列表来存储代表每个学生的字典。add_student()函数提示用户输入学生的姓名、年龄和年级，用这些信息创建一个字典，并将其添加到学生列表中。view_students函数只是循环遍历列表并打印出每个学生的信息。delete_student函数提示用户删除一个学生名，在学生列表中搜索匹配的名字，如果找到，则删除相应的字典。edit_student)函数提示用户输入要编辑的学生姓名，在学生列表中搜索匹配的姓名，并提示用户输入新的年龄和年级值以更新相应的字典。最后，程序使用while循环来重复显示选项菜单，并根据用户的选择调用相应的函数。
# This program uses a list called `students` to store dictionaries representing each student. The `add_student()` function prompts the user for the student's name, age, and grade, creates a dictionary with this information, and adds it to the `students` list. The `view_students()` function simply loops through the list and prints out each student's information. The `delete_student()` function prompts the user for a student name to delete, searches the `students` list for a matching name, and removes the corresponding dictionary if found. The `edit_student()` function prompts the user for a student name to edit, searches the `students` list for a matching name, and prompts the user for new age and grade values to update the corresponding dictionary. Finally, the program uses a `while` loop to repeatedly display a menu of options and call the appropriate function based on the user's choice.

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print("Student added successfully!")

def view_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student["name"] == "name":
            students.remove(student)
            print("Student deleted successfully!")
            return
            # break
        print("Student not found.")

def edit_student():
    name = input("Enter student name to edit: ")
    for student in students:
        if student["name"] == "name":
            age = input("Enter new age: ")
            grade = input("Enter new grade: ")
            student["age"] = age
            student["grade"] = grade
            print("Student edited successfully!")
            return
        print("Student not found.")

while True:
    print("\n1. Add student\n2. View students\n3. Delete student\n4. Edit student\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        break
    else:
        print(" Please try again.")