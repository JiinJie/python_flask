# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 21:19
# @Author  : jinjie
# 前端页面在  .\templates\index.html 中

from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'random_key'  # 防止CSRF伪造请求


# ①前端实现的formb表单
@app.route('/login_page',methods=['GET','POST'])
def Login_page():
    return render_template('index.html')
    # 可以使用jinja2 （将文件及导入jinja2）

# ②flask实现的表单
from wtforms import StringField,PasswordField,SubmitField  # 输入内容，密码，提交
from flask_wtf import FlaskForm  # 前端对参数进行校验
from wtforms.validators import DataRequired,EqualTo  # 验证数据是否为空，是否相等


# 定义flask表单,继承自flask表单
class Register_form(FlaskForm):
    user_name = StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码',validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='再次输入密码',validators=[DataRequired('密码不能为空'),EqualTo('password')])
    submit_btn = SubmitField(label='提交')


@app.route('/register',methods=['GET','POST'])
def register():
    # 实例化刚才的flask表单对象
    form = Register_form()
    # return '1234'
    if request.method == 'GET':
        return render_template('register.html', form=form)  # 将表单传给前端页面
    if request.method == 'POST':
        if form.validate_on_submit():  # 如果验证通过才能提交
            user_name = request.form.get('user_name')
            password = request.form.get('password')
            password2 = request.form.get('password2')
            print(user_name,password,password2)
        else:
            print("输入参数校验失败")



if __name__ == '__main__':
    app.run(port=10010)