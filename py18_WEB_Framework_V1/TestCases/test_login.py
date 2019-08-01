#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: 简
# Time: 2019/7/31

import unittest
from selenium import webdriver

from py18_WEB_Framework_V1.PageObjects.login_page import LoginPage
from py18_WEB_Framework_V1.PageObjects.index_page import IndexPage


# 测试用例 = 测试对象的功能 + 测试数据

class TestLogin(unittest.TestCase):

    def setUp(self):
        # 打开浏览器，访问网址
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # 用例 = 登陆页的登陆功能 - 首页的 检查用户昵称存在的功能
        # 步骤
        LoginPage(self.driver).login("18684720553", "python")
        # 断言
        self.assertTrue(IndexPage(self.driver).check_userName_exists())

    def test_login_noPasswd(self):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login("18684720553", "")
        # 断言
        self.assertEqual("请输入密码", lp.get_form_error_info())

    def test_login_wrongPasswd(self):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login("18684720000", "python")
        # 断言
        self.assertEqual("此账号没有经过授权，请联系管理员!", lp.get_page_center_error_info())
