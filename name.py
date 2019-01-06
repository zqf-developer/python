# -*- coding:UTF-8 -*-
#使用方法修改字符串的大小
name = "ada lovelace"
name_dif = "ADA lovelace"
print(name.title())
print(name_dif.title())
print(name.upper())
print(name.lower())

# \n 是换行符 \t 制表符 可以一起使用
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "\nHello, "+full_name.title()+"!"
print(message)

more_message = "\nLanguages:\n\tPython\n\tC\n\tJavaScript"
print(more_message)

# 删除空白 rstrip() 删除末尾空格，lstrip() 删除开头空格 strip() 删除两端空格
favorite_languge = ' python '
print(favorite_languge)
favorite_languge = favorite_languge.rstrip()
print(favorite_languge)
favorite_languge = favorite_languge.lstrip()
print(favorite_languge)



