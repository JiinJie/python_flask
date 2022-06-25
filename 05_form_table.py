# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 21:19
# @Author  : jinjie
# 前端页面在  .\templates\index.html 中

from flask import Flask,render_template


app = Flask(__name__)

@app.route('/login_page',methods=['GET','POST'])
def Login_page():
    return render_template('index.html')
    # 可以使用jinja2 （将文件及导入jinja2）

if __name__ == '__main__':
    app.run(port=10010)