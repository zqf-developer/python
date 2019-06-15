#  与运算
print(True and True)
print(True and False)
print(False and False)

#  或运算
print('\n')
print(True or True)
print(True or False)
print(False or False)

#  非运算
print('\n')
print(not True)
print(not False)

#  短路计算
print('\n')
a = False
"""
下面输出的结果原因如下：
因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True，所以：

True and ‘a=T’ 计算结果是 ‘a=T’ 
继续计算 ‘a=T’ or ‘a=F’ 计算结果还是 ‘a=T’ 
要解释上述结果，又涉及到 and 和 or 运算的一条重要法则：短路计算。

在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。

在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。

所以Python解释器在做布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果。

"""
print(a and 'a=T' or 'a=F')  # 结果为a=T

