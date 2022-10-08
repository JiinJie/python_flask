# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:58
# @Author  : jinjie

from flask import Flask,render_template
# 模板中的控制循环


app = Flask(__name__)

@app.route('/')
def index():
    return "flask is working"

@app.route('/control')
def control():
    return render_template("control.html")

