"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from pymessenger import Element, Button

app = Flask(__name__)

ACCESS_TOKEN = "EAAI7dZCA2fkcBAO8efZALItmw06JKM0kxcmzkz8vtZB5iZAwMVjUw3ezw15ZBO3m7ZA0ZAkkfFW9BQlIFiBLKgvzI3W5f7I1R8D90oEvqchfPbRAIANO62AKOSwFmYWJbfkpVYRXQCyvKdm9oUwGZBafCRorGUZAoGxFKerjxDE38ZCQZDZD"
VERIFY_TOKEN = "test_token"
bot = Bot(ACCESS_TOKEN)

def get_image_element(message):
    image_url = 'http://android.agrostar.in/static/Cotton.jpg'
    elements = []
    element = Element(title="Cotton", image_url=image_url, subtitle="Click to view more details", item_url="http://crm.agrostar.in/#/products")
    elements.append(element)
    return elements

def get_buttons():
    buttons = []
    button = Button(title='Want To Buy', type='web_url', url='http://crm.agrostar.in/#/products')
    buttons.append(button)
    button = Button(title='Want to Know More', type='postback', payload='other')
    buttons.append(button)
    text='Select Option'
    return text, buttons

def analyse_and_send_message(bot, recipient_id,  message):
    print "Sending message"
    bot.send_text_message(recipient_id, message)
    if 'cotton' in message:
        bot.send_generic_message(recipient_id, get_image_element('cotton'))
        result = bot.send_button_message(recipient_id, *get_buttons())        


















@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.json
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message') and x['message'].get('text'):
                    message = x['message']['text']
                    #message = "You said" + message
                    recipient_id = x['sender']['id']
                    analyse_and_send_message(bot, recipient_id, message)
                    #bot.send_text_message(recipient_id, message)
                    
                else:
                    pass
        return "Success"

if __name__ == '__main__':
    app.run(debug=True)

