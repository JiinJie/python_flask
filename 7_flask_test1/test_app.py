# -*- coding: utf-8 -*-
# @Time    : 2022/12/7 10:49
# @Author  : jinjie
# @File    : test_app.py
import sqlite3
# 使用 unittest进行flask的单元测试

from flask import abort
import unittest
from myapp import app,db




# sqlite数据库配置
DATABASE = 'test.db'



# 使用测试类,工厂模式
class MyappTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.app_context()
        app.config.update(
        TESTING=True,
            WTF_CSRF_ENABLED=False,
            # 使用默认的sqlite数据库 # 单元测试使用内存级别的sqlite会更快
            SQLALCHEMY_DATABASE_URI=f'sqlite:///:{DATABASE}:'
        )
        db.creat_all()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    #  测试用例
    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertIn('404 Error', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)

    def test_500_page(self):
        # create route to abort the request with the 500 Error
        @app.route('/500')
        def internal_server_error_for_test():
            abort(500)

        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 500)
        self.assertIn('500 Error', data)
        self.assertIn('Go Back', data)

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('flask is running', data)


if __name__ == '__main__':
    unittest.main()

