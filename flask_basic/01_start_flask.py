# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 19:36
# @Author  : jinjie
from flask import Flask

app = Flask(__name__)

@app.route('/test/')
def hello():
    return 'start flask'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="11001")

