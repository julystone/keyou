# -*-coding:utf8-*-


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('http://www.baidu.com')

driver.find_element_by_xpath('//div[@id="u1"]//a[text()="登录"]').click()

time.sleep(0.5)
WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')))

driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
# driver.quit()
