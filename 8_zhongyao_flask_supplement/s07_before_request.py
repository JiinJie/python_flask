# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 11:53
# @Author  : jinjie
# @File    : s07_before_request.py
# 三个钩子函数 before_request after_request errorhandler


from flask import Flask,render_template,request,session,redirect
from functools import wraps

app = Flask(__name__)
app.secret_key="sessionkey"  #用来加密session内容


# 登录验证，位获取到session时会自动跳转login页面
# def login_warp(f):
#     def nei(*args,**kwargs):
#         if session.get("user"):
#             ret = f(*args,**kwargs)
#             return ret
#         return redirect("/login")
#     return nei

"""不再使用装饰器，而是统一使用钩子函数before_request"""
@app.before_request  #如果有多个则按代码自上而下顺序执行
def get_session():
    # 如果路由已经是login就返回none，不用再次重定向，否则浏览器会因为多次重定向而报错
    if request.path == "/login":
        return None  #处理完成后必须返回None!!!!
    user = session.get("user")
    if user:
        return None
    else:
        return redirect("/index")

# 返回给用户前调用
@app.after_request # 如果有多个则按代码顺序由下而上执行输出
def ready_back1(res): #必须要一个参数接收response
    print("after1")
    # do action  to "res" value
    return res

@app.after_request
def ready_back2(res): #必须要一个参数接收response
    print("after2")
    # do action  to "res" value
    return res

@app.errorhandler(404)  #将code404重新定义，替换默认的404页面，返回定制内容
def errors(args): # args是 code_or_exception
    print(args)
    return "404,未找到页面"

@app.route('/index',methods=['GET','POST'],strict_slashes=False)
def index_page():
    if request.method == 'GET':
        return render_template('login_page.html')
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print(name,passwd)
        if name == "test" and passwd == "123456":
            session["user"] = name
            return render_template('homepage.html')
        else:
            return render_template("login_page.html",msg="账号或密码错误")

@app.route('/homepage',methods=['GET','POST'])
def homepage():
    if not session.get("user"): #判断是否有session,没有则直接跳转登录页面
        return redirect('/index')
    return render_template('homepage.html')


@app.route('/detail',endpoint="detail")
def detail():
    return render_template('detail.html')

"""# 默认添加多个login_warp时会报错
# 因为默认添加装饰器时，视图函数名称会发生改变，route中不允许有重名的视图函数
# 因此需要使用endpoint参数，使其不重复"""
@app.route('/userlist',endpoint="user_list")
def user_list():
    return render_template('userlist.html')


@app.route('/login',methods=['GET','POST'],endpoint="login")
def login():
    return redirect('/index')



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=11111,debug=True)
