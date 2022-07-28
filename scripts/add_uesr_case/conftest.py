import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage
from page.index_page import IndexPage
from page.add_user_page import AddUserPage
from utils.web_base import UtileDriver
driver = None


@pytest.fixture(scope='class')
def setup_class(project_module_start):
    add_user_page = AddUserPage()
    index_page = IndexPage()
    login_page = LoginPage()
    global driver
    driver = project_module_start
    login_page.login('root', 'tian159.')
    index_page.enter_add_user()
    yield add_user_page
    UtileDriver.quit_web_driver()


# @pytest.fixture()
# def refresh_page():
#     yield
#     # 判断弹出框是否存在
#     result = EC.alert_is_present()(driver)
#     # 如果存在就点击确定后在刷新
#     if result:
#         driver.switch_to.alert.accept()
#         driver.refresh()
#         time.sleep(3)
