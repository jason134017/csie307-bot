# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:29:26 2018

@author: User
"""

'''
測試 Line Notify
Created on 2017年12月11日
@author: rocky.wang
'''
#import os
import lineTool
 
# token 改成你自己的，底下的案例是設到環境變數
#token = os.environ["LINE_TEST_TOKEN"]
# 這是放明碼，不建議，以免不小心就 push 到 github 上了
token = "dJPav4yXG1ILWCmlvdTqRvS2dgAodu8iwg6KY6ln6YZ"
msg = "Notify from Python \nHave a nice day"
 
lineTool.lineNotify(token, msg)