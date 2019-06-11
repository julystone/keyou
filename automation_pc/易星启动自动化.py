from time import sleep

from appium import webdriver

sleep(5)
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'esunny.test'
desired_caps['appActivity'] = 'com.esunny.estar.StartActivity'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.set_page_load_timeout(5)

def is_element_present(locator):
    application = current_application()
    elements = self._element_finder.find(application, locator, None)
    return len(elements) > 0


if __name__ == "__main__":
    # if is_element_present("取消"):
    #     print("存在")
    # else:
    #     print("不存在")

    sleep(5)
    driver.find_element_by_id("esunny.test:id/toolbar_right_first").click()
    driver.find_element_by_accessibility_id("交易登录").click()
    driver.find_element_by_name("text:交易登录").click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first").click()

    driver.find_element_by_partial_link_text("图标设置").click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first").click()

    driver.find_element_by_partial_link_text("交易设置").click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first").click()

    driver.find_element_by_partial_link_text("价格预警").click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first").click()

    driver.find_element_by_partial_link_text("行情登录").click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first").click()

# try:
# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.widget.CheckBox")
# except:
# print("err")
# else:
# el1.click()
# el2 = driver.find_element_by_id("esunny.test:id/es_login_state_confirm_activity_confirm")
# el2.click()


# sleep(5)
# TouchAction(driver)   .press(x=752, y=929)   .move_to(x=475, y=929)   .release()   .perform()
# print("1")
# sleep(5)    
# TouchAction(driver)   .press(x=761, y=891)   .move_to(x=492, y=920)   .release()   .perform()
# print("1")    
# el3 = driver.find_element_by_id("esunny.test:id/textView_welcome_enterApp")
# el3.click()


# driver.find_element_by_id("id/es_login_state_confirm_activity_confirm").click()
