# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 9:46
# @Author  : jinjie

# 自定义过滤器


from flask import Flask,abort,render_template


app = Flask(__name__)

@app.route('/index')
def index_page():
    abort(404)  #当访问不正确的路由时会自动abort 404 页面

    data = {
        'name': '张三',
        'age': '18',
        'mylist': [1,2,3,4,5,6],
    }

    return render_template('index.html',data=data)


def my_list_filter(li):
    """自定义过滤器"""
    return li[::2]

# 注册该自定义过滤器
app.add_template_filter(my_list_filter,'list_filter')
# my_list_filter是函数名，list_filter是在前端页面中的映射




if __name__ == '__main__':
    app.run()