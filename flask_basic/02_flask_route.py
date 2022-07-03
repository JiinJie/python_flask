# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 19:56
# @Author  : jinjie
from flask import Flask

app = Flask(__name__)


@app.route('/url1')
def route_001():
    return '<h1>hello world<h1>'

@app.route('/url2')
def route_002():
    return '<h1>Goodbye<h1>'


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=11002)