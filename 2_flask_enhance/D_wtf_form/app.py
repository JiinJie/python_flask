# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:40
# @Author  : jinjie
from flask import Flask,request,render_template

from forms import LoginForm

app = Flask(__name__)


@app.route('/login',methods=['GET','POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')  # 将表单传给前端页面
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():  # 如果验证通过才能提交
            return "登陆成功"
        else:
            return "邮箱或密码错误"

@app.route('/')
def start():
    return "flask is running"



if __name__ == '__main__':
    app.run(port=10010,debug=True)
