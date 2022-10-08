# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:19
# @Author  : jinjie

from flask import Flask
import config
from db_common import db
from api_blueprints import bp_user
from api_blueprints import bp_quest





app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(bp_user)
app.register_blueprint(bp_quest)

@app.route('/')
def start():
    return "flask is running"


if __name__ == '__main__':
    app.run(port=10010,debug=True)
