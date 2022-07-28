from locators.index_locators import IndexLocators
from utils.web_base import WebJudgeExecution


class IndexPage(WebJudgeExecution):

    # 组织 ==> 添加用户
    def enter_add_user(self):
        self.click(IndexLocators.organize)
        self.switch_iframe(IndexLocators.add_user_iframe)
        self.click(IndexLocators.add_user)
        self.back_iframe()