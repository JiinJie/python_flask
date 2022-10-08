# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 13:55
# @Author  : jinjie

from flask import Flask,render_template,request


app = Flask(__name__)


@app.route('/')
def start_page():
    return "flask is running"

@app.route('/index',methods=['GET','POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print(name,passwd)
        return render_template('405.html')

@app.route('/login_page',methods=['GET','POST'])
def Login_page():
    return render_template('login.html')
    # 可以使用jinja2 （将文件及导入jinja2）


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=10010,debug=True)