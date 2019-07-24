# -*-coding:utf8-*-
"""
***************************
Author:Lillian
Date:2019/7/18
***************************
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(20)  # 等待元素存在，等待命令执行完成

driver.get('https://ke.qq.com/')

wait = WebDriverWait(driver, 10)  # 显性等待

wins = driver.window_handles
print(wins)

# driver.find_element_by_xpath('//div[@id="u1"]//a[text()="登录"]').click()
driver.find_element_by_id('js_login').click()
wait.until(EC.frame_to_be_available_and_switch_to_it)

loc0 = (By.XPATH, "//a[contains(@class, 'btns-enter-qq')]")
wait.until(EC.visibility_of_element_located(loc0))
driver.find_element(*loc0).click()

# 需要鼠标移动一下
# ActionChains(driver).move_by_offset(100, 300)



loc00 = (By.XPATH, "//a[@id='switcher_plogin']")
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc00))
driver.find_element(*loc00).click()

loc1 = (By.XPATH, '//input[@id="u"]')
wait.until(EC.visibility_of_element_located(loc1))
driver.find_element_by_xpath('//input[@id="u"]').send_keys('1223871051')

loc2 = (By.XPATH, '//input[@id="p"]')
wait.until(EC.visibility_of_element_located(loc2))
driver.find_element_by_xpath('//input[@id="p"]').send_keys('ghshadiao0124')

loc3 = (By.XPATH, '//input[@id="login_button"]')
wait.until(EC.visibility_of_element_located(loc3))
driver.find_element_by_xpath('//input[@id="login_button"]').click()

print(wins)

# loc = (By.XPATH, r"//p[@id='TANGRAM__PSP_10__footerULoginBtn']")
# wait.until(EC.visibility_of_element_located(loc))     # loc
# # wait.until(EC.visibility_of(driver.find_element(*loc)))  # element
# driver.find_element(*loc).click()
# EC.alert_is_present.
print("pass")
