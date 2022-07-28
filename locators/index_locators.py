from selenium.webdriver.common.by import By

class IndexLocators:
    # 组织
    organize = (By.XPATH, '//*[@id="menuMainNav"]/li[@data-app="system"]/a')


    # 需要先切换至iframe
    add_user_iframe = (By.XPATH, '//*[@id="appIframe-system"]')
    # 添加用户
    add_user = (By.XPATH, '//*[@id="mainMenu"]/div/a[@class="btn btn-primary create-user-btn"]')
    