# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 21:26
# @Author  : jinjie


import os,time
from flask import Flask,request,redirect,flash,url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'H:\百度网盘'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# 创建文件上传接口1
@app.route('/upload_file',methods=['GET','POST'])
def upload_file():
    # 获取上传的文件
    files = request.files["media"]
    # 获取文件名
    filename = files.filename
    # 上传服务器，保存
    with open ("D:\\"+filename.split('.')[0]+"_"+str(int(time.time()))+"."+"filename.split('.')[1]","wb") as f:
        f.write(files.read())
    # 返回
    return filename+"上传成功！"



# 创建文件上传接口2
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/offical_upload', methods=['GET', 'POST'])
def offical_upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 自动重定向至下载页面可不需要
            #return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''



if __name__ == '__main__':
    app.run(port=10010)