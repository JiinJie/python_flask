# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 16:45
# @Author  : jinjie

from flask import Flask
from flask_migrate import Migrate
import config
from db_common import db

app = Flask(__name__)
app.config.from_object(config)

# 将app绑定至db上
db.init_app(app)

# 创建Migrate 对象
migrate = Migrate(app, db)


