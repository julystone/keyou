from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://ke.qq.com/')

wait = WebDriverWait(driver, 10)  # 显性等待


def my_find(loc):
    wait.until(EC.visibility_of_element_located(loc))
    return driver.find_element(*loc)


my_find((By.ID, 'js_login')).click()

my_find((By.XPATH, "//a[contains(@class, 'btns-enter-qq')]")).click()

wait.until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))

my_find((By.XPATH, "//a[@id='switcher_plogin']")).click()

my_find((By.XPATH, '//input[@id="u"]')).send_keys('1223871051')

my_find((By.XPATH, '//input[@id="p"]')).send_keys('ghshadiao0124')

my_find((By.XPATH, '//input[@id="login_button"]')).click()

print("pass")
