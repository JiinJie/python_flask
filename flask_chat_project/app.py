# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:19
# @Author  : jinjie
import celery
from flask import Flask,session,g  #全局变量g
import config
from mycelery import make_celery
from commons import mail,db,redis_cli
from api_blueprints import bp_user,bp_quest,bp_backact
from flask_migrate import Migrate
from db_model import UserModel




app = Flask(__name__)
app.config.from_object(config)
# 初始化mysql数据库模块
db.init_app(app)
# 初始化邮件模块
mail.init_app(app)
# 初始化redis数据库模块
redis_cli.init_app(app)


celery_app = make_celery(app)
migrate = Migrate(app=app, db=db, directory='migrate_dir')

app.register_blueprint(bp_user)
app.register_blueprint(bp_quest)
app.register_blueprint(bp_backact)



# 将session属性绑定至全局变量g，每次调用前均进行设置
@app.before_request
def set_session():
    user_id = session.get("user_id")
    #"user_id"是session中的属性，通过flask可以直接解析。获取请查看user.py中的login视图
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # setattr(g,"user",user)  === g.user = user
            # 将g绑定一个名为user的全局变量，值为user
            g.user = user
        except:
            print("该用户不存在")
            g.user = None


# 上下文处理器,所有模板均会执行该方法
@app.context_processor
def context_user():
    # 如果当前用户已经登录则返回，如果为登录则不做处理
    if hasattr(g,"user"):
        return {"user": g.user}
    else:
        return {}  # 直接返回空


@app.route('/')
def start():
    return "flask is running"





if __name__ == '__main__':

    app.run(port=10010,debug=True)
