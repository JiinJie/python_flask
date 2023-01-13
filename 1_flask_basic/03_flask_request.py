# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 20:03
# @Author  : jinjie

from flask import Flask,request,Markup
app = Flask(__name__)

# methods为请求方式 endpoint防止方法重名而使用别名
@app.route('/url1',methods=['GET','POST'],endpoint='hello')
def route_001():
    return '<h1>hello world<h1>'

@app.route('/url2')
def route_002():
    return '<h1>Goodbye<h1>'

@app.route('/course/<id>')
#默认传参都是str类型，因此需要转换
#或者使用转换器 'int:id'  @app.route('/course/<int:id>')
def index(id):
    if id == '1':
        return 'python'
    if id == str(2):
        return 'java'
    if int(id) == 3:
        return 'c++'

@app.route('/req_args')
def args_form():
    if request.method == "GET":
        return "helloworld"
    if request.method == "POST":
        print(request.args) #header中url的参数
        print(request.form) #body中的参数
        print(request.values) #所有的参数
        """
        如果args和form中均有同名参数，则会获取到args中的该参数值
        在通过values获取参数时会先获取args的再获取form
        """
        return f"{request.values.get('id')}"

# http://127.0.0.1/req_args?id=header_id
# body{"id":"body_id","name":"zhangsan"}



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=11002)