# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 14:52
# @Author  : jinjie
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Sqlconfig:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    # 连接flaskdb前需创建该数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


# 添加配置至flask app
app.config.from_object(Sqlconfig)

# 将 SQLAlchemy 绑定至app
db = SQLAlchemy(app)

class students1(db.Model): # 类名即为表名
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


# 清除所有表
db.drop_all()

# 创建所有表
db.create_all()

# if __name__ == '__main__':
#     app.run()