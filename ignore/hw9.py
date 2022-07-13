import pandas as pd
url = 'http://www.stockq.org/market/asia.php'
table = pd.read_html(url)[4]
table = table.drop(table.columns[[0,1,2,3,4]],axis=0)
table = table.drop(table.columns[9:296],axis=1)
print(table)