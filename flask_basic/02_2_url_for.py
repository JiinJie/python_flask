# -*- coding: utf-8 -*-
# @Time    : 2022/9/9 11:19
# @Author  : jinjie

# 在开发过程中路由地址可能随时发生改变，因此需要通过函数反转直接跳转相关路由url
import json
from flask import Flask, url_for, jsonify

app = Flask(__name__)

books = {"01":"aaa","02":"bbb","03":"ccc"}
books01 = {{"id":"01","name":"aaa","url":"book/1"},
          {"id":"02","name":"bbb","url":"book/2"},
          {"id":"03","name":"ccc","url":"book/3"}}

@app.route("/book/detail<string:book_id>")
def book_detail(book_id):
    for key,value in books:
        if book_id == str(books[key]):
            return books[value]

    return f"{book_id}未找到"


@app.route("/book/list")
def book_list():
    for key,value in books01:
        books01['url'] = url_for("book_detail",book_id=books[value])

    return jsonify(books01[value])

