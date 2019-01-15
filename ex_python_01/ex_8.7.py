def make_album(singer_name, album_name, sing_qty=10):
    music_album = {'singer': singer_name.title(),
                   'album': album_name.title(),
                   'sing_qty': sing_qty}
    print(music_album)
    return music_album


while True:
    print("\nPlease tell me album name:")
    print("(enter 'q' at any time to quit)")

    s_name = input("singer name: ")
    if s_name == 'q':
        break

    a_name = input("album name: ")
    if a_name == 'q':
        break
    """这个调用函数必须写在里面才能看到正常结果"""
    singer_album = make_album(s_name, a_name)


# singer_album_01 = make_album('zhoujielun', 'daohuaxiang', '20')
# print(singer_album_01)
#
# singer_album_02 = make_album('heye', 'tianliangyiqian')
# print(singer_album_02)
#
# singer_album_03 = make_album('shenyicheng', 'chun')
# print(singer_album_03)
