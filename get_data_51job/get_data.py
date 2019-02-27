import xlwt,re,urllib,requests


def get_data():

    for i in range(26700, 26716):
        url = 'http://www.risfond.com/case/fmcg/{}'.format(i)
        html = urllib.request.urlopen(url).read().decode('utf-8')
        print(html)
        result = re.findall(r'<div class="sc_d_c">.*?<span class="sc_d_con">(.*?)</span></div>', html)
        print(result)


get_data()
