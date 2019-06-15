import math


# 返回多值
def move(xx, yy, step, angle):
    nx = xx + step * math.cos(angle)
    ny = yy - step * math.sin(angle)
    return nx, ny


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def move_thing(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move_thing(n-1, a, c, b)
    print(a, '-->', c)
    move_thing(n-1, b, a, c)


x, y = move(100, 100, 60, math.pi / 6)  # 返回多值就是一个tuple
print(x, y)
"""
如果我们计算fact(5)，可以根据函数定义看到计算过程如下：

===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120

递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试计算 fact(10000)。

"""
# print(fact(10000))

print(move_thing(3, 'A', 'B', 'C'))

