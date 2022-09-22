# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 14:42
# @Author  : jinjie

# 模板继承  将同一样式如标题栏、尾页等封装在一起，作为父模板。
# 子模板直接调用即可，然后在定义自己页面样式和元素。避免代码冗余

# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:58
# @Author  : jinjie

from flask import Flask,render_template
# 模板中的控制循环


app = Flask(__name__)

@app.route('/')
def root_path():
    return "flask is working"

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/control')
def control():
    context = {
        "age": 17,
        "name": "小明",
        "books": ['三国','水浒','红楼','西游']
    }
    return render_template("control.html",**context)


@app.route('/inhert')
def inhert():
    context = {
        "age": 17,
        "name": "小明",
        "books": ['三国','水浒','红楼','西游']
    }
    return render_template("son_page.html",**context)


if __name__ == '__main__':
    app.run(port=10010,debug=True )


