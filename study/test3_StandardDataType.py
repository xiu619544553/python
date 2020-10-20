
'''
参考链接：https://www.runoob.com/python/python-variable-types.html
'''

'''
Python 标准数据类型

在内存中存储的数据可以有多种类型。
Python 定义了一些标准类型，用于存储各种类型的数据。


Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）


Python支持四种不同的数字类型：
int（有符号整型）—— 比如：10、-8
long（长整型，也可以代表八进制和十六进制），Python使用 L 来显示长整型，比如 122L、0xDEFABC、-90L
float（浮点型）。—— 比如：0.0、15.20、70.2E-12、-90.
complex（复数）。—— 比如：45.j、.876j。Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

注意：long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。
'''


'''
Python 数字

数字数据类型用于存储数值。
他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
当你指定一个值时，Number 对象就会被创建：
'''
var1 = 2
var2 = 3
var3 = 20
print(var1)
# 使用 del语句删除一些对象的引用
del var1
del var2, var3
# var2已被删除，在引用就会报错
# print(var2)


'''
Python字符串

字符串或串(String)是由数字、字母、下划线组成的一串字符。

python的字串列表有2种取值顺序:
①从左到右索引默认0开始的，最大范围是字符串长度少1
②从右到左索引默认-1开始的，最大范围是字符串开头

如下，2种取值顺序：
R   U  N  O  O  B
0   1  2  3  4  5  -->  从左到右索引默认0开始的
-6 -5 -4 -3 -2 -1  -->  从右到左索引默认-1开始的
'''
print('...字符串...')
s = 'abcdef'

# [头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符
# 当使用以冒号分隔的字符串，python 返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界
print("s[1:5] = " + s[1:5])
# 下标可以为空表示取到头或尾
print("s[1:] = " + s[1:])  # 尾下标为空，表示从下标1取到尾
print("s[:2] = " + s[:2])  # 头下标为空，表示从下标 (2-1)位置取到头

# [下标]
print("s[5] = " + s[5])
print("s[-1] = " + s[-1])

print("字符串截取")
print("s = " + s)            # 输出完整字符串
print("s[0] = " + s[0])      # 输出字符串中的第一个字符串
print("s[2:5] = " + s[2:5])  # 输出字符串中的第3个至第5个字符串
print("s[2:] = " + s[2:])    # 输出从第3个到最后一个字符串
print("s * 2 = " + s * 2)    # 输出字符串两次
print(s + "TEST")            # + 输出连接的字符串

# Python 列表截取可以接收第三个参数，参数作用是截取的步长
print("步长")
# 步长为2，表示间隔一个位置来截取字符串
print(s[1:4:2])


'''
Python列表

List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
'''
print('Python列表')
l = ['a', 'b', 'c', 'd', 'e']
print(l)
print(l[1:3])
print(l[:4])
print(l[3:])
print(l[:])
# 加号 + 是列表连接运算符，星号 * 是重复操作
print(l * 2)
l2 = ['o', 'p', 'q']
print(l + l2)


'''
Python 元组

元组是另一个数据类型，类似于 List（列表）。
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
'''
print('Python 元组')
tuple = ('Alex', 'Bob', 2.9, 10, -9)
tinytuple = (666, 'john')

print(tuple)       # 输出完整元组
print(tuple[0])    # 输出元组的第一个元素
print(tuple[1:3])  # 输出元组第一个元素到第3个元素(不包含)
print(tuple[2:])   # 输出元组从第二个元素到最后
print(tuple[:5])   # 输出元素第5个元素(不包含)到头
print(tuple * 2)  # 输出元组2次
print(tuple + tinytuple) # 打印组合元组


'''
Python 字典

字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
print('Python 字典')

dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

tinydict = {'name': 'Tank', 'code': 200, 'msg': 'success'}

print(dict)      # 输出完整字典
print(dict['one'])
print(dict[2])
print(tinydict)  # 输出完整字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


'''
Python数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值
'''
print('Python数据类型转换')
print(int())

str = "RUNLOOP"
print(str)
print(repr(str))
print(repr(dict))









