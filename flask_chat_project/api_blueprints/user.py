# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:42
# @Author  : jinjie

# user model

from flask import Blueprint, render_template, request,\
    url_for,redirect,jsonify,session,flash
from flask_mail import Message
import string,random
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from .forms import RegisterForm,LoginForm
from commons import mail, db
from db_model import EmailModel, UserModel



string_dict = string.ascii_uppercase + string.digits



bp_user = Blueprint("user",__name__,url_prefix="/user")


# 登录功能接口
@bp_user.route('/login',methods=['GET','POST'])
def login_page():
    if request.method == 'GET':
        return render_template("login_page.html")
    if request.method == 'POST':
        form = LoginForm(request.form)
        try:
            form.validate()
        except Exception as e:
            print("验证异常",e)
        if form.validate():  #在wtf的form中已经验证
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            # 数据库查找密码并解密验证，并将其作为session返回给用户
            if user and check_password_hash(user.password,password):
                session['user_id'] = user.id
                return redirect('/index')
            else:
                #使用flash在前端直接刷新提示信息
                flash("输入邮箱或密码错误！")
                return redirect(url_for('user.login_page'))
        else:
            flash("输入邮箱或密码格式不符！")
            return redirect(url_for('user.login_page'))




# 注册功能接口
@bp_user.route('/register',methods=['GET','POST'])
def register_page():
    if request.method == 'GET':
        return render_template("register_page.html")
    if request.method == 'POST':
        form = RegisterForm(request.form)
        #print(form.email)
        try:
            form.validate()
        except Exception as e:
            print("验证异常",e)
        if form.validate():  #在wtf的form中已经验证
            email = form.email.data
            vaild_code = form.vaild_code.data
            username = form.username.data
            password = form.password.data
            # 密码进行md5加密
            hash_password = generate_password_hash(password)
            #print(email,username,vaild_code,hash_password)
            user = UserModel(email=email,username=username,password=hash_password)
            db.session.add(user)
            db.session.commit()
            #return "register success"
            return render_template("register_to_login.html")
            # TODO （已完成）可以替换为跳转登录页，延时几秒后由前端跳转至登录页
        #验证成功跳转至登录页，失败则提示问题
        else:
            print("验证异常：",form.errors)
            #return jsonify({"code": "500","status": "failed","text": f"{form.errors}"})
            flash(f"注册失败  {form.errors}")
            #TODO 使用前后端接口返回，目前使用flash错误提示信息。且可读性较差
            #TODO 错误提示效果不好，应该在输入时实时提示相关信息
            return redirect(url_for("user.register_page"))



# 如何保存用户注册生成的验证码和映射关系？
# 使用redis/mencached/数据库（mysql）等...


# ”/email“测试邮箱功能是否正常，已替换为”/captcha“
# @bp_user.route('/email')
# def send_email():
#     message = Message(
#         subject="主题：邮箱测试",
#         recipients=['jiyinjie789@foxmail.com'],  #收件人
#         body="内容：验证码是QWER"
#     )
#
#     mail.send(message)
#     return "send success"

# 点击获取验证码接口
@bp_user.route('/captcha',methods=['POST'])
def vaild_email_code():
    random_code = "".join(random.sample(string_dict,4))  #将列表6个随机数转为字符串
    print("验证码: "+random_code)# 打印下code
    # 前端获取邮箱和输入的验证码
    user_email = request.form.get("email")
    # vaild_code = request.args.get("vaild_code")
    # 如果未填写邮箱则自动跳过
    if user_email:
        message = Message(
            subject="主题：邮箱测试",
            recipients=[user_email],  #收件人
            body=f"内容：您本次登录的验证码是：{random_code} 请勿告诉任何人！ "
        )

        mail.send(message)
        captcha_model = EmailModel.query.filter_by(email=user_email).first()
        if captcha_model:   #如果已经存在邮箱则更新captacha
            captcha_model.captcha = random_code
            captcha_model.create_time = datetime.now()  #只有第一次入库会自动写入，update更新时需要手动刷新
            db.session.commit()
        else:
            captcha_model = EmailModel(email=user_email,captcha=random_code)
            db.session.add(captcha_model)
            db.session.commit()

            #TODO 做成接口，前端返回发送成功后，继续填写相关信息，不需要直接返回页面
        return jsonify({"code": "200","status": "succcess","text": "发送成功"})

    else:
        return jsonify({"code": "400","status": "failed","text": "请填写邮箱!"})


# 注册提交按钮？
@bp_user.route('/submit',methods=['POST'])
def register_submit():
    user_email = request.args.get("email")
    vaild_code = request.args.get("vaild_code")
    password = request.args.get("password")


#TODO 个人中心页面设计
@bp_user.route('/userinfo')
def userinfo_page():
    return "#TODO 这是个人中心"


@bp_user.route('/logout')
def logout_page():
    # 清除session
    session.clear()
    return render_template("logout_page.html")