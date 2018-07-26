
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:14:27 2018

@author: User
"""

import pandas as pd
tables = pd.read_html("https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.22851700%201523329374",encoding="big5")
#print (tables[0])
x=len(tables)
table = tables[x-3]
table = table.drop(table.index[0:1])
table = table.drop(table.columns[0:1],axis=1)
table = table.drop(table.columns[3:5],axis=1)
table = table.drop(table.columns[4:5],axis=1)
table = table.drop(table.columns[5:6],axis=1)
table = table.drop(table.columns[7::],axis=1)
#table = table.drop(table.columns[11::],axis=1)
#print(table[3][24])



for i in range(2,25):
    #昨收-成交=漲跌
    if (float(table[3][i])-float(table[8][i])<=0):
        #print (float(table[3][i])-float(table[8][i]))
        #table = table.drop(table.index[i],axis=1)
        table = table.drop(i,axis=0)
        
table = table.drop(table.columns[4:5],axis=1)  
table = table.drop(1,axis=0)
table.columns =["股票代號","時間","成交","漲跌","最高","最低"] 
result="not found"
for i in table.index:
    b=table.loc[i,"股票代號"].find("1300")
    if(b!=-1):
        print(table.loc[i,:])
        result=table.loc[i,:]
 
print(table)
print(result)
#△