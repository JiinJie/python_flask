# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 15:01
# @Author  : jinjie

from flask import Flask,make_response,json,jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/index')
def index():
    data = {
        'name':'zhangsan'
    }
    resp =  make_response(json.dumps(data,ensure_ascii=False))
    resp.mimetype = 'application/json'
    return resp
# 将数据转为json格式 默认使用ASCII码返回时不会识别为json格式，通过禁用可以正常显示

@app.route('/index_json')
def return_json():
    data = {
        'name':'张三'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=10010)
