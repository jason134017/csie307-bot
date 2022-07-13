# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:06:47 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:37:30 2018

@author: CSIE
"""


import pandas as pd
tables = pd.read_html("https://opendata.epa.gov.tw/Data/Contents/AQI/")
x=len(tables)
table = tables[x-1]
table = table.drop(table.columns[3:4],axis=1)
table = table.drop(table.columns[4::],axis=1)
table.columns =["SiteName","County","AQI","Pollutant"]
#print (table["AQI"][0])

maxad1=0
maxad2=0
maxad3=0
for i in range(0,len(table)):
    #把對敏感族群不健康 替換成 不良
    if table["AQI"][i]>=101:
        table["Pollutant"][i]="不良"
    if table["AQI"][i]>=table["AQI"][maxad1]:
        maxad1=i
    #print (table.values[:]["AQI"])
"""    
for i in range(0,len(table)):
    if table["AQI"][i]>=table["AQI"][maxad2]:
        if table["AQI"][maxad1]>table["AQI"][maxad2]:
            maxad2=i
            
    #print (table.values[:]["AQI"])
for i in range(0,len(table)):
    #把對敏感族群不健康 替換成 不良
    if table["AQI"][i]>=table["AQI"][maxad1]:
        maxad1=i
    #print (table.values[:]["AQI"])    
"""    
print (table)
print (table.iloc[maxad1, :])
#print (table.iloc[maxad2, :])