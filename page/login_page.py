import time

from utils.web_base import WebJudgeExecution
from locators.login_locators import Login_locators


class LoginPage(WebJudgeExecution):
    # 登录
    def login(self, username, password):
        self.input_text(Login_locators.username, username)
        self.input_text(Login_locators.password, password)
        time.sleep(5)
        self.click(Login_locators.login_btn)
        time.sleep(5)
