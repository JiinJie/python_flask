# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 16:47
# @Author  : jinjie

# abort 在网页中主动抛出异常 ，  与 raise 主动抛出异常类似

from flask import Flask,abort

app = Flask(__name__)

@app.route('/index')
def index_page():
    abort(404)  #当访问不正确的路由时会自动abort 404 页面
    return '1234'




if __name__ == '__main__':
    app.run()