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

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
    
#create event   
import datetime
#payload = {'ctrl': '1'}
#r_on= requests.get("http://192.168.0.13/1") 
today=datetime.date.today()
start='19:00:00'
end='2018-07-25T19:00:00Z'
if(len(start)==8):
    time=str(today)+"T"+start+"+08:00"
    #now=datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    print (time) 
elif(len(start)==20):
    time=start.replace("Z","+08:00")
    #now=datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    print (time)    
event = {
  'summary': 'Google I/O 2018 test',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2018-07-26T20:00:00+08:00',
  },
  'end': {
    'dateTime': '2018-07-26T22:00:00+08:00',
  },
  
}

event = service.events().insert(calendarId='primary', body=event).execute()
print ('Event created: %s' % (event.get('htmlLink')))