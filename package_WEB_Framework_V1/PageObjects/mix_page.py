from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MixInPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_widget(self, loc):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))

    def get_widget(self, loc):
        return self.driver.find_element(*loc)
