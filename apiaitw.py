# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:53:57 2018

@author: User
"""

import os.path
import sys
import json as json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'e6e3017b385347a8b26284f52c6ea2b0'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = "close the door"

    response = json.loads(request.getresponse().read().decode('utf-8'))
    #print (response.read())
    print (response)

    

if __name__ == '__main__':
    main()