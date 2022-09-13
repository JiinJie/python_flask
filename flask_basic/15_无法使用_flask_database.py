# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 10:51
# @Author  : jinjie

# ①使用sqlalchemyd的实例
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# engine = create_engine('mysql:////root:123456@127.0.0.1:3306/flaskdb')
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
#
# def init_db():
#
#     Base.metadata.create_all(bind=engine)
#
#

# ②将其配置单独作为类来表示

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


class Sqlconfig:
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    # 连接flaskdb前需创建该数据库
    SQLALCHEMY_TRACK_MODIFICATIONS	= True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


# 添加配置至flask app
app.config.from_object(Sqlconfig)

# 将 SQLAlchemy 绑定至app
db = SQLAlchemy(app)


# 创建数据库模型类
# class Role(db.Model):
#     """角色表映射db模型"""
#     __tablename__ = 'role'
#     id = db.Column(db.In,)

class Book(db.Model):
	__tablename__ == 'book'   # 表名
	id = db.Column(db.Integer, primary_key = True, autoincrement = True) # id号
	title = db.Column(db.String(50), nullable = False) # 书名，不能为空
	price = db.Column(db.String(50), nullable = False) # 价格，不能为空
	publish_office = db.Column(db.String(100),nullable = False) # 出版社，不能为空
	isbn = db.Colume(db.String(50), nullable = False) # isbn号
	storage_time = db.Column(db.Datetime, default = datetime.now) # 入库时间
