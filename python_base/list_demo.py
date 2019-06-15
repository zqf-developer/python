"""
列表：list
1. 是Python内置的一种数据类型
2. 是一种有序的集合
3. 可以随时添加和删除其中的元素
Author:轻风
Version:v1
"""
classmates = ['Adam', 'Luis', 'Luce', 'Sam']
print(classmates)
if classmates.__contains__('Peter'):
    classmates.remove('Peter')
else:
    print('Peter', '不存在！')
    classmates.append('Peter')

classmates.pop(1)  # 删除索引对应的值
classmates.insert(1, 'Kara')  # 对应索引的位置插入指定的值
print(classmates)

print(classmates[2])
classmates[2] = 'Paul'  # 替换指定位置的值
print(classmates)
print('')
print('2到结尾：', classmates[2:])  # 切片
print('开头到-2：', classmates[:-2])
print('-2到结尾：', classmates[-2:])
print('2到-2：', classmates[2:-2])
print('1到2：', classmates[1:2])  # 不包括1对应的值

for key, value in enumerate(classmates):
    while key > 2:
        print('第 ' + str(key + 1) + ' 个同学名字：' + value)
        break

total = 0.0
scores = [100, 78, 40, 35, 60, 77]
for key, score in enumerate(scores):
    if score < 60:
        continue
    total = total + score
print('大于60分总分：' + str(total))



