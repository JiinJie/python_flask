# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 14:42
# @Author  : jinjie
import time

from flask import Flask, redirect, url_for, request, render_template

# redirectj和url_for 都可以用于重定向

# 重定向分为暂时重定向和永久重定向


app = Flask(__name__)

@app.route('/index')
def index_page():
    return 'hello ,this is index page'

@app.route('/baidu')
def baidu():
    """重定向至其他网站"""
    return redirect('http://www.baidu.com')

@app.route('/test')
def back_index():
    """重定向至自己的路由方法"""
    return redirect(url_for('index_page'))


@app.route('/profile')
def profile():
    # 参数传递的两种方式：
    # 1、 作为url的组成部分： /book/1
    # 2、 查询字符串： /book?id=1
    user_id = request.args.get('id')
    if user_id:
        return f"用户个人中心,当前用户为{user_id}"
    else:
        return redirect(url_for('index_page'))



# tips_page多次使用重定向，需要借助前端页面进行二次跳转
@app.route('/tips_page')
def tips_fun():
    return render_template("many_redirect.html")  # 返回页面提示信息，由页面再次重定向


if __name__ == '__main__':
    app.run(port=10010,debug=True)
