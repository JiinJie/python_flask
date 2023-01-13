# -*- coding: utf-8 -*-
# @Time    : 2023/1/13 14:57
# @Author  : jinjie
# @File    : s10_1_WTForms_packages.py
# WTForms 模板使用

from wtforms.fields import simple,core
from wtforms import Form,validators,widgets


# 登录功能
class LoginForm(Form):
    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=5,max=16,message="长度需5-16位"),
        ],
        # widget=widgets.TextInput(),StringField已有，可不写
        # render_kw 表示添加至前端页面的标签参数，是一个键值对
        render_kw={"class": "username_tag"}
    )

    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=6, max=16, message="长度需6-16位"),
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class": "password_tag"}
    )

# 注册功能
class RegisterForm(Form):
    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=5,max=16,message="长度需5-16位"),
        ],
        # widget=widgets.TextInput(),StringField已有，可不写
        # render_kw 表示添加至前端页面的标签参数，是一个键值对
        render_kw={"class": "username_tag"}
    )

    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=6, max=16, message="长度需6-16位"),
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class": "password_tag"}
    )

    repassword = simple.PasswordField(
        label="再次输入密码",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.EqualTo("password",message="两次密码不一致") #指定名称而不是对象
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class": "password_tag"}
    )

#########以下两个core属性已经无法使用，忽略
    #AttributeError: module 'wtforms.fields.core' has no attribute 'RadioField'
    gender = core.RadioField(
        label="性别"
    )

    hobby = core.SelectMultipleField(
        lable="爱好"
    )


