# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:36:36 2018

@author: User
"""

import pandas as pd
import tensorflow as tf
import numpy as np

#首先將資料讀入並存至pandas的DataFrame，另外對可能有N/A的row進行剔除：
aqi= pd.read_csv('./AQI-n20.csv' ,index_col=0,encoding="big5")
aqi.dropna(how='any',inplace=True)



print(aqi)
from sklearn import preprocessing
def normalize(df):
    newdf= df.copy()
    min_max_scaler = preprocessing.MinMaxScaler()
    
    for i in range(1,21):
        s="AQI"+str(i)
        newdf[s] = min_max_scaler.fit_transform(df[s].values.reshape(-1,1))
   
    return newdf
AQI_norm= normalize(aqi)
print(AQI_norm)

import numpy as np
def data_helper(df, time_frame):
    
    # 資料維度: 開盤價、收盤價、最高價、最低價、成交量, 5維
    number_features = len(df.columns)
    # 將dataframe 轉成 numpy array
    datavalue = df.as_matrix()
    result = []
    # 若想要觀察的 time_frame 為20天, 需要多加一天做為驗證答案
    for index in range( len(datavalue) - (time_frame+1) ): # 從 datavalue 的第0個跑到倒數第 time_frame+1 個
        result.append(datavalue[index: index + (time_frame+1) ]) # 逐筆取出 time_frame+1 個K棒數值做為一筆 instance
    
    result = np.array(result)
    number_train = round(0.9 * result.shape[0]) # 取 result 的前90% instance做為訓練資料
    
    x_train = result[:int(number_train), :-1] # 訓練資料中, 只取每一個 time_frame 中除了最後一筆的所有資料做為feature
    y_train = result[:int(number_train), -1][:,-1] # 訓練資料中, 取每一個 time_frame 中最後一筆資料的最後一個數值(收盤價)做為答案
    
    # 測試資料
    x_test = result[int(number_train):, :-1]
    y_test = result[int(number_train):, -1][:,-1]
    
    # 將資料組成變好看一點
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], number_features))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], number_features))  
    return [x_train, y_train, x_test, y_test]
# 以20天為一區間進行股價預測
X_train, y_train, X_test, y_test = data_helper(AQI_norm, 20)



from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.recurrent import LSTM
import keras
def build_model(input_length, input_dim):
    d = 0.3
    model = Sequential()
    model.add(LSTM(256, input_shape=(input_length, input_dim), return_sequences=True))
    model.add(Dropout(d))
    model.add(LSTM(256, input_shape=(input_length, input_dim), return_sequences=False))
    model.add(Dropout(d))
    model.add(Dense(16,kernel_initializer="uniform",activation='relu'))
    model.add(Dense(1,kernel_initializer="uniform",activation='linear'))
    model.compile(loss='mse',optimizer='adam', metrics=['accuracy'])
    return model
# 20天、5維
model = build_model( 20, 15 )

model.fit( X_train, y_train, batch_size=128, epochs=50, validation_split=0.1, verbose=1)

def denormalize(df, norm_value):
    original_value = df['AQI1'].values.reshape(-1,1)
    norm_value = norm_value.reshape(-1,1)
    
    min_max_scaler = preprocessing.MinMaxScaler()
    min_max_scaler.fit_transform(original_value)
    denorm_value = min_max_scaler.inverse_transform(norm_value)
    
    return denorm_value
# 用訓練好的 LSTM 模型對測試資料集進行預測
pred = model.predict(X_test)
# 將預測值與正確答案還原回原來的區間值
denorm_pred = denormalize(aqi, pred)
denorm_ytest = denormalize(aqi, y_test)


import matplotlib.pyplot as plt
  
plt.plot(denorm_pred,color='red', label='Prediction')
plt.plot(denorm_ytest,color='blue', label='Answer')
plt.legend(loc='best')
plt.show()

# Add an op to initialize the variables.
init_op = tf.global_variables_initializer()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, initialize the variables, do some work, and save the
# variables to disk.
with tf.Session() as sess:
  sess.run(init_op)
  # Do some work with the model.

  # Save the variables to disk.
  save_path = saver.save(sess, "/tmp/model.ckpt")
  print("Model saved in path: %s" % save_path)