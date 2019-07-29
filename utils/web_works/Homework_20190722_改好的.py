# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/24 16:06
file:Homework_20190722.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('腾讯课堂')
driver.find_element_by_id('su').click()

wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="_专业的在线教育平台(ke.qq.com)"]')))
driver.find_element_by_xpath('//a[text()="_专业的在线教育平台(ke.qq.com)"]').click()

wins = driver.window_handles
driver.switch_to.window(wins[-1])

loc = (By.XPATH, '//a[text()="登录"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (By.XPATH, '//a[text()="QQ登录"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (By.XPATH, '//iframe[@name="login_frame_qq"]')
# wait.until(EC.visibility_of_element_located(loc))
driver.switch_to.frame("login_frame_qq")
# wait.until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))

wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="帐号密码登录"]')))
driver.find_element_by_xpath('//a[text()="帐号密码登录"]').click()

print("pass")
