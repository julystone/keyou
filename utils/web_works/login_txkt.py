# -*-coding:utf-8-*-
"""
====================================
author:mazai
time:19-7-23
file:login_txkt.py
software:PyCharm Community Edition
E-mail:785038575@qq.com
====================================
"""
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 开启一个浏览器会话
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

print(driver.current_window_handle)
# 获取当前所有的窗口列表
wins = driver.window_handles
driver.maximize_window()

print("所有的窗口列表-0:", wins)

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()

wait = WebDriverWait(driver, 20)

wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="_腾讯课堂"]')))

driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()
wait.until(EC.new_window_is_opened(wins))

wins = driver.window_handles
print("所有窗口-1:", wins)

driver.switch_to.window(wins[-1])
loc = (By.XPATH, '//a[text()="登录"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
#  <i class="icon-font i-qq"></i>QQ登录
# <a href="javascript:void(0);" data-type="1" class="js-btns-enter btns-enter btns-enter-qq"> <i class="icon-font i-qq"></i>QQ登录</a>'/

loc = (By.XPATH, '//a[text()="QQ登录"]')
# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
# <div class="bottom hide" id="bottom_qlogin" style="display: block;"><a class="link" hidefocus="true" id="switcher_plogin" href="javascript:void(0);" tabindex="8">帐号密码登录</a>  <div id="q_low_login_box" title="为了确保你的信息安全，不建议在网吧等公共环境勾选此项" class="low_login" style=""><a class="checked" id="q_low_login_enable" href="javascript:void(0);" tabindex="9"></a> <label class="low_login_wording" id="q_low_login_wording">下次自动登录</label></div>   <span class="dotted" id="docs_dotted">|</span> <a href="https://ssl.ptlogin2.qq.com/j_newreg_url" class="link" target="_blank">注册新帐号</a>   <span class="dotted">|</span> <a class="link" id="feedback_qlogin" href="https://support.qq.com/products/14800" target="_blank">意见反馈</a>  </div>
driver.find_element(*loc).click()
# <a class="link" hidefocus="true" id="switcher_plogin" href="javascript:void(0);" tabindex="8">帐号密码登录</a>
loc = (By.XPATH, '//iframe[@name="login_frame_qq"]')
wait.until(EC.frame_to_be_available_and_switch_to_it(loc))

loc = (By.XPATH, '//div[@class="bottom hide"]//a[text()="帐号密码登录"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# loc = (By.XPATH, '//div[@id="q_low_login_box"]//a[@id="q_low_login_enable"][@checked]')
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
# driver.find_element(*loc).click()

# loc = (By.XPATH, '//div[@class="inputOuter"]//input[@id="u"]')
loc = (By.XPATH, '//input[@id="u"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
# driver.find_element(*loc).send_keys('785038575')
driver.find_element(*loc).send_keys('1223871051')

loc = (By.XPATH, '//div[@class="inputOuter"]//input[@id="p"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
# driver.find_element(*loc).send_keys("#password#")
driver.find_element(*loc).send_keys("ghshadiao0124")

loc = (By.XPATH, '//div[@class="submit"]//input[@id="login_button"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(10)
driver.quit()
