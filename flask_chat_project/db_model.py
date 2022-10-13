# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 14:14
# @Author  : jinjie
from commons import db
from datetime import datetime
from werkzeug.security import generate_password_hash
import uuid

"""
flask db init
flask db migrate
flask db upgrade
"""
class EmailModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(100),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    #使用now() 则会实例化对象，项目运行时实例化一次该时间（该时间不会改变）。直接使用now则在每次运行时调用一次函数


class UserModel(db.Model):
    # 初始化用户密码，将其直接加密存入数据库，就不需要在视图函数中调用
    def __init__(self,*args,**kwargs):
        if "password" in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop("password")
        super(UserModel,self).__init__(*args,**kwargs)
        # 使用super继承该类的其他属性，只初始化了password

    #将password变量方法转为属性。可以直接通过属性的方式调用
    # now: UserModel.password
    # before UserModel.password()
    @property
    def password(self):
        return self._password

    # 将设置password的属性
    @password.setter
    def password(self,newpwd):
        self._password=generate_password_hash(newpwd)


    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    _password = db.Column(db.String(200), nullable=False, unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now)


class CommitQuestModel(db.Model):
    __tablename__ = "quest"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(50),default=uuid.uuid1().int)   #生成时间戳相关的唯一uuid
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)  # 作者字段引用外键
    create_time = db.Column(db.DateTime,default=datetime.now)

    author = db.relationship("UserModel",backref="authors")


class AnswerModel(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey("quest.id"),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)  # 设置关联的外键属性必须与关联的字段属性一致(类型，非空等)
    create_time = db.Column(db.DateTime,default=datetime.now)

    bind_quest_id = db.relationship("CommitQuestModel",backref=db.backref("answers_q",order_by=create_time.desc()))  #时间倒序
    reply_author = db.relationship("UserModel",backref="answers_a")


