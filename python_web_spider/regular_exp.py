import re

content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)  # 目标匹配
result = re.match('^Hello.*Demo$', content)  # 通用匹配
print(result)
print(result.group())
# print(result.group(1))  # 通用匹配不能使用这个方式
print(result.span())
# result = re.match('[a-zA-Z]+://[^\s]*', content)
# result_search = re.search('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())

# print(result_search)
# print(result_search.group(1))

