# sort 排序永久
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# sorted 临时排序 reverse = True 你顺序排序相反的排序
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the reverse of true list:")
print(sorted(cars,reverse = True))

# reverse() 倒着打印
cars.reverse()

print("\nHere is the reverse list:")
print(cars)

print("\nHere is the original list")
cars.reverse()
print(cars)  # 不能直接写在print里面

print("\nHere is the length of list:")
print(len(cars))



