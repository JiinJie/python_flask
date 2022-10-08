# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:23
# @Author  : jinjie
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
db = SQLAlchemy(app)


migrate = Migrate(app=app, db=db, directory='migrate_dir')


class User001(db.Model):
    __tablename__ = "user001"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


# db.create_all()