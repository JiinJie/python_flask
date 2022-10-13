# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 17:45
# @Author  : jinjie
from wtforms import Form,StringField,ValidationError,IntegerField
from wtforms.validators import length,EqualTo,DataRequired
from wtforms.validators import email as EmailVailed


from db_model import EmailModel,UserModel


# 注册表单
class RegisterForm(Form):
    username = StringField(validators=[length(min=3,max=8,message='用户名应在3-8位字符之间')])
    email = StringField(validators=[EmailVailed(message='邮箱格式错误')])
    vaild_code = StringField(validators=[length(min=4,max=4,message='验证码格式错误')])
    password = StringField(validators=[length(min=8,max=20,message='密码应在8-20位字符之间')])
    password_confirm = StringField(validators=[DataRequired(),EqualTo("password",message='密码不一致')])


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

    #email 方法中会对非空进行校验，如果使用用户名登录，vaildate会校验失败显示为False
    email = StringField(validators=[EmailVailed(message="邮箱格式错误")])
    #username = StringField(validators=[length(min=3,max=20,message="用户名格式错误")])
    password = StringField(validators=[length(min=8, max=20,message="密码格式错误")])

    # def validate_email(self,field):
    #     #TODO 尝试重写email的vaildate
    #     pass
        # email = field.data
        # #print("获取的邮箱为",email)
        # if email = :
        #     raise ValidationError("未填写邮箱！")



class CommitQuest(Form):
    quest_title = StringField(validators=[length(min=3,max=200)])
    quest_content = StringField(validators=[length(min=5,max=2000)])


class CommitAnswer(Form):
    reply_content = StringField(validators=[length(min=5,max=2000)])
    question_id = IntegerField(validators=[DataRequired()])
    #question_uuid = IntegerField(validators=[DataRequired()])