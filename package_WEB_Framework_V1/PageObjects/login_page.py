#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: login_page
# Author: july
# Time: 2019/7/31

from selenium.webdriver.common.by import By

from package_WEB_Framework_V1.PageObjects.mix_page import MixInPage


class LoginPage(MixInPage):
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (By.XPATH, '//button')
    # 表单错误提示
    form_error_loc = (By.XPATH, '//div[@class="form-error-info"]')
    # 页面中间错误提示
    page_center_error_loc = (By.XPATH, '//div[@class="layui-layer-content"]')

    def login(self, username, passwd):
        # 等待
        self.wait_widget(self.user_loc)
        self.get_widget(self.user_loc).send_keys(username)
        self.get_widget(self.passwd_loc).send_keys(passwd)
        self.get_widget(self.login_button_loc).click()

    def get_form_error_info(self):
        self.wait_widget(self.form_error_loc)
        return self.get_widget(self.form_error_loc).text

    # 获取页面中间的提示信息
    def get_page_center_error_info(self):
        self.wait_widget(self.page_center_error_loc)
        return self.get_widget(self.page_center_error_loc).text
