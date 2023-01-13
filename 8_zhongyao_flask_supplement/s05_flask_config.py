# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 10:48
# @Author  : jinjie
# @File    : s05_flask_config.py
# flask的四种配置方式

from flask import Flask
import flask_config


app = Flask(__name__)
# 1-默认方式
app.config["DEBUG"] = True

# 2-使用文件方式添加1(使用默认的config文件)
app.config.from_pyfile('config.py')

# 3-使用类对象方式添加2(自定义导入外部文件)
app.config.from_object(flask_config.Config)

@app.route("indx")
def index():
    return "hello world"


if __name__ == '__main__':
# 4-启动添加参数
    app.run(port=10011)

