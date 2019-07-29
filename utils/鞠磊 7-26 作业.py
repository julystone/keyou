# 每一个元素都有的四种操作：click、send_keys、text、get_attribute
# driver.find_element_by_id("kw").send_keys("柠檬班")
# # driver.find_element_by_id("su").click()
# # text = driver.find_element_by_id("su").text #
# # driver.find_element_by_id("su").get_attribute("class")

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

# 找到元素
ele = driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')
# 实例化ActionChains
ac = ActionChains(driver)
# 悬浮操作
ac.move_to_element(ele).click(ele)
# 执行鼠标操作
ac.perform()

loc = (By.XPATH, '//a[text()="高级搜索"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 先找到select元素
loc = (By.XPATH, '//select[@name="gpc"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
select_ele = driver.find_element(*loc)

# 实例化Select类
s = Select(select_ele)
s.select_by_index(4)  # 通过下标来选
time.sleep(1)
s.select_by_value("stf")  # 通过value属性来选值
time.sleep(1)
s.select_by_visible_text("最近一周")  # 通过文本值来选择
time.sleep(1)

# 键盘操作
loc = (By.ID, "adv_keyword")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
# 输入加减乘除
driver.find_element(*loc).send_keys(Keys.ADD, Keys.SUBTRACT, Keys.MULTIPLY, Keys.DIVIDE)
