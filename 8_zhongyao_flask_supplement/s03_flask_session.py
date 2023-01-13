# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 16:16
# @Author  : jinjie
# @File    : s03_flask_session.py
# session详解

from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key="sessionkey"  #用来加密session内容

@app.route('/index',methods=['GET','POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print(name,passwd)
        if name == "test" and passwd == "123456":
            session["user1"] = name #session会存放在浏览器的cookie中
            session["user2"] = name + "11111"  #添加的键值对越多，加密后的值越长
            return render_template('homepage.html')

@app.route('/homepage',methods=['GET','POST'])
def homepage():
    if request.method == 'GET':

        if not session.get("user1"): #判断是否有session,没有则直接跳转登录页面
            return redirect('index.html')
        return render_template('homepage.html')

    if request.method == 'POST':
        return render_template("405.html")

