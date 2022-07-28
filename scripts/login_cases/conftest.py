import time
import pytest
from page.login_page import LoginPage
from utils.web_base import UtileDriver


driver = None


@pytest.fixture(scope='class')
def setup_class(project_module_start):
    login_page = LoginPage()
    global driver
    driver = project_module_start
    yield driver, login_page
    UtileDriver.quit_web_driver()



@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()
    time.sleep(3)
