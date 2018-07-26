# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


import os.path
import json as json
import sys
import datetime
import speech_recognition as sr
from gtts import gTTS
import requests
import tempfile 
from pygame import mixer

#setting mic
mixer.init()
#seting apiai 
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
CLIENT_ACCESS_TOKEN = 'e6e3017b385347a8b26284f52c6ea2b0'
# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))


#play this text
def play(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save('{}.mp3'.format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
    #speech.say('Hola mundo', 'es_ES')
    
def googlecalendarcreate(start,end,description):
    event = {
      'summary': 'Google I/O 2018 test',
      'location': '800 Howard St., San Francisco, CA 94103',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': start,
      },
      'end': {
        'dateTime': end,
      },
  
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))
                    
#execute     
def run(text):
    #tts = gTTS(text="execute"+text, lang='en')
    play("execute"+text)
    print("execute",text)
    
def timeformat(time):
    today=datetime.date.today()

    if(len(time)==8):
        time=str(today)+"T"+time+"+08:00"
        #now=datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        print ("format:"+time)
        return time
        
    elif(len(time)==20):
        time=time.replace("Z","+08:00")
        #now=datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        print ("format:"+time)
        return time
        
#apiai setting  and main excute stay
def main(text):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = text
    #response = request.getresponse()
    response = json.loads(request.getresponse().read().decode('utf-8'))
    #print (response.read())
    print (response)
    print ("-------------------------------------------------------")
    print (response['result']['fulfillment']['speech'])
           
    #light statu change
    status=response['result']['parameters']
    print(status)
    
    if(response['result']['fulfillment']['speech']=="ok,I will make an appointment ."):
        print(status['start'])
        print(status['end'])
        if(status['start']!='' and status['end']!=''):
            start=timeformat(status['start'])
            end=timeformat(status['end'])
            print("make appointment,google")
            googlecalendarcreate(start,end,"test")
    for i in status:
        #print(i) #json name
        #print(status[i])#json value
        if(i=="light"):
            if(status[i]=="on" or status[i]=="off"):
                payload = {'ctrl': status['light']}
                requests.get("http://120.105.129.70/home/ctrl.php", params=payload) 
                """
                if(status['light']=="off"):
                    r_off= requests.get("http://192.168.0.13/0") 
                if(status['light']=="on"):
                    r_on= requests.get("http://192.168.0.13/1") 
                """
    play(text=response['result']['fulfillment']['speech'])     
    
if __name__ == '__main__':
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...") 
        #listen for 5 seconds and create the ambient noise energy level 
        r.adjust_for_ambient_noise(source, duration=6)    
        tts = gTTS(text="hello", lang='en')
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            tts.save('{}.mp3'.format(fp.name))
            mixer.music.load('{}.mp3'.format(fp.name))
            mixer.music.play()
        
        print("Say something!")
        audio=r.listen(source)

# recognize speech using Google Speech Recognition 
    try:
        print("Google Speech Recognition thinks you said:")
        print(r.recognize_google(audio, language="en"))
        run(r.recognize_google(audio, language="en"))
        main(r.recognize_google(audio, language="en"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))

   
