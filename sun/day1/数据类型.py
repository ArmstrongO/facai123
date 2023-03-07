# 注释：python的注释   // java的注释
# 注释： 被注释的内容解释器看不到。被注释的内容不运行，是给自己作为代码的提示的。
# 快速注释多行： ctrl + /

# 什么是数据类型？
# python的数据类型都有哪些？
# python 的数据类型一共有八种
# 简单的： int 整数型   string 字符串   float 浮点型   boolean 布尔型 （对或者错）
# 复杂的： list 列表[]   set集合{}     tuple 元组()    dict 字典{}

# int类型  整数型
# 定义变量。 var res = res.response.json()
# number = 10  # 把10赋值给number   number是一个变量名，随便起。

# 算术运算 + - * / %
# num1 = 10
# num2 = 20
# print(num1 + num2)
# print() 打印  如果你想看到代码交互之后的结果，在控制台中显示出来，必须用print打印。

# 注意：
# 为了代码的规范性，在变量名和符号之间要空格
# 在编辑器中，一行代码只做一件事请，如果想再次定义变量必须换行。
# 在python中空格或者缩进代表层级关系，如果下面的代码不定格写说明他是上面的子集。

# %代表模  模： 取余数
# 思考：如果一个数字模2等于0，这个数是什么数？ 偶数
# num1 = 10
# num2 = 3
# print(num1 % num2)

# 比较运算 比较运算返回值是布尔类型  >  < >= <=   相等： ==  不等于： !=
# num1 = 10
# num2 = 20
# print(num1 != num2)


# 字符串 string
# 定义一个字符串 字符串必须加引号。 单引号 双引号， 无所谓。
# student_name = "老孙"
# info = "我的姓名是老孙，我喜欢看一本书叫做'《零基础学python从入门到放弃》'"
# 如果一个字符串里面同时存在这个多个引号，必须双印嵌套单引，或者单引嵌套双印。

# 有一种情况int类型和string都可以完成。
# student1 = "老孙"
# student2 = "老赵"
# student1 += student2  # student1 = student1 + student2
# print(student1)
#
# num1 = 10
# num2 = 15
# num1 += num2 # num1 = num1 + num2
# print(num1)
#
# obj1 = "老孙"
# obj2 = "80"
# obj1 += obj2
# print(obj1)
# TypeError: can only concatenate str (not "int") to str
# # 只能用字符串和字符串进行拼接，不能是int类型。

# 定义五个变量，分别是 姓名，书名，作者，销量，朋友
# 形成一句话 "我叫：XXXX，我今天买了一本叫:XXX的书，这本书的作者是:xxxx.这本书今年一共销售了:XXX，我会把他推荐给我的朋友XXX去看"
# print("我叫：" + obj1 + )

# name = "老孙"
# book_name = "《西游记》"
# author = "吴承恩"  # string
# sales = 10000  # int
# friend = "老赵"
# print("我叫：" + name + "我今天买了一本叫：" + book_name + "的书，这本书的作者是：" + author + "这本书一共销售了：" + str(sales) + "我会把他推荐给我的朋友" + friend +"去看")
# 1. 强转 强转就是强行转换数据类型。
# 把int类型强行转换成str  str(sales)  强行转换成int   int(变量名)  # type() 查看当前的对象是什么数据类型
# number = "108m"
# print(int(number))

# 2. 第二种拼接的方式是我们最为推荐也是最常用的。
# print(f"我叫：{name}，我今天买了一本叫：{book_name}的书，这本书的作者是：{author}，这本书一共销售了：{sales}，我把他推荐给我的朋友：{friend}去看")
# print(f"xxx{}xxxx{}xxxx{}")

# 字符串的切片和取值
# 字符串取值的原则也是通过索引来获取，只不过python中索引可以从前往后，也可以从后往前。
# 如果索引是从后往前数，那么从-1开始， 从前往后是从0开始。
info = "fanmaoxueyuan"
# 我想要获取info中的m     # print(变量名[索引])
# print(info[-4])
# 我想从m取到y  字符串的切片。
# print(info[3:-3])
# 字符串的切片的原则  print(变量名[start:end])  左闭右开。  闭区间就是包括边界值，开区间不包括。
# print(info[3:-1])  # 默认是从头开始，也就是0
# print(info[:])

# 从info的第一到第五位
print(info[:5])
# 从头到倒数第三位
print(info[:-2])
# 取mao
print(info[3:6])
# 从倒数第四位取到最后
print(info[-4:])
# 从第五位到y
print(info[4:-3])













