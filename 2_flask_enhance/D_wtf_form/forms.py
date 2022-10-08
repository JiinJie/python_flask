# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:37
# @Author  : jinjie
import wtforms
from wtforms.validators import length,email



class LoginForm(wtforms.Form): #继承wtforms.form组件
    email_v = wtforms.StringField(validators=[length(min=5,max=20),email()])
    passwd_v = wtforms.StringField(validators=[length(min=5,max=20)])

