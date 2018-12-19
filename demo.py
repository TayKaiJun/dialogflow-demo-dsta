import os
import json

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    
    # taking data from dialogflow
    result = req.get("queryResult")
    parameters = result.get("parameters")
    action = result.get('action')
    
    emotion = parameters.get("Emotion")
    
    if action == "show_heroku_emotion":
        correctOutput = "Hello, you're in Heroku and you're " + str(emotion)
        return {
            "fulfillmentText": correctOutput
        }
    else:
        return {
            "fulfillmentText": "You failed"
        }
    
        
