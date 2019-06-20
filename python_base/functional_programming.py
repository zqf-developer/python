from functools import reduce
import math


# 高阶函数
def add(x, y, fun1):
    return f(x) + fun1(y)


# map()函数 返回一个新的list
def f(x):
    return x * x


# 差函数
def diff(x, y):
    return x - y


# 求和
def sum_two(x, y):
    return x + y


# 判断奇数函数
def is_odd(x):
    return x % 2 == 1


# 删除None或者空字符串
# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
def is_not_empty(s):
    return s and len(s.strip()) > 0


# 是否为平方数
def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x


# 返回函数，延迟计算
# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum


# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def fun(j):
            def g():
                return j * j
            return g
        r = fun(i)
        fs.append(r)
    return fs


print(add(4, -5, abs))
# map()函数
map_list = list(
    map(diff, [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 1, 5, 8, 0, 1, 9]))
print(map_list)
# reduce()还可以接收第3个可选参数，作为计算的初始值
total = reduce(sum_two, [2, 3, 5, 13, 12], 100)
print(total)
# filter()函数
result = list(filter(is_odd, [1, 3, 5, 8, 10]))
result2 = list(filter(is_not_empty, ['test', None, '', 'str', 'END']))
print(result2)
print(result)
print(type(filter(is_odd, [1, 3, 5, 8, 10])))
# sum可以计算列表，元组，字典的value值，
sum_total = sum({'sss': 12, 'kkk': 13}.values())
print(sum_total)

result3 = list(filter(is_sqr, range(1, 101)))
print(result3)
print(sorted(result3, reverse=True))  # 临时排序

fun2 = calc_sum(result3)
print(fun2)
print(fun2())
f1, f2, f3 = count()  # 初始化
print(f1(), f2(), f3())

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8])))  # 匿名函数



