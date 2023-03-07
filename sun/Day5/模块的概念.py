# 模块的概念
# 包就是python的结构中的目录。
# 每个包下面都有很多模块  模块就是以.py结尾的python文件。

# 因为在python中，每个包和模块都可以在另外的模块中互相导入使用。
# 导入的关键字有两个  一个是：from    一个是：import
# 包刚刚导入的时候是置灰显示的，因为该函数还没有被当前模块使用到。当你用到了，就亮了。

# 第一种导包的方式
# from 包名.模块名 import 函数名
# from Day04.student_program import deleteStudent, addStudent, search_student, updateStudent

# 第二种导包的方式
# import 包名.模块名 as 别名
import Day04.student_program as sp

print("""
欢迎登录学生管理系统：
1. 新增学生；
2. 查看学生；
3. 修改学生；
4. 删除学生；
5. 退出
""")

while True:
    n = input("请输入指令：")
    if n == "1":
        sp.addStudent()
    elif n == "2":
        sp.search_student()
    elif n == "3":
        sp.updateStudent()
    elif n == "4":
        sp.deleteStudent()   # 快速导包  alt + enter
    elif n == "5":
        break
    else:
        print("您输入的指令不存在，请重新输入")

# 明天我们需要用到一个库叫做：requests
# requests这个库不是python自带的，而是第三方提供的库。
# 如果你需要引入第三方的库，必须先安装它。

















