# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 10:19
# @Author  : jinjie

from flask import Flask
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
engine = db.get_engine()

@app.route('/')
def hello_world():
    # conn = engine.connect()
    # conn.close()
    with engine.connect() as conn:
        result = conn.execute('select 1')
        print(result.fetchone())
        st = str(result)
    return f"hello SQLAlchemy {st}"


if __name__ == '__main__':
    app.run(debug=True,port=10010)