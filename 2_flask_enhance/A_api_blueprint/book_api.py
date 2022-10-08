# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 16:28
# @Author  : jinjie
from flask import Blueprint

#  ——————————正式编写代码时不同的blueprint应该分文件进行保存——————————
#路由文件一
# 设置父级路由路径地址为 'book'
book_bp = Blueprint('book',__name__,url_prefix='/book')

@book_bp.route('/list')
def book_list():
    return "图书列表"
