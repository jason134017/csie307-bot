# -*- coding: utf-8 -*-
"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
#import requests
# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

#import requests

#payload = {'ctrl': '1'}
#r_on= requests.get("http://192.168.0.13/1") 
def timeformat(time):
    today=datetime.date.today()

    if(len(time)==8):
        time=str(today)+"T"+time+"+08:00"
        #now=datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        print (time)
        return time
    elif(len(time)==20):
        time=time.replace("Z","+08:00")
        #now=datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        print (time)
        return time
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
if __name__ == '__main__':
    start=timeformat("22:00:00")
    end=timeformat("23:00:00")
    #googlecalendarcreate(start,end,"test")
    #payload = {'ctrl': 'off'}
    #requests.get("http://120.105.129.70/home/ctrl.php", params=payload) 