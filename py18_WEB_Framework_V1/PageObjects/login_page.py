#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: login_page
# Author: 简
# Time: 2019/7/31

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
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

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, passwd):
        # 等待
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.user_loc))
        self.driver.find_element(*self.user_loc).send_keys(username)
        self.driver.find_element(*self.passwd_loc).send_keys(passwd)
        self.driver.find_element(*self.login_button_loc).click()

    def get_form_error_info(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.form_error_loc))
        return self.driver.find_element(*self.form_error_loc).text

    # 获取页面中间的提示信息
    def get_page_center_error_info(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.page_center_error_loc))
        return self.driver.find_element(*self.page_center_error_loc).text
