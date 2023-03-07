# -*- coding: utf-8 -*-



import Day04.学生管理系统 as st
from Day04.学生管理系统 import add_student,search_student,edit_student,delete_student,admin
import time

print(str(time.time() * 1000))


while 1:
    print("欢迎来带学生管理系统，请输入您要办理的业务：")
    number = input("\n1.新增学生   \n2.查询学生   \n3.修改学生   \n4.删除学生   \n5.退出 \n6.管理员后台")
    if number == "1":
        st.add_student()
    elif number == "2":
        st.search_student()
    elif number == "3":
        st.edit_student()
    elif number == "4":
        st.delete_student()
    elif number == "5":
        break
    elif number == "6":
        st.admin()
    else:
        pass
