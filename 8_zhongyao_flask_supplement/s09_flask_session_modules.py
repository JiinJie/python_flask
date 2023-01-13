# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 17:00
# @Author  : jinjie
# @File    : s09_flask_session_modules.py
# 使用 Flask-Session 内容 如下：
# 在不修改原有session的情况下，将session中的open-session替换为flask-session


from flask import Flask,views,url_for,session
from flask_session import Session
from redis import Redis
from s08_flask_CBV import bp


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SESSION_TYPE"] = "redis"   #配置sessio_type存入数据
app.config["SESSION_REDIS"] = Redis(host="127.0.0.1",port=6379,db=5)
# 直接传入redis对象，初始化其参数,db=5表示第5个切片（一共16个），用于隔离

app.secret_key = "test_key"


app.register_blueprint(bp)

# 使用flask-session
Session(app)
"""# session的数据存放位置
    def _get_interface(self, app):
        config = app.config.copy()
        config.setdefault('SESSION_TYPE', 'null')
        config.setdefault('SESSION_PERMANENT', True)
        config.setdefault('SESSION_USE_SIGNER', False)
        config.setdefault('SESSION_KEY_PREFIX', 'session:')
        config.setdefault('SESSION_REDIS', None)
        config.setdefault('SESSION_MEMCACHED', None)
        config.setdefault('SESSION_FILE_DIR',
                          os.path.join(os.getcwd(), 'flask_session'))
        config.setdefault('SESSION_FILE_THRESHOLD', 500)
        config.setdefault('SESSION_FILE_MODE', 384)
        config.setdefault('SESSION_MONGODB', None)
        config.setdefault('SESSION_MONGODB_DB', 'flask_session')
        config.setdefault('SESSION_MONGODB_COLLECT', 'sessions')
        config.setdefault('SESSION_SQLALCHEMY', None)
        config.setdefault('SESSION_SQLALCHEMY_TABLE', 'sessions')
"""

@app.route("/")
def index():
    return "hello!"


class Index(views.MethodView):
    # 不支持使用methods = ["GET","POST"]
    # 对应的请求方法
    def get(self):
        session["user"] = "user01"  # 本来的加密字符串会改为uuid，通过uuid拿到session
        # uuid --> c3ad7194-3bee-4970-b2ef-8c4e7d478950
        return "get something"

    def post(self):
        return "post something"


if __name__ == '__main__':
    app.run(port=10010)