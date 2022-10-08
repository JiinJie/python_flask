# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 14:42
# @Author  : jinjie

# 安装
# pip install flask-migrate
"""
ORM模型迁移插件
lask-migrate是基于Alembic进行的一个封装，并集成到Flask中，而所有的迁移操作其实都是Alembic做的，他能跟踪模型的变化，并将变化映射到数据库中。
fun；更改 sqlachemy 类时无需每次删除后重新见表
省略 db.drop_all() db.create_all() 等众多操作

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

class Sqlconfig:

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

app.config.from_object(Sqlconfig)
db = SQLAlchemy(app)

# ---------------------------------------------------
# 创建Migrate 对象
migrate = Migrate(app, db)






class UserExtension(db.Model):  # 该拓展表数据为一对一关系
    __tablename__ = "user_ext"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # 反向引用  User.id 并控制限制使用list
    user = db.relationship("User", backref=db.backref("extension",uselist=False))

# ________before data ________
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)

# 之前创建的Article表
class Article(db.Model):
    __tablename__ = "artcle"
    # ！！！ 使用pycharm 专业版会对数据库操作的进行相关自动补全
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id 自增，设为主键
    title = db.Column(db.String(200), nullable=False)  # varchar 不超过200字符  不能为空
    content = db.Column(db.Text, nullable=False)  # 使用text文本类型，string最多只能225个字符

    #   添加外键进行关联   artcle表中的author_id 关联user表中的id
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

