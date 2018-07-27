from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import os
import json
import datetime

import linetool
#llne setting

app = Flask(__name__)
#
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
        
# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
#
def googlecalendarcreate(start,end,summary):
    event = {
      'summary': summary,
      'start': {
        'dateTime': start,
      },
      'end': {
        'dateTime': end,
      },
  
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return

import apiai

CLIENT_ACCESS_TOKEN = 'e6e3017b385347a8b26284f52c6ea2b0'
def main(text):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = text
    #response = request.getresponse()
    response = json.loads(request.getresponse().read().decode('utf-8'))
    #print (response.read())
    status=response['result']['parameters']
    
    if(response['result']['fulfillment']['speech']=="ok,I will make an appointment."):
        if(status['start']!='' and status['end']!=''):
            start=timeformat(status['start'])
            end=timeformat(status['end'])
            googlecalendarcreate(start,end,"Auto add with linebot")
    
    if(response['result']['fulfillment']['speech']=="ok,send the Emergency message."):
        msg = "Notify from Python \nEmergency message"
        lineTool.lineNotify(os.environ['linetoken'], msg) 
        
    return response['result']['fulfillment']['speech']     
# Channel Access Token
line_bot_api = LineBotApi('hENhmJA37FLCWKahY/DjYkbvrQuHlekCAsrZ0iUhtpzbyfc+aXllNKV1Do7S1z6MdBMuPVvlcB97QnY9e1Glk5n5tlUhdlmTqhexrZFEidyR2wj9jwgixxT+mLY+HKak5HanZRA0Oy3bPO22B8S8mwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2987a3d9ddb8a4d84c9f206e1113518e')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message)
    result=main(event.message.text)
    message = TextSendMessage(text=result)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
