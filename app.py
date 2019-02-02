import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
bot_id = "db59a366c4f2cbb461c3baae23	"

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # Check for trigger
  if 'JoeyBaca' in data['text']:
      if data['name'] != 'Private Baca':
        if data['name'] !="Sgt. Baca == American Hero"
            msg = 'Thank you Joey'
            send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : bot_id,
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

def log(msg):
  print(str(msg))
  sys.stdout.flush()
