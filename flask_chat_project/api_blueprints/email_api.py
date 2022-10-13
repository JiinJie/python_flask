# -*- coding: utf-8 -*-
# @Time    : 2022/10/13 14:12
# @Author  : jinjie


from flask import Blueprint,jsonify,current_app,request


bp_backact = Blueprint("backact",__name__,url_prefix="/backact")


@bp_backact.route('/')
def test_backact():
    return "backact_model is running"


# ”/email“测试邮箱功能是否正常，已替换为”/captcha“
@bp_backact.route('/email')
def send_email():
    # message = Message(
    #     subject="主题：邮箱测试",
    #     recipients=['jiyinjie789@foxmail.com'],  #收件人
    #     body="内容：验证码是QWER"
    # )
    try:
        # 需要从前端页面获取mail的值

        email = request.args.get("mail")
        subject = "邮箱主题"
        body = "邮箱内容"
        current_app.celery.send_task("send_mail", (email, subject, body))
        return jsonify("success")
    except Exception as e:
        print(e)
        return jsonify("fail")




