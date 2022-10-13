# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:40
# @Author  : jinjie

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_redis import FlaskRedis

db = SQLAlchemy()
mail = Mail()
redis_cli = FlaskRedis()


