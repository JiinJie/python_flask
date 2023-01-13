# -*- coding: utf-8 -*-
# @Time    : 2023/1/13 15:19
# @Author  : jinjie
# @File    : s10_2_WTForms_use.py

# 建议查看enhance中的wtforms使用，这里代码量较多，比较冗余


from flask import Flask, views,render_template,request,session
from s10_1_WTForms_packages import LoginForm


app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key="sessionkey"  #用来加密session内容

@app.route("/")
def index():
    return "hello!"

# 编写一个视图类

class Index(views.MethodView):
    methods = ["GET","POST"]
    decorators = [aaa,bbb,ccc] # 装饰器，按照cba的顺序执行
    # 对应的请求方法
    def get(self):
        loginfm = LoginForm() #添加表单的验证
        return render_template("wtf_simple.html",fm=loginfm)

    def post(self):
        name = request.form.get("username")
        # 将传入的username进行后端校验
        loginfm = LoginForm(request.form)
        if not loginfm.validate():
            return render_template("wtf_simple.html",fm=loginfm)

        session["user"] = "test_session"
        return f"username '{name}' is saved"

app.add_url_rule("/index",endpoint="class_index",view_func=Index.as_view(name="index"))


if __name__ == '__main__':
    app.run(port=10010)

