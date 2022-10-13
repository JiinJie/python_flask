# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 10:02
# @Author  : jinjie

from flask import g,redirect,url_for
from functools import wraps


# 写个装饰器判断用户是否登录，若未登录则跳转至登录页面
def login_required(func):
    # @wraps是必须的,否则会丢失传入装饰器的方法的属性（方法名会被替换为wrapper）
    @wraps(func)
    def wrapper(*args,**kwargs):
        if hasattr(g,"user"):
            return func(*args,**kwargs)
        else:
            return redirect(url_for("user.logout"))
    return wrapper

