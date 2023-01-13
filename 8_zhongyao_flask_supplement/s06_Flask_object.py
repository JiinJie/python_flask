# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 11:18
# @Author  : jinjie
# @File    : s06_Flask_object.py
#  详解Flask的参数

from flask import Flask,render_template


# 指定静态文件夹路径和路由
"""  
static_folder是文件存放位置
static_url_path是文件夹对应路由访问地址  默认值为 "/static" 
static_host用于远程访问服务器的静态资源 （通常页面文件和静态资源在两台web服务器）通常与host_matching 一起使用默认为False

"""
app = Flask(__name__,static_folder="static123",static_url_path="/static")

"""Flask对象的所有参数
    import_name: str,
    static_url_path: t.Optional[str] = None,
    static_folder: t.Optional[t.Union[str, os.PathLike]] = "static",
    static_host: t.Optional[str] = None,
    host_matching: bool = False,
    subdomain_matching: bool = False,
    template_folder: t.Optional[str] = "templates",
    instance_path: t.Optional[str] = None,
    instance_relative_config: bool = False,
    root_path: t.Optional[str] = None,
"""


@app.route("/index")
def index():
    return render_template("rabbit.html")


if __name__ == '__main__':
    app.run(port=10011,debug=True)