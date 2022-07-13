# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:37:35 2018

@author: User
"""

list=[30,98,12,191,66,47,82,54]

for i in range(0, len(list)-1):#從0開始並假設位置0為最小值
    min_indx = i 
    for j in range(i+1, len(list)):
        if (list[min_indx] > list[j]):#找到新的最小值位置時取代
            min_indx = j
            
    if (min_indx!=i):       #有心的最小值時要做交換
        tmp = list[min_indx]
        list[min_indx] = list[i]
        list[i] = tmp
    
print(list)