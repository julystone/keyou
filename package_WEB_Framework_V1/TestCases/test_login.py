#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: july
# Time: 2019/7/31

import unittest

import yaml
from selenium import webdriver

from package_WEB_Framework_V1.PageObjects.index_page import IndexPage
from package_WEB_Framework_V1.PageObjects.login_page import LoginPage
from package_WEB_Framework_V1.TestData import common_data as cd
from package_WEB_Framework_V1.library.ddt import data, ddt

# 测试用例 = 测试对象的功能 + 测试数据
with open("../TestData/login_data.yaml", encoding="utf8") as f:
    s = yaml.safe_load(f)


@ddt
class TestInvest(unittest.TestCase):

    def setUp(self):
        # 打开浏览器，访问网址
        self.driver = webdriver.Chrome()
        self.driver.get(cd.global_data["website"])
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @data(*s["success"])
    def test_login_success(self, data):
        # 用例 = 登陆页的登陆功能 - 首页的 检查用户昵称存在的功能
        # 步骤
        LoginPage(self.driver).login(data["user"], data["pwd"])
        # 断言
        self.assertTrue(IndexPage(self.driver).check_username_exists())

    @data(*s["invalid_data"])
    def test_login_invalidInput(self, data):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login(data["user"], data["pwd"])
        # 断言
        self.assertEqual(data["errInfo"], lp.get_form_error_info())

    @data(*s["exp_snr"])
    def test_login_excSnr(self, data):
        # 步骤
        lp = LoginPage(self.driver)
        lp.login(data["user"], data["pwd"])
        # 断言
        self.assertTrue(data["errInfo"] in lp.get_page_center_error_info())


if __name__ == '__main__':
    unittest.main()
