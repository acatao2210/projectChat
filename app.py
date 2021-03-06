import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
bot_id = "ad73e79306e3ad1b3452a4a990"

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # Check for trigger
  if 'Joey' in data['text']:
      if data['name'] != 'Private Baca':
        if data['name'] !="Sgt. Baca == American Hero":
            msg = 'We dont need Baca, we just need 4 inches of cold rolled steel'
            send_message(msg)
  elif 'We cant just let them attack the gate' in data['text']:
      if data['name'] != 'Private Baca':
        if data['name'] !="Sgt. Baca == American Hero":
            msg = 'The bars of those gates are 4 inches of cold rolled steel'
            send_message(msg)
  elif 'You know nothing' in data['text']:
      if data['name'] != 'Private Baca':
        if data['name'] !="Sgt. Baca == American Hero":
            msg = '...Joey Baca'
            send_message(msg)
  elif '!gasp' in data['text']:
      if data['name'] != 'Private Baca':
        if data['name'] !="Sgt. Baca == American Hero":
            msg = ' '
            send_message_img(msg)

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

def send_message_img(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : bot_id,
          'text'   : msg,
          "picture_url": "https://i.groupme.com/540x283.gif.2412940a05a44378b4d92cc28f05c70f.large"
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()



def log(msg):
  print(str(msg))
  sys.stdout.flush()
