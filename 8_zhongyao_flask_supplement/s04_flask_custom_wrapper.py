# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 17:02
# @Author  : jinjie
# @File    : s04_flask_custom_wrapper.py
# 在flask中自定义装饰器

"""
在flask定义装饰器时，路由视图函数装饰器必须在最外层
"""


from flask import Flask,render_template,request,session,redirect
from functools import wraps

app = Flask(__name__)
app.secret_key="sessionkey"  #用来加密session内容

# 登录验证，位获取到session时会自动跳转login页面
def login_warp(f):
    def nei(*args,**kwargs):
        if session.get("user"):
            ret = f(*args,**kwargs)
            return ret
        return redirect("/login")
    return nei

@app.route('/index',methods=['GET','POST'],strict_slashes=False)
def index_page():
    if request.method == 'GET':
        return render_template('login_page.html')
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print(name,passwd)
        if name == "test" and passwd == "123456":
            session["user"] = name
            return render_template('homepage.html')
        else:
            return render_template("login_page.html",msg="账号或密码错误")

@app.route('/homepage',methods=['GET','POST'])
def homepage():
    if not session.get("user"): #判断是否有session,没有则直接跳转登录页面
        return redirect('/index')
    return render_template('homepage.html')


@app.route('/detail',endpoint="detail")
@login_warp
def detail():
    return render_template('detail.html')

"""# 默认添加多个login_warp时会报错
# 因为默认添加装饰器时，视图函数名称会发生改变，route中不允许有重名的视图函数
# 因此需要使用endpoint参数，使其不重复"""
@app.route('/userlist',endpoint="user_list")
@login_warp
def user_list():
    return render_template('userlist.html')


@app.route('/login',methods=['GET','POST'],endpoint="login")
def login():
    return redirect('/index')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=11111,debug=True)

