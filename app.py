from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)



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
    
import os
import sys
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
import json
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
   
    return response['result']['fulfillment']['speech']     
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
