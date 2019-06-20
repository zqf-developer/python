"""
装饰器decorator
问题：
1. 定义了一个函数
2. 想在运行时动态增加功能
3. 又不想改动函数本身的代码

python内置的@语法就是为了简化装饰器的调用

装饰器的作用：
1. 可以极大地简化代码，避免每个函数编写重复性的代码
打印日志：@log
检测性能：@performance
数据库事务：@transaction
URL路由：@post（’/register’）

"""
from functools import reduce
import time
import functools


# 任意参数，打印日志 编写无参数decorator
def log(f):
    @functools.wraps(f)  # Python内置的functools可以用来自动化完成这个“复制”的任务
    def fn(*args, **kwargs):
        print('call ' + f.__name__ + '()...')
        return f(*args, **kwargs)
    return fn


# 编写带参数decorator
# 拆开以后会发现，调用会失败，因为在3层嵌套的decorator定义中，
# 最内层的wrapper引用了最外层的参数prefix，
# 所以，把一个闭包拆成普通的函数调用会比较困难。
# 不支持闭包的编程语言要实现同样的功能就需要更多的代码。
def log_with_para(prefix):
    def log_decorator(f):
        @functools.wraps(f)  # Python内置的functools可以用来自动化完成这个“复制”的任务
        def wrapper(*args, **kw):
            print('[%s] %s()...' % (prefix, f.__name__))
            return f(*args, **kw)
        return wrapper
    return log_decorator


# 编写无参数decorator
def performance(f):
    @functools.wraps(f)  # Python内置的functools可以用来自动化完成这个“复制”的任务
    def g(*args, **kwargs):
        t1 = time.time()
        r = f(*args, **kwargs)
        t2 = time.time()
        print('call%s() in %fs' % (f.__name__, t2-t1))
        return r
    return g


# 编写带参数decorator
def performance_with_para(unit):
    def perf_decorator(f):
        @functools.wraps(f)  # Python内置的functools可以用来自动化完成这个“复制”的任务
        def wrapper(*args, **kwargs):
            t1 = time.time()
            r = f(*args, **kwargs)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)  # 表达式
            print('call%s() in %f%s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator


@performance_with_para('ms')
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


@log
def add(x, y):
    return x + y


@log_with_para('DEBUG')
def test():
    pass


# print(test())
print(factorial.__name__)
# print(add(1, 2))

