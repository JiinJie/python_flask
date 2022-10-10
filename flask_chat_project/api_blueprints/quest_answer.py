# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:42
# @Author  : jinjie

# question and answer model


from flask import Blueprint,g
from flask import render_template

bp_quest = Blueprint("quest",__name__,url_prefix="/")


@bp_quest.route('/index')
def index_page():
    if hasattr(g,"user"):
        print(g.user.username)  #打印user中的username属性
    return render_template("index.html")

