# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 14:14
# @Author  : jinjie
from commons import db
from datetime import datetime


class EmailModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(100),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    #使用now() 则会实例化对象，项目运行时实例化一次该时间（该时间不会改变）。直接使用now则在每次运行时调用一次函数


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now)



