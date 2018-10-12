# -*- coding: utf-8 -*-
"""
Created on Thu May 10 02:25:10 2018

@author: User
"""

import requests

r_off= requests.get("http://192.168.0.13/H")
print (r_off.getresponse().read())