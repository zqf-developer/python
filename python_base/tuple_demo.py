"""
tuple：
1. 是另一种有序的列表，中文翻译为“ 元组 ”。
2. tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。

Author:轻风
Version:v1
"""

t = ('Adam', 'Lisa', 'Bart', ['Family', 'Country'])
t1 = ()  # 空元组
print(type(t1))
t2 = (1)  # 这个是个整型而不是一个单元组
t3 = (1,)  # 后面加个逗号才表示一个单元组
print(type(t2))
print(type(t3))
try:
    # t[0] = 'KK'
    l = t[3]
    l[0] = 'Friend'
    l[1] = 'City'  # list元素可以变，但tuple元素不可变
except TypeError as e:
    print(e)
print(t)

for name in t:
    print(name)
    print('显示元组内容：' + str(name))  # 打印的时候列表无法跟字符一起输出,需要转换类型
