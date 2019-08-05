from pymessenger import Bot
import os, sys
from flask import Flask, request

app = Flask(__name__)
PAGE_ACCESS_TOKEN = 'EAAg4f5ZBJPCwBACZBIOH5xDydyb4utfDO7sFuG2hChwCewqppbHYux2KrfExxtlz7wiEeYAaWUlZAgZBgfBtCoxHixH0ZAwer7NGHQG3nLTdsrkZCQTJbO33gT61GcpVmMcFagBbBPm7we5NZCaNlqobTeh85S6LemDHiJ800EibFMUtl58IQZA4YA3VTAC5qkEZD'
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    #Webhook Verification
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if not request.args.get('hub.verify_token') == 'hello':
            return 'Verification Token Mismatch', 403
        return request.args['hub.challenge'], 200
    return 'hello world', 200

@app.route('/',methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                #IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no_text'
                    #Echo
                    response = messaging_text
                    bot.send_text_message(sender_id, response)

    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug = True, port = 80)
