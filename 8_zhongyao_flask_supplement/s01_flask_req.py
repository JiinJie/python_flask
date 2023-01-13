# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 16:14
# @Author  : jinjie
# @File    : s01_flask_req.py

# 详解request中args、form、values

from flask import Flask,render_template,request
@app.route('/req_args')
def args_form():
    if request.method == "GET":
        return "helloworld"
    if request.method == "POST":
        print(request.args) #header中url的参数
        print(request.form) #body中的参数
        print(request.values) #所有的参数
        # 根据不同的content-type 会将数据存入不同的reuqest子类对象
        """
        如果args和form中均有同名参数，则会获取到args中的该参数值
        在通过values获取参数时会先获取args的再获取form
        """
        return f"{request.values.get('id')}"

# http://127.0.0.1/req_args?id=header_id
# body{"id":"body_id","name":"zhangsan"}