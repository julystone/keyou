# -*-coding:utf-8-*-
"""
****************************************
author:善待今天
time:2019/07/23 20:12
file:window_switch.py
software:PyCharm Community Edition
E-mail:2904504961@qq.com
Motivational motto: Do difficult things and get something
****************************************
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
print(driver.window_handles)
driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()
print(driver.window_handles)
# //a[text()="_腾讯课堂"]
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="_腾讯课堂"]')))
time.sleep(1)
wins = driver.window_handles
driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()
wins = driver.window_handles
print(driver.window_handles)
driver.switch_to.window(wins[-1])
