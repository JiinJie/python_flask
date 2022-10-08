# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 11:40
# @Author  : jinjie

# 表关系 一对一
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Sqlconfig:

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

app.config.from_object(Sqlconfig)
db = SQLAlchemy(app)

"""创建 UserExtension 存放用户不常用的信息，避免数据库一次性查询并返回大量数据"""

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


# db.drop_all()
db.create_all()
print("创建完成")

@app.route('/one_to_one')
def one_to_more():
    user = User.query.filter_by(id=1).first()   #取出第一个与 [0]效果一致
    extension = UserExtension(school="南京大学")
    user.extension = extension

    db.session.add(user)
    db.session.commit()
    return "one to one 绑定成功"


if __name__ == '__main__':
    app.run(debug=True,port=10010)