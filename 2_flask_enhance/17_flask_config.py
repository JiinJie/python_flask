# -*- coding: utf-8 -*-
# @Time    : 2022/9/9 10:29
# @Author  : jinjie

# 添加config.py文件后可以直接使用

from flask import Flask
import config

app = Flask(__name__)
# 在入口方法中，直接导入所有配置即可
app.config.from_object(config)  # 即config文件



if __name__ == '__main__':
    app.run()

