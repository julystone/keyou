from selenium.webdriver.common.by import By

from package_WEB_Framework_V1.PageObjects.mix_page import MixInPage


class IndexPage(MixInPage):
    # 用户昵称定位
    user_loc = (By.XPATH, '//a[contains(text(),"我的帐户")]')

    def check_username_exists(self):
        try:
            self.wait_widget(self.user_loc)
            return True
        except:
            return False
