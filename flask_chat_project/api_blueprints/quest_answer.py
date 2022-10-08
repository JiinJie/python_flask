# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:42
# @Author  : jinjie

# question and answer model


from flask import Blueprint
from flask import render_template

bp_quest = Blueprint("quest",__name__,url_prefix="/")


@bp_quest.route('/index')
def index_page():
    return render_template("index.html")
