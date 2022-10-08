# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 19:36
# @Author  : jinjie
from flask import Flask

app = Flask(__name__)

# 配置路由映射地址
@app.route('/test/')
# 路由装饰的函数称为函数视图
def hello():
    return 'start flask'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=11001,debug = True,)
     # 设置debug可以直接保存项目后立即刷新后端

