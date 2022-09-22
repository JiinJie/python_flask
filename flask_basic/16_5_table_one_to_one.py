# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 11:40
# @Author  : jinjie

# 表关系 一对一
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Sqlconfig:

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

app.config.from_object(Sqlconfig)
db = SQLAlchemy(app)

