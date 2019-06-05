# @File   :   BasePage.py
# @Author :   July401
# @Date   :   2019/6/5
# @Email  :   july401@qq.com

import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

from package_102.common.R_r_caps import my_caps
from package_102.common.R_r_os import my_os


class Action(unittest.TestCase):
    """Base封装公用的方法"""

    def setUp(self) -> None:
        print("Begin".center(32, '-'))

    def tearDown(self) -> None:
        print('End'.center(32, '-'))

    def setUpClass(cls) -> None:
        caps = my_caps.read_caps()
        desired_caps = {'platformName': caps['platformName'], 'platformVersion': caps['platformVersion'],
                        'deviceName': caps['deviceName'], 'appPackage': caps['appPackage'],
                        'appActivity': caps['appActivity'], 'noSign': caps['noSign'], 'noReset': caps['noReset']}
        cls.driver = webdriver.Remote('http://' + caps['ip'] + ':' + str(caps['port']) + '/wd/hub', desired_caps)

    def find_element(self, loc):
        """重写查找元素方法"""
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception:
            print('%s 页面中未能找到%s 元素' % (self, loc))

    def clear_key(self, loc):
        """重写清空文本输入法"""
        time.sleep(3)
        self.find_element(loc).clear()

    def send_keys(self, loc, value):
        """重写在文本框中输入内容的方法"""
        self.clear_key(loc)  # 先调用
        self.find_element(loc).send_keys(value)

    def click_button(self, loc):
        """重写点击按钮的方法"""
        self.find_element(loc).click()

    def getScreenShot(self):
        """重写截图方法"""
        date2display = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        self.sh_file = my_os.readpath('screenshot') + "screenshot_" + date2display + ".png"
        self.driver.get_screenshot_as_file(self.sh_file)

    def get_windows_size(self):
        """获取屏幕大小"""
        windows_size = self.driver.get_window_size()
        return windows_size

    def swipe_windows(self, direction='down'):
        """滑动屏幕"""
        windows_size = self.driver.get_window_size()
        if direction == 'down':
            TouchAction(self.driver).press(x=0.5 * windows_size['width'], y=0.75 * windows_size['height']).move_to(
                x=0.5 * windows_size['width'], y=0.25 * windows_size['height']).release().perform()
        else:
            TouchAction(self.driver).press(x=0.5 * windows_size['width'], y=0.25 * windows_size['height']).move_to(
                x=0.5 * windows_size['width'], y=0.75 * windows_size['height']).release().perform()
