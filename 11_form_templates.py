# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 19:25
# @Author  : jinjie

from flask import Flask,render_template
from wtforms import StringField,PasswordField,SubmitField  #导入表单字段名
from flask_wtf import FlaskForm #导入flask表单
from wtforms.validators import DataRequired,EqualTo  #导入表格字段校验（非空等）

app = Flask(__name__)


# 定义表单模型类,继承flaskform
class Register(FlaskForm):
    user_name = StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    user_passwd = StringField(label='密码',validators=[DataRequired('密码不能为空')])
    user_passwd2 = StringField(label='密码',validators=[DataRequired('密码不能为空'),EqualTo(user_passwd)])
    submit = SubmitField(label='提交')
@app.route('/register')
def register():
    pass
    return render_template()
