# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 16:26
# @Author  : jinjie


from flask import Flask
from flask_enhance.api_blueprint.book_api import book_bp
from flask_enhance.api_blueprint.user_api import user_bp
from flask_enhance.api_blueprint.price_api import price_bp


app = Flask(__name__)

app.register_blueprint(book_bp)
app.register_blueprint(user_bp)
app.register_blueprint(price_bp)

if __name__ == '__main__':
    app.run(debug=True,port=10010)

