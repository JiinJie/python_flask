# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 20:23
# @Author  : jinjie
# @discribe :自定义转换器


from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)
# 自定义转换器继承自父类
class My_Re_Converter(BaseConverter):
    """
    自定义转换器类
    """
    def __init__(self,url_map,regex):
        # 重写init时需要调用部分父类方法，使用super，继承原来的init方法中部分内容
        super(My_Re_Converter,self).__init__(url_map)
        self.regex = regex

    def to_python(self,value):
        """
        父类方法功能已实现
        :param value:
        :return:
        """

        return value

# 将自定义的转换器类添加到flask应用中
app.url_map.converters['re'] = My_Re_Converter



"""
@app.route('/index/<re("1\d{10}"):value>')
首字母开头有10位
"""
@app.route('/index/<re("234"):value>')
def index(value):
    print(value)
    return 'hello'


if __name__ == '__main__':

    app.run(port=10010)
