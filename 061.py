# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:29:29 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:28:57 2018

@author: User
"""

#使用pandas套件讀寫excel檔案, ref:E_7_12.py
import csv
import pandas as pd
from pandas import ExcelWriter
PM=[0,0,0,0,0,0,0,0,0,0,0,0]
CO=[0,0,0,0,0,0,0,0,0,0,0,0]
SO2=[0,0,0,0,0,0,0,0,0,0,0,0]
Days=[31,29,31,30,31,30,31,31,30,31,30,31]

f = open('105_XiTun.csv', 'r')
for row in csv.DictReader(f):
    if row['日期']>="2016/1/1" and row['日期']<="2016/1/31":
             moon=1
    if row['日期']>="2016/2/1" and row['日期']<="2016/2/29":
             moon=2
    if row['日期']>="2016/3/1" and row['日期']<="2016/3/31":
             moon=3
    if row['日期']>="2016/4/1" and row['日期']<="2016/4/30":
             moon=4
    if row['日期']>="2016/5/1" and row['日期']<="2016/5/31":
             moon=5
    if row['日期']>="2016/6/1" and row['日期']<="2016/6/30":
             moon=6
    if row['日期']>="2016/7/1" and row['日期']<="2016/7/31":
             moon=7
    if row['日期']>="2016/8/1" and row['日期']<="2016/8/31":
             moon=8
    if row['日期']>="2016/9/1" and row['日期']<="2016/9/30":
             moon=9
    if row['日期']>="2016/10/1" and row['日期']<="2016/10/31":
             moon=10
    if row['日期']>="2016/11/1" and row['日期']<="2016/11/30":
             moon=11
    if row['日期']>="2016/12/1" and row['日期']<="2016/12/31":
             moon=12
    if row['測項']=='PM2.5':
        
             s1=row['9'].replace("x","")
             s1=s1.replace("#","")    
             if s1!='':
                 PM[moon-1]+=float(s1)   
    if row['測項']=='CO':
        s1=row['9'].replace("x","")
        s1=s1.replace("#","")    
        if s1!='':
            CO[moon-1]+=float(s1)
    if row['測項']=='SO2':
        s1=row['9'].replace("x","")
        s1=s1.replace("#","")    
        if s1!='':
            SO2[moon-1]+=float(s1)  
                        
        #print(PM)
for i in range(0,12):
    PM[i]/=Days[i]
    PM[i]=round(PM[i],5)
    CO[i]/=Days[i]
    CO[i]=round(CO[i],5)
    SO2[i]/=Days[i]
    SO2[i]=round(SO2[i],5)
    
print(PM,CO,SO2)   
indexs=["PM2.5","CO","SO2"] 
cloumns=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]   
datas=[PM,CO,SO2]
df=pd.DataFrame(datas,columns=cloumns,index=indexs)
print(df)
f.close()
#開啟要寫入的檔案以及工作表
writer = ExcelWriter('105_XiTun.xlsx')
df.to_excel(writer,'105_XiTun')
workbook = writer.book
worksheet = writer.sheets['105_XiTun']

#畫折線圖
chart = workbook.add_chart({'type': 'line'})
chart.add_series({'name': '=105_XiTun!$A$2','categories': '=105_XiTun!$B$1:$M$1',
'values': '=105_XiTun!$B$2:$M$2'})
chart.add_series({'name': '=105_XiTun!$A$3','categories': '=105_XiTun!$B$1:$M$1',
'values': '=105_XiTun!$B$3:$M$3'})
chart.add_series({'name': '=105_XiTun!$A$3','categories': '=105_XiTun!$B$1:$M$1',
'values': '=105_XiTun!$B$4:$M$4'})

chart.set_x_axis({'name': '月份'})
chart.set_y_axis({'name': 'Stock Value', 'major_gridlines': {'visible': False}})
chart.set_legend({'position': 'top'})
worksheet.insert_chart('A8: J25', chart)
writer.save()

"""
df=pd.read_csv('105_XiTun.csv',encoding='big5')
df1=pd.DataFrame(df)
print(df1)
print(df1.loc[:,"9"])
"""
    
    
