# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 11:21
# @Author  : jinjie

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Sqlconfig:
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    """flask配置参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    # 连接flaskdb前需创建该数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


# 添加配置至flask app
app.config.from_object(Sqlconfig)

# 将 SQLAlchemy 绑定至app
db = SQLAlchemy(app)

# create数据库 操作
class Article(db.Model):
    __tablename__ = "artcle"
    # ！！！ 使用pycharm 专业版会对数据库操作的进行相关自动补全
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) #id 自增，设为主键
    title = db.Column(db.String(200),nullable=False) # varchar 不超过200字符  不能为空
    content = db.Column(db.Text,nullable=False)  #使用text文本类型，string最多只能225个字符

# 将ORM映射转化为数据库中的表
db.create_all()

# insert 操作
@app.route('/article_insert')
def insert_article():
    # 添加数据 'insert table article value(xxx)'
    article = Article(title="测试标题",content="测试内容xxxxx") #id自增不需要手动插入
    # session执行语句
    db.session.add(article)
    # session提交操作
    db.session.commit()
    return "添加数据成功！"
    # 需要访问路由地址才会进行操作！！

# select 操作
@app.route('/article_select')
def select_article():
    """
    cls.query.filter(类名.属性名 条件操作符 条件) 过滤特定条件,返回的是query对象
    cls.query.filter_by(关键字参数对) 单条件查询,条件必须关键字参数,而且and连接
    """
    # filter_by  返回一个类列表对象
    # art_number_list = Article.query.filter_by(id=1)  #返回整个列表
    art_number = Article.query.filter_by(id=1)[0]  #取第一个值
    my_title = art_number.title  #取这个列表title列的值
    return f"操作成功  标题为：{my_title}  "

# update 操作
@app.route('/article_update')
def update_article():
    art_number = Article.query.filter_by(id=1)[0]  #取第一个值
    art_number.content = 'yyy'
    db.session.commit()
    return "id=1的content数据已更新"

# delete 操作
@app.route('/article_delete')
def delete_article():
    Article.query.filter_by(id=1).delete()
    db.session.commit()
    return "id=1的整条数据已删除"



@app.route('/')
def create_table():
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute('use flaskdb; desc artcle')
    return f"创建表成功 {result}"



if __name__ == '__main__':
    app.run(debug=True,port=10010)
