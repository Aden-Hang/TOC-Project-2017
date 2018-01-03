import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = "545376328:AAGJI0a5beqjQjyutQ3Va_9XpnHYE6FG9sQ"
WEBHOOK_URL = 'https://a998cfa9.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'start',
        'hi',
        'hello',
        'goodmorning',
        'sleep',
        'plan',
        'no_plan',
        'study',
        'n_d',
        'n_o',
        's_d',
        's_o',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'hi',
            'conditions': 'is_going_to_hi'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'hello',
            'conditions': 'is_going_to_hello'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'goodmorning',
            'conditions': 'is_going_to_goodmorning'
        },
        {
            'trigger': 'advance',
            'source': 'plan',
            'dest': 'sleep',
            'conditions': 'is_going_to_sleep'
        },
        {
            'trigger': 'advance',
            'source': 'plan',
            'dest': 'no_plan',
            'conditions': 'is_going_to_no_plan'
        },
        {
            'trigger': 'advance',
            'source': 'plan',
            'dest': 'study',
            'conditions': 'is_going_to_study'
        },
        {
            'trigger': 'advance',
            'source': 'no_plan',
            'dest': 'n_d',
            'conditions': 'is_going_to_n_d'
        },
        {
            'trigger': 'advance',
            'source': 'no_plan',
            'dest': 'n_o',
            'conditions': 'is_going_to_n_o'
        },
        {
            'trigger': 'advance',
            'source': 'study',
            'dest': 's_d',
            'conditions': 'is_going_to_s_d'
        },
        {
            'trigger': 'advance',
            'source': 'study',
            'dest': 's_o',
            'conditions': 'is_going_to_s_o'
        },
        {
            'trigger': 'go_plan',
            'source': [
                'hello',
                'hi',
                'goodmorning',
                'n_d',
                's_d'
            ],
            'dest': 'plan'
        },
        {
            'trigger': 'go_back',
            'source':  [
                'sleep',
                's_o',
                'n_o',
            ],
            'dest': 'start'
        }
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
