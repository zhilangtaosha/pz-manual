#!/usr/bin/python
# _*_ coding: utf-8 _*_
from gevent import monkey

monkey.patch_all()

import json
import base64
import urllib

from flask import Flask, request, jsonify
# from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler
from flask_twisted import Twisted

from bot import chatbot
from conf.const import *

app = Flask(__name__, instance_relative_config=True)
twisted = Twisted(app)
app.config['DEBUG'] = False


@app.route('/gac/demo', methods=['POST', 'GET'])
def home():
    bot = chatbot.ChatBot()
    if request.method == 'GET' and request.args:
        msg = request.args
        user_id = msg[UID]
        query = base64.b64decode(urllib.unquote(msg[QUERY])).decode("utf-8")
        bot.set({UID: user_id, QUERY: query})
        data_tup = bot.get_response().decode("unicode_escape")
        return data_tup, 201
    elif request.method == 'POST' and request.json:
        msg = json.loads(request.get_data())
        query = (msg[QUERY])
        user_id = msg[UID]
        bot.set({UID: user_id, QUERY: query})
        data_tup = bot.get_response().decode("unicode_escape")
        return jsonify(data_tup), 200
    else:
        return '<h1>只接受get.post请求！</h1>'


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 5000
    DEBUG = True if app.config['DEBUG'] else False
    if DEBUG:
        app.run(host='0.0.0.0', debug=DEBUG, threaded=True)
    else:
        app.run(host='0.0.0.0', threaded=True)
        # if DEBUG:
        #     app.run(debug=DEBUG, threaded=True)
        #     app.debug = True
        #     server = WSGIServer(('', int(port)), app, handler_class=WebSocketHandler)
        #     server.serve_forever()
        # else:
        #     server = WSGIServer(('', int(port)), app, handler_class=WebSocketHandler)
        #     server.serve_forever()
