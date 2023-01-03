# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 17:10
# @Author  : jinjie

from flask import Flask,Response,request,session


app = Flask(__name__)
app.config['SECRET_KEY'] = "ADVSADFDDA"

#  生成cookie
@app.route('/set_cookie')
def set_cookie():
    response = Response("cookie 设置")
    response.set_cookie("user_id","xxx_user_id_value_xxx")
    # response.set_cookie("user_id","xxx",max_age=1800,path='/')
    return response

# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get("user_id")
    print(f"userid: {user_id}")
    return "获取cookie"


"""
在设置session前必须设置secret_key
flask中会将session的 内容（key和value）通过secret_key进行加密，返回给前端
"""
@app.route('/set_session')
def set_session():
    session['username'] = "test_user"
    return "session 设置成功"

@app.route('/get_session')
def get_session():
    username = session.get('username') #直接获取，flask底层会自动解密
    print("username")
    return "get session"



@app.route('/index')
def index_page():
    return "this is index page"




if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=10010,debug=True)