# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 15:43
# @Author  : jinjie
# @File    : s08_flask_CBV.py

# flask中的CBV  CBV(class-based-view) 中文翻译为视图类
# 对应的是 FBV(function-based-view) 视图函数[flask默认的接口方式]
# flask默认使用的是FBV，使用的是resful规范

from flask import Flask, views, Blueprint

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return "hello!"

# 编写一个视图类

class Index(views.MethodView):
    # 不支持使用methods = ["GET","POST"]
    # 对应的请求方法
    def get(self):
        return "get something"

    def post(self):
        return "post something"

# as_view 将类中的每一个函数(get、post)对应写入视图方法,将其命名为index
# 如果使用get方法访问，返回的将是get something 如果使用post方法访问，返回的将是post something
app.add_url_rule("/index",endpoint="class_index",view_func=Index.as_view(name="index"))

# ---cbv在buleprint中的用法---

bp = Blueprint("blue_name",__name__)
class bpclass(views.MethodView):
    def get(self):
        return "blue_get"

bp.add_url_rule("/blue",endpoint="blue",view_func=bpclass.as_view(name="bpclass"))

if __name__ == '__main__':
    app.run()
