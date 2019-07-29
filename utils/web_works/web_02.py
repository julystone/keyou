# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 14:01
# @Author  : 晴天
# @FileName: web_02.py
# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from selenium import webdriver

# browser = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver = webdriver.Chrome()

driver.get("https://ke.qq.com/")
# 窗口最大化
driver.maximize_window()
driver.find_element_by_xpath('//section[contains(@class,"banner-slide ")]//a[text()="登录"]').click()

driver.implicitly_wait(10)
# 点击QQ登录
driver.find_element_by_xpath('//a[contains(@class,"btns-enter-qq")]').click()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it('login_frame_qq'))

time.sleep(0.1)
# 点击QQ快捷登录
# driver.find_element_by_xpath('//span[@id="img_out_2397924730"]').click()
# 点击账户密码登录
driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()

id = "u"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
# 输入账户
# driver.find_element_by_id("u").send_keys("3230614498")
driver.find_element_by_id("u").send_keys("1223871051")
# driver.find_element_by_name("u")
time.sleep(0.1)
# 输入密码
# driver.find_element_by_name("p").send_keys("nmb123456")
driver.find_element_by_name("p").send_keys("ghshadiao0124")
time.sleep(0.1)
# 点击登录
driver.find_element_by_xpath('//input[@id="login_button"]').click()
