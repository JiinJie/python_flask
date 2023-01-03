# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 10:32
# @Author  : jinjie
# @File    : instant_msg.py
import time
from datetime import datetime

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@ app.route('/',methods=['POST','GET'])
def index():
    return render_template('send_msg.html')



@ socketio.on('imessage', namespace='/test_conn')
def test_message(message):
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    emit('message', {'data': message['data']+'\t'+nowtime}, broadcast=True)  # broadcast表示启用广播，后端广播信息的事件名最好跟前端发送信息的事件名不同
    # emit('message', {'data': message['data'] + '\t' + nowtime}, broadcast=False)




if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0", debug=True, port=10011)
