"""
1、移动到元素element对象的“底端”与当前窗口的“底部”对齐：
    driver.execute_script("arguments[0].scrollIntoView(false);",element)

2、移动到元素element对象的“顶端”与当前窗口的“顶部”对齐  ：
    driver.execute_script("arguments[0].scrollIntoView();",element)

3、移动到页面底部：
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

4、移动到页面顶部：
    driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

# 先移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

driver.find_element_by_id("kw").send_keys("12306", Keys.ENTER)

# 移动到官网对象与底部对齐
loc = (By.XPATH, '//a[text() = "官网"]/preceding-sibling::a')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)

driver.execute_script("arguments[0].scrollIntoView(false);", ele)

time.sleep(2)
driver.find_element(*loc).click()

# EC.new_window_is_opened()
wins = driver.window_handles
driver.switch_to.window(wins[-1])

loc = (By.XPATH, "//a[text()='中国铁路12306']")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
# driver.find_element(*loc).click()


# 12306 - js 修改日期输入框
loc1 = (By.XPATH, "//input[@id = 'fromStation']")
loc2 = (By.XPATH, "//input[@id = 'fromStationText']")
loc3 = (By.XPATH, "//input[@id = 'toStation']")
loc4 = (By.XPATH, "//input[@id = 'toStationText']")
WebDriverWait(driver, 35).until(EC.visibility_of_element_located(loc1))
for _ in range(4):
    exec(f"ele{_} = driver.find_element(*loc{_})")

# driver.execute_script("argument[0].readonly = false; argument[0].value = argument[1]", ele, "上海")

js = """
var a = document.getElementById("fromStationText");
var c = document.getElementById("fromStation");
a.value = "上海"
c.value = "SHH"
var b = document.getElementById("toStationText");
var d = document.getElementById("toStation");
b.value = "武汉";
d.value = "WHN";
"""
time.sleep(2)

driver.execute_script(js)

time.sleep(2)

loc = (By.XPATH, "//a[@id = 'search_one']")
WebDriverWait(driver, 35).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
