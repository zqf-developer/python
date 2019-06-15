"""
字典{key:value}
dict的特点
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。

不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。

由于dict是按 key 查找，所以，在一个dict中，key不能重复。
dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样
dict的第三个特点是作为key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key
Author:轻风
Version:v1
"""

d = {
    'Adam': 100,
    'Lisa': 80,
    'Bart': 99
}

print(d)
print(d['Lisa'])
print(d.get('Bart'))
print(d.get('ss'))

# d1 = {
#     ['1', '3']: '13'
# }
# print(d1)
d2 = {
    ('1', '3'): '13'
}
print(d2)