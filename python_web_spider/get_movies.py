import urllib.request

from bs4 import BeautifulSoup

import pymysql


movielist = []
url = "https://movie.douban.com/top250"


def get_html(url):

    res = urllib.request.urlopen(url)

    html = res.read().decode()

    return html


def parse_html(html_file):

    mysoup = BeautifulSoup(html_file, 'html.parser')  # 解析html

    movie_zone = mysoup.find('ol')

    movie_list = movie_zone.find_all('li')

    for movie in movie_list:

        movie_name = movie.find('span', attrs={'class': 'title'}).getText()

        movielist.append(movie_name)

        next_page = mysoup.find('span', attrs={'class', 'next'}).find('a')

    if next_page:

        new_url = url + next_page['href']

        parse_html(get_html(new_url))  # 递归调用


def save_data(movielist):

    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test')

    mycursor = conn.cursor()

    # sql = 'CREATE TABLE movie(ID VARCHAR(10), name VARCHAR(30)) DEFAULT CHARSET=utf8'

    sql = ''

    for id, movie in enumerate(movielist):

        sql = "INSERT INTO movie values (%s,%s)"

        mycursor.execute(sql, (id+1, movie))

    conn.commit()

    mycursor.close()

    conn.close()


reshtml = get_html(url)
# print(reshtml)
parse_html(reshtml)
print(movielist)
save_data(movielist)
