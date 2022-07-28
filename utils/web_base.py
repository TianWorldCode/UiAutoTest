from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time
from selenium.webdriver.support import expected_conditions as EC

import config


class UtileDriver:
    _web_driver = None
    url = 'http://localhost/zentaopms/www/user-login.html'

    @classmethod
    def get_web_driver(self):
        if self._web_driver is None:
            self._web_driver = webdriver.Chrome()
            self._web_driver.maximize_window()
            self._web_driver.get(url=self.url)
        return self._web_driver

    @classmethod
    def quit_web_driver(self):
        self._web_driver.quit()
        self._web_driver = None


class Web(UtileDriver):

    def __init__(self):
        self.driver = UtileDriver.get_web_driver()

    def find_element(self, *location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


class WebJudgeExecution(Web):

    def input_text(self, location, text):
        element = self.find_element(*location)
        element.clear()
        element.send_keys(text)

    def click(self, location):
        element = self.find_element(*location)
        element.click()

    def list_choose(self, location, text):
        element = self.find_element(location[0], location[1].format(text))
        element.click()

    def switch_iframe(self, location):
        self.driver.switch_to.frame(self.find_element(*location))

    def back_iframe(self):
        self.driver.switch_to.default_content()

    def refresh_page(self):
        self.driver.refresh()

    def save_screenshot(self, title):
        # path = config.IMG_PATH + '-{0}-{1}.png'.format(p_name, time.time())
        allure.attach(self.driver.get_screenshot_as_png(), title, allure.attachment_type.PNG)

    def alert_is_present(self):
        result = EC.alert_is_present()(self.driver)
        # 如果存在就点击确定后在刷新
        if result:
            self.driver.switch_to.alert.accept()