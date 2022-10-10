# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 17:45
# @Author  : jinjie
from wtforms import Form,StringField,ValidationError
from wtforms.validators import length,EqualTo
from wtforms.validators import email as EmailVailed


from db_model import EmailModel,UserModel


# 注册表单
class RegisterForm(Form):
    username = StringField(validators=[length(min=3,max=20)])
    email = StringField(validators=[EmailVailed()])
    vaild_code = StringField(validators=[length(min=4,max=4)])
    password = StringField(validators=[length(min=8,max=20)])
    password_confirm = StringField(validators=[EqualTo("password")])


    """ 重写对于验证码的验证，需要与数据库中的值进行对比 """
    def validate_vaild_code(self, field):
        captcha = field.data
        email = self.email.data
        #print("获取到的email",email)
        captcha_model = EmailModel.query.filter_by(email=email).first()
        #print("数据库中验证码为：",captcha_model.captcha)
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise ValidationError("验证码校验失败！")

    def validate_email(self,field):
        email = field.data
        #print("获取的邮箱为",email)
        user_email = UserModel.query.filter_by(email=email).first()
        if user_email:
            raise ValidationError("邮箱已经存在！")


# 登录表单
class LoginForm(Form):
    email = StringField(validators=[EmailVailed()])
    password = StringField(validators=[length(min=8, max=20)])