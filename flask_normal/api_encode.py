# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 22:50
# @Author  : jinjie
import base64,hashlib,rsa
from flask import Flask,request

app = Flask(__name__)


# md5 加密
def passwd_md5(args):
    md5_value = hashlib.md5(str(args).encode("utf-8")).hexdigest()
    return md5_value


# base64加密
def passwd_base64(args):
    base64_value = base64.b64encode(str(args).encode("utf-8")).decode(encoding="utf-8")
    return base64_value


# md5加密注册接口
@app.route("/md5_login",methods=["GET","POST"])
def register_md5():
    # 获取前端接口入参
    username_1 = request.values.get("username")
    passwd_1 = request.values.get("passwd")

    new_passwd = passwd_md5(passwd_1)
    # 写入数据库的密码
    sql = f"insert into user_table(username,passwd) values('{username_1}','{new_passwd}')"


    if sql == "sql返回结果":
        return "register_success"
    else:
        return "register_failure"

# -------------------------------------------------
# RSA加解密
def create_key():
    (pubilc_key,private_key) = rsa.newkeys(1024)  ## 1024表示长度
    # 默认会生成一个流文件，需要保存至相应编码，然后格式化转义
    # print(pubilc_key)  # 流文件
    """
    PublicKey(119046745218505399532383566994032978650545070767292515251174696622304543239826180128903720179954862634264686613501797813945690185039811150383372229371244934984860945583911771135433553723494638066576155357347455160098927034423538221123624013789806078278451145353826459163443418099859964559591719076927192054891, 65537)
    """
    # print(pubilc_key.save_pkcs1()) ## pkcs1 编码
    """
    b'-----BEGIN RSA PUBLIC KEY-----\nMIGJAoGBAKmHN58RzA2mS8A0EiMFBSG9FH5q85YPQ7np1uH8MasOLDFI+RgSNx+V\nYy6kVKzfBLO5cXFsXzGE0mOXbnsN1qe2qZCQPtqhuVolce7FTddSqPmTl084xNgr\nk9RX4gr1Chzutb7f8LzhvLxrgHpqGY77BljF6dGvvuP668PWsjxrAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'
    """
    # print(pubilc_key.save_pkcs1().decode()) ##  格式化
    """
    -----BEGIN RSA PUBLIC KEY-----
    MIGJAoGBAKmHN58RzA2mS8A0EiMFBSG9FH5q85YPQ7np1uH8MasOLDFI+RgSNx+V
    Yy6kVKzfBLO5cXFsXzGE0mOXbnsN1qe2qZCQPtqhuVolce7FTddSqPmTl084xNgr
    k9RX4gr1Chzutb7f8LzhvLxrgHpqGY77BljF6dGvvuP668PWsjxrAgMBAAE=
    -----END RSA PUBLIC KEY-----
    """
    # 保存生成的密钥
    with open("./pubilc_key.pem","w+") as f:
        f.write(pubilc_key.save_pkcs1().decode())
    with open("./private_key.pem","w+") as f:
        f.write(private_key.save_pkcs1().decode())

# 通过公钥获取加密
def rsa_public():
    with open("./public.pem") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read().encode())
        byte_str = base64.b64encode()







if __name__ == '__main__':
    # app.run()
    create_key()

