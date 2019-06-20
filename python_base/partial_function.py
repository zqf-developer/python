import functools


print(int('1234', 8))
# functools.partial可以把一个参数多的函数变成一个参数少的新函数
int2 = functools.partial(int, base=2)
print(int2('1010101'))
