#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: index_page
# Author: 简
# Time: 2019/7/31

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:
    # 用户昵称定位
    user_loc = (By.XPATH, '//a[contains(text(),"我的帐户")]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_userName_exists(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.user_loc))
            return True
        except:
            return False
