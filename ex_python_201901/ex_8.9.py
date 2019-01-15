def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())


def make_great(magicians_modify):
    """
    调用这个方法会返回修改后的列表，下面方法是百度出来的 for
    :param magicians_modify:
    :return:
    """
    for i in range(len(magicians_modify)):
        magicians_modify[i] = "the Great " + magicians_modify[i]
    return magicians_modify


def make_great_default(magicians_now, magicians_modified):
    """使用while循环赋值"""
    while magicians_now:
        current_magician = "the Great " + magicians.pop()
        magicians_modified.append(current_magician)


magicians = ['jack', 'amy', 'helen']
modify_magicians = []
make_great_default(magicians, modify_magicians)
show_magicians(modify_magicians)

# magicians_change = make_great(magicians[:])
# show_magicians(magicians)
# show_magicians(magicians_change)





