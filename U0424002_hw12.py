# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:53:55 2018

@author: User
"""
import socket
import threading
import pandas as pd

bind_ip = "192.168.0.100"
bind_port = 5050


#建立 TCP server socket 物件
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#繫結socket與 ip, port 
server.bind((bind_ip, bind_port))
#開始監聽用戶端連接            
server.listen(5)

print ("[*] Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
	#讀取客戶端的資料, 並使用 decode() 將 byte 轉成 string 
    data1 = client_socket.recv(1024).decode() # Read Number 1
    #data2 = client_socket.recv(1024).decode() # Read Number 2
    print("股票代號",data1)
    #print("Number2=%s",data2)
    #data=int(data1)+int(data2)
    #print('Received: %s + %s = %d'%(data1,data2,data))
    tables = pd.read_html("https://tw.stock.yahoo.com/s/list.php?c=%A5b%BE%C9%C5%E9&rr=0.51589400%201526403022",encoding="big5")

    #print (tables)
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
    for i in range(2,74):
    #昨收-成交=漲跌
        if (float(table[3][i])-float(table[8][i])<=0):
            #print (float(table[3][i])-float(table[8][i]))
            #table = table.drop(table.index[i],axis=1)
            table = table.drop(i,axis=0)
    table = table.drop(table.columns[4:5],axis=1)
    table = table.drop(1,axis=0)
    
    table.columns =["股票代號","時間","成交","漲跌","最高","最低"] 
    result="not found."
    for i in table.index:
        b=table.loc[i,"股票代號"].find(data1)
        if(b!=-1):
            print(table.loc[i,:])
            result=table.loc[i,:]
    print(table)
    print(result)


	#傳送資料到客戶端
	#傳入socket前須先使用 encode()將 string 轉成 byte 以利 iostream 傳輸
    #若不轉換成 byte 將造成錯誤
    if(data1=="00000"):
         client_socket.send(str(table).encode())
         client_socket.close()
    client_socket.send(str(result).encode())
    #client_socket.send(str(table).encode())
    #client_socket.send(str("\n").encode())
    client_socket.close()
	
while True: # 伺服器需不斷的測試是否有Client與之相連
    #取得與客戶端連結的位址 addr 與 Socket物件 client
    client, addr = server.accept()
    print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
    #呼叫 handle_client 產生一個與客戶端連線的 Thread
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start() # 啟動客戶端連線的 Thread 
    #server.close()