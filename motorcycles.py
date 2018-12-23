motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表末尾添加元素
motorcycles.append('honda')
print(motorcycles)

# 插入元素
motorcycles.insert(0,'pandan')
print(motorcycles)

motorcycles.insert(3,'monkey')
print(motorcycles)

# 删除元素 永久删除不可访问了
del motorcycles[0]
print(motorcycles)

# del不能批量删除
# del motorcycles

# pop()删除元素 可以保存删除项，堆栈弹出逻辑
pop_all = [] # 存储被移除的元素

popped_motorcycle = motorcycles.pop()
pop_all.append(popped_motorcycle)
print(motorcycles)
print(popped_motorcycle + "\n")

last_owned = motorcycles.pop()
pop_all.append(last_owned)
print("The last motorcycle I owned was a " + last_owned.title() + ".\n")
print(pop_all)
print(motorcycles)

pop_second = motorcycles.pop(1) # pop(索引值)
pop_all.append(pop_second)
print(motorcycles)
print(pop_all)

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
# motorcycles.remove('honda','suzuki') 不能接受两个参数






