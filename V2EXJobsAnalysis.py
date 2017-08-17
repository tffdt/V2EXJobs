#-*- coding:utf-8 -*-
#author:Zoey
#Updatatime:2017/8/16 0016
#Function:


import re
import os
import time
import jieba
import requests
from bs4 import BeautifulSoup

multilist = [[0 for col in range(100)] for row in range(2000)]

def show_res():
    pass

def analyse_infofpage(page_inf):
    pass

def get_infofpage(page_num):
    try:
        page_url = 'https://www.v2ex.com/go/jobs?p=' + str(page_num)
        r = requests.get(page_url).text
        soupObj = BeautifulSoup(r, 'html.parser')
        jobinf = soupObj.findAll('span')
        cnt = 0
        for span in jobinf:
            spanpattern = re.compile(r'<a href=')
            strspan = str(span.contents)
            searchresult = spanpattern.search(strspan)#
            if searchresult:
                multilist[page_num][cnt] = span.text
                cnt = cnt + 1
        print (page_num)
    except:
        print(u'获取' + str(page_num) + u'页信息失败')

def get_numberofpage(main_url):
    try:
        r = requests.get(main_url).text
        soupObj = BeautifulSoup(r, 'html.parser')
        page_num = soupObj.find('input', attrs={max}).attrs['max']
        return page_num
    except:
        print(u"获取页面个数出错")
        os._exit()


if __name__ == '__main__':
    main_url = 'https://www.v2ex.com/go/jobs'
    page_num = get_numberofpage(main_url)
    print (u'共找到' + str(page_num) + u'页招聘信息')
    for num in range(1, 2):   # int(page_num)
        get_infofpage(num)
        time.sleep(1)