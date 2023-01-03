# -*- coding: utf-8 -*-
# @Time    : 2022/12/7 10:48
# @Author  : jinjie
# @File    : myapp.py


from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



# 数据库的配置变量

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flaskdb'
USERNAME = 'root'
PASSWARD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWARD,HOSTNAME,PORT,DATABASE)


app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# 配置是否跟踪每次修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
engine = db.engine()
# #engine = db.get_engine() get_engine()在3.1版本中被弃用


@ app.route('/',methods=['GET'])
def index():
    return {"flask is running"}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10010,debug=True)



