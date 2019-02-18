def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        save_not_found_file(filename)
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        # pass #不提示用户任何消息
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


def save_not_found_file(not_file_name):
    """存储找不到文件的名字"""
    with open("missing_files.txt", 'w') as file_object:
        file_object.write(not_file_name)


filename = 'aaa.txt'
count_words(filename)
