# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:19:15 2018

@author: User
"""
import requests
url = 'https://api.dialogflow.com/v1/intents?v=20150910'
headers = {'Authorization':'Bearer 3ed32c51113a4cb38a0ec269946a9f26','Content-Type':'application/json'}

r = requests.get(url, headers=headers)

print(r.json())