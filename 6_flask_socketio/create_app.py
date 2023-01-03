# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 9:50
# @Author  : jinjie
# @File    : create_app.py

# 需要提前安装websocket   pip install websocket
# 改善 websocket使用  pip install gevent-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO
import random

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['allow_unsafe_werkzeug'] = True
socketio = SocketIO(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('test_socketio.html')


@socketio.on('connect', namespace='/test_conn')
def test_connect():
    while True:
        socketio.sleep(5)
        t = random_int_list(1, 100, 10)
        socketio.emit('server_response',
                      {'data': t},
                      namespace='/test_conn')


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=10010, debug=True)
