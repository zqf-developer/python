"""
注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有key-value对：dict
而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。

"""

L = ['Adam', 'Lisa', 'Bart', 'Paul']
#   索引迭代
for index, name in enumerate(L):
        print(index, '-', name)

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
dvi = d.items()
print(dvi)
print(d.values())
lst = d.values()
print(type(lst))
print(type(d.__iter__()))  # 获取key值
print(type(d.items()))
# [85, 95, 59]
for v in d.items():
    print(v)
