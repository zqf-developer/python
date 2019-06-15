"""
set
dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。

有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。

set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

创建 set 的方式是调用set()并传入一个list，list的元素将作为set的元素

打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。

set的特点
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

最后，set存储的元素也是没有顺序的。
Author:轻风
Version:v1
"""

s = set(['A', 'B', 'C', 'C', 'c'])
print(s)
print(len(s))
s.add('D')  # 添加元素，存在的添加不会报错
print(s)
if 'c' in s:
    s.remove('c')  # 删除不存在的元素会报错
    print(s)
# s.remove('ss')
# try:
#     s.remove('ss')
# except KeyError as e:
#     print(e)

# 自动去重
for para in s:
    print(para)

print(help(abs))
