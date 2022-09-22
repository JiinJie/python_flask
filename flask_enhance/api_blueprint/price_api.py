# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 16:29
# @Author  : jinjie
from flask import Blueprint

#路由文件三
# 设置父级路由路径地址为 'price'
price_bp = Blueprint('price',__name__,url_prefix='/price')

@price_bp.route('/list')
def price_list():
    return "价格列表"