import time

from locators.add_user_locators import AddUserLocators
from utils.web_base import WebJudgeExecution


class AddUserPage(WebJudgeExecution):
    # 添加用户
    def add_user(self, username, password, recur_password, position, name, root_password):
        self.switch_iframe(AddUserLocators.add_information_iframe)
        self.input_text(AddUserLocators.username, username)
        self.input_text(AddUserLocators.password, password)
        self.input_text(AddUserLocators.recur_password, recur_password)
        self.list_choose(AddUserLocators.position, position)
        self.input_text(AddUserLocators.name, name)
        self.input_text(AddUserLocators.root_password, root_password)
        time.sleep(5)
        self.click(AddUserLocators.save)
