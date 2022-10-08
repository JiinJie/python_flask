# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:33
# @Author  : jinjie

#  数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'chat_web'
USERNAME = 'root'
PASSWARD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWARD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
# 配置是否跟踪每次修改
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "ads321dsa123"

