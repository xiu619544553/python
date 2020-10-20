

'''
Python 基础语法
'''

# Hello world
a = "Hello world"
print("Hello world!")
print(a)
print("你好！")

# Python3.x 与 Python2.x 的许多兼容性设计的功能可以通过 __future__ 这个包来导入。
# Python2.x 中使用 Python3.x 的 print 函数，导入 __future__
# 如果 Python2.x 版本想使用使用 Python3.x 的 print 函数，可以导入 __future__ 包，该包禁用 Python2.x 的 print 语句，采用 Python3.x 的 print 函数：
# from __future__ import print_function
list = ["A", "B", "C"]
print(list)


# Python 标识符
# 在 Python 里，标识符由字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
#
# Python 中的标识符是区分大小写的。
#
# 以下划线开头的标识符是有特殊意义的。
# 以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
#
# Python 可以同一行显示多条语句，方法是用分号 ; 分开，如：
print("1L"); print("2L")



# 行和缩进
# 学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。
# python 最具特色的就是用缩进来写模块。
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行，否则编译器会报错
if True:
    print("True")
else:
    print("False")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")



# 多行语句
# Python语句中一般以新行作为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
print("...多行语句...")
item_one = "One"
item_two = "Two"
item_three = "Three"
total = item_one + \
        item_two + \
        item_three
print(total)

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)


# Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子"
paragraph = '''这是一个段落。
包含了多个语句'''
print(word)
print(sentence)
print(paragraph)


# Python注释
# python中单行注释采用 # 开头。注释可以在语句或表达式行末
# 输出语句
print("单行注释")  # 输出语句

# python 中多行注释使用三个单引号(''')或三个双引号(""")
'''
这是一个语句，用于输出多行语句
'''
print('''《静夜思》
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
''')



# Python空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。



# 等待用户输入
# 下面的程序执行后就会等待用户输入，按回车键后就会退出
# 函数 input() 让程序暂停运行，等待用户输入一些文本，获取用户的输入后，Python将其存储到一个变量中，以方便后期使用。
name = input("输入你的名字：")
print(name)


# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
# 保存用户输入的内容
age = input("输入你的年龄：")
if int(age) >= 30:
    print("青壮年")
elif int(age) >= 18:
    print("青少年")
else:
    print("少年")
print("按 enter 退出")



# 命令行参数
# 很多程序可以执行一些操作来查看一些基本信息，Python 可以使用 -h 参数查看各参数帮助信息：



