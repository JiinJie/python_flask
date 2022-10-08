# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:42
# @Author  : jinjie

# user model

from flask import Blueprint,render_template

bp_user = Blueprint("user",__name__,url_prefix="/user")


@bp_user.route('/login')
def login_page():
    return render_template("login_page.html")

@bp_user.route('/register')
def register_page():
    return render_template("register_page.html")