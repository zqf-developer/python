"""
列表生成式
Author:轻风
Version:v1
"""


# 字符串返回大写字母
def to_uppers(l):
    return [i.upper() for i in l if isinstance(i, str)]


print(to_uppers(['hello', 'world', 101]))

# 生成列表
list_para = list(range(1, 11))
print(list_para)

print([x * x for x in range(1, 11)])

# 复杂表达式
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.items()]
print('<table>')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')

# 条件过滤
result = [x * x for x in range(1, 11) if x % 2 == 0]
print(result)

# 多层表达式
result2 = [m + n for m in 'ABC' for n in '123']
print(result2)

result3 = [i * 100 + j * 10 + k
           for i in range(1, 10)
           for j in range(10)
           for k in range(10) if i == k]
print(result3)


