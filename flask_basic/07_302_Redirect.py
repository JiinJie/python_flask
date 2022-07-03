# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 14:42
# @Author  : jinjie

from flask import Flask,redirect,url_for
# redirectj和url_for 都可以用于重定向

app = Flask(__name__)

@app.route('/index')
def index():
    return 'hello ,this is index page'

@app.route('/baidu')
def baidu():
    """重定向至其他网站"""
    return redirect('http://www.baidu.com')

@app.route('/test')
def back_index():
    """重定向至自己的路由方法"""
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=10010)
