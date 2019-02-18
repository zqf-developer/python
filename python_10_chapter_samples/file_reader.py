file_name = r'text_files\pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    # contents = file_object.read()
#     # print(contents.rstrip())
