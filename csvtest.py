# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 02:42:33 2018

@author: User
"""

import pandas as pd
import tensorflow as tf
import numpy as np

#首先將資料讀入並存至pandas的DataFrame，另外對可能有N/A的row進行剔除：
aqi= pd.read_csv('./AQI-n20o.csv' ,index_col=0,encoding="big5")
aqi.dropna(how='any',inplace=True)
aqi=aqi[::-1]