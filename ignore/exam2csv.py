# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:42:36 2018

@author: User
"""

import pandas as pd
tables = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")

table = tables.drop(tables.columns[3::],axis=1)
#table = table.drop(table.columns[4::],axis=1)
#table.columns =["SiteName","County","AQI","Pollutant"]
#print (table["AQI"][0])
maxad1=0
maxad2=0
maxad3=0
for i in range(0,len(table)):
    #把對敏感族群不健康 替換成 不良
    if table["AQI"][i]>table["AQI"][maxad1]:
        maxad1=i

for i in range(0,len(table)):
    if table["AQI"][i]>table["AQI"][maxad2] :
        if i!= maxad1:
            maxad2=i
for i in range(0,len(table)):
    if table["AQI"][i]>=table["AQI"][maxad2] :
        if i!= maxad1 and i!=maxad2:
            maxad3=i
            
print (table.iloc[maxad1, :])
print (table.iloc[maxad2, :])
print (table.iloc[maxad3, :])