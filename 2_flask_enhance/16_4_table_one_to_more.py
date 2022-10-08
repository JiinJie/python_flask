# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 10:43
# @Author  : jinjie

# 表关系 一对多
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Sqlconfig:

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

app.config.from_object(Sqlconfig)
db = SQLAlchemy(app)


# 创建user表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200),nullable=False)

# 之前创建的Article表
class Article(db.Model):
    __tablename__ = "artcle"
    # ！！！ 使用pycharm 专业版会对数据库操作的进行相关自动补全
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) #id 自增，设为主键
    title = db.Column(db.String(200),nullable=False) # varchar 不超过200字符  不能为空
    content = db.Column(db.Text,nullable=False)  #使用text文本类型，string最多只能225个字符

#   添加外键进行关联   artcle表中的author_id 关联user表中的id
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))

# sqlalchemy 中使用relationship进行关系绑定
    """
    使用relationship的前提是必须已经绑定外键
    backref 是反向引用,表示对方访问Article的字段名称  
    一个"user"可能会有多个"article"因此创建变量 "articles"
    """
    author = db.relationship("User", backref="articles")



# 暂未使用ORM迁移，现删除表再创建修改表结构才能生效
db.drop_all()
# 将ORM映射转化为数据库中的表
db.create_all()
print("创建完成")



@app.route('/one_to_more')
def one_to_more():
    article1 = Article(title="111",content="内容xxxxx")  # Article中的author_id会自动创建
    article2 = Article(title="222",content="内容yyyyy")  # Article中的author_id会自动创建
    user = User(username="zhangsan")
    article1.author = user  #进行绑定
    article2.author = user  #进行绑定
    db.session.add(article1,article2)
    db.session.commit()
    return "one to more 绑定成功"


if __name__ == '__main__':
    app.run(port=10010,debug=True)