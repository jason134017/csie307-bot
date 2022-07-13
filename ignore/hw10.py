# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:30:43 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:14:27 2018

@author: User
"""

import pandas as pd
tables = pd.read_html("https://opendata.epa.gov.tw/Data/Contents/AQI/")
x=len(tables)
table = tables[x-1]
table = table.drop(table.columns[3:4],axis=1)
table = table.drop(table.columns[4::],axis=1)
table.columns =["SiteName","County","AQI","Pollutant"]
#print (table["AQI"][0])
for i in range(0,len(table)):
    #把對敏感族群不健康 替換成 不良
    if table["AQI"][i]>=101:
        table["Pollutant"][i]="不良"
    #print (table.values[:]["AQI"])
   
print (table)



