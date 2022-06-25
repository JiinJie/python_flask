# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 16:02
# @Author  : jinjie

# abort 主动抛出异常与raise功能类似

from flask import Flask, abort, request, make_response, render_template, url_for

app=Flask(__name__)

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print(name,passwd)
        if name =="zhangsan" and passwd == "123":
            return 'login success'
        else:
            # return f"{name},{passwd}"
            abort(404)
            return None





@app.errorhandler(404)
def stat_404(err):
    # re_info = f"404：无法找到页面 错误信息{err}"
    # return re_info
    return url_for('static',filename='code_404.html')

if __name__ == '__main__':
    app.run(port=10010)
