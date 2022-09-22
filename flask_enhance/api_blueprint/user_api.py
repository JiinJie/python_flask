# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 16:28
# @Author  : jinjie

from flask import Blueprint

#路由文件二
# 设置父级路由路径地址为 'user'
user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/list')
def user_list():
    return "用户列表"