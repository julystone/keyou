#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: 键盘操作
# Author: 简
# Time: 2019/7/24

# 键盘操作
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("柠檬班", Keys.ENTER)

# driver.execute_script() # 执行js
