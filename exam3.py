# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:07:37 2018

@author: User
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box04'})
#print(data2)
    
data3 = data2.find_all('div', {'class':'ball_tx'})
#print(data3)
#
# binggo彩號碼
print("三星彩：",end="")

print("開出獎號：",end="")
for n in range(0,3):
    print(data3[n].text,end="  ") 


## 第二區