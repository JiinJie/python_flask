# -*- coding: utf-8 -*-
# @Time    : 2022/9/15 14:38
# @Author  : jinjie

from flask import Blueprint

#  ——————————正式编写代码时不同的blueprint应该分文件进行保存——————————
#路由文件一
# 设置二级路由路径地址为 'book'
bp1 = Blueprint('book',__name__,url_prefix='/book')
# list是子路由地址
@bp1.route('/list')
def book_list():
    return "图书列表"


#路由文件二
# 设置二级路由路径地址为 'user'
bp2 = Blueprint('user',__name__,url_prefix='/user')

@bp2.route('/list')
def user_list():
    return "用户列表"

#路由文件三
# 设置二级路由路径地址为 'price'
bp2 = Blueprint('price',__name__,url_prefix='/price')

@bp2.route('/list')
def price_list():
    return "价格列表"

