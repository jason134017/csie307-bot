# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:08:26 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:36:05 2018

@author: User
"""
import requests,re

url = 'https://www.caac.ccu.edu.tw/CacLink/apply107/107apply_Sieve_pg58e3q/html_sieve_107yaya/ColPost/common/apply/' 
name=['交大資工資工程組','清大資工資工程組','成大資工']
school=['013092','011352','004392']
"""
def APCS(url):
    html = requests.get(url)
    regex=re.compile('[0-9]{8}') # 連續8位數字(準考證號碼)
    data=regex.findall(html.text)
    for i in range(0,len(data)):
       print(data[i],end=' ')
    print()
"""
data1=list()
data2=list()
data3=list()
for i in range(0,3):
     
    nurl=url+school[i]+'.htm'
    html = requests.get(nurl)
    regex=re.compile('[0-9]{8}') # 連續8位數字(準考證號碼)
    data=regex.findall(html.text)
    for j in range(0,len(data)):
       if i==0:
           data1.append(data[j])
       if i==1:
           data2.append(data[j])
       if i==2:
           data3.append(data[j])    
    """  
    for k in range(0,len(data1)):
       print(data1[i],end=' ')
    """
    print()
result=list()
for j in range(0,len(data1)):
       for k in range(0,len(data2)):
           if data1[j] == data2[k]:
               for l in range(0,len(data3)):
                   if data3[l] == data2[k]:
                       result.append(data3[l])
               
print (result)
        