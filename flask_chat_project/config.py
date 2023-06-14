# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:33
# @Author  : jinjie

# jsonify接口返回编码设置为utf-8
JSON_AS_ASCII = False
JSONIFY_MIMETYPE = "application/json;charset=utf-8"

#  数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_chat_sys'
USERNAME = 'root'
PASSWARD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWARD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
# 配置是否跟踪每次修改
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "ads321dsa123"

# 邮箱配置
MAIL_SERVER = "smtp.163.com"    #默认为 ‘localhost’
MAIL_PORT = 465          #默认为 25
MAIL_USE_TLS = False    #默认为 False
MAIL_USE_SSL = True     #默认为 False
MAIL_DEBUG = True       #默认为 app.debug
MAIL_USERNAME = "username@163.com"
MAIL_PASSWORD = "password"
MAIL_DEFAULT_SENDER = "username@163.com"
# MAIL_MAX_EMAILS = None  #默认为 None
# MAIL_SUPPRESS_SEND = app.testing    #默认为 app.testing
# MAIL_ASCII_ATTACHMENTS = False      #默认为 False


# Celery配置
REDIS_URL = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

