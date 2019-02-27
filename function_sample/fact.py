def fact(n):
    """递归函数"""
    if n == 1:
        return 1
    return n*fact(n-1)


# 下面两个函数是解决递归调用栈溢出问题
def fact_new(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)


# print(fact(1))
# print(fact(5))
# print(fact(100))
# print(fact(1000))  # 递归调用栈溢出
print(fact_new(5))
