import pytest
from selenium import webdriver
from utils.web_base import UtileDriver

driver = None


@pytest.fixture(scope='module')
def project_module_start():
    global driver
    driver = UtileDriver.get_web_driver()
    yield driver
