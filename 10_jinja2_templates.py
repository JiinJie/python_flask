# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 17:23
# @Author  : jinjie
# 使用jinja2 模板

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def index():
    data = {
        'name':'zhangsan',
        'age':'18',
        'list_1':[1,2,3,4,5,6]
    }
    return render_template('index2_jinja.html',data=data)

@app.route('/filter')
def filter():

    return render_template('index2_jinja.html',data=data)


def list_step(li):
    """自定义过滤器"""
    return li[::2]

# 在自定义过滤器之前需要注册过滤器
app.add_template_filter(list_step,'li2_filter')



if __name__ == '__main__':
    app.run(port=10010)

