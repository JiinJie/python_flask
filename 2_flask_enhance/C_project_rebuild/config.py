# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 16:46
# @Author  : jinjie
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flaskdb'
USERNAME = 'root'
PASSWARD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWARD,HOSTNAME,PORT,DATABASE)


SQLALCHEMY_DATABASE_URI = DB_URI
# 配置是否跟踪每次修改
SQLALCHEMY_TRACK_MODIFICATIONS = True