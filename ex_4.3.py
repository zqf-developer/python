for number in range(1,21):
	print(number)

numbers = []
for value in range(1,1000001):
	numbers.append(value)
	# print(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("以上为min、max和sum函数使用\n")
# 输出1到20的奇数
odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
	print(odd_number)
print("以上为奇数函数使用\n")
# 输出3到30内能被3整除的数字
double_numbers = list(range(3,31,3))
for double_number in double_numbers:
	print(double_number)
print("以上为倍数函数使用\n")	
# 立方
cube_numbers = []
for value in range(1,11):
	cube_number = value**3
	cube_numbers.append(cube_number)
	print(cube_number)
print("以上为立方函数使用\n")	

#列表解析
cube = [value**3 for value in range(1,11)]
print(cube)
print("以上为列表解析的使用\n")

