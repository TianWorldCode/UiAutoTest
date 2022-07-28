from selenium.webdriver.common.by import By


class AddUserLocators:
    add_information_iframe = (By.XPATH, '//*[@id="appIframe-admin"]')
    username = (By.XPATH, '//*[@id="account"]')
    password = (By.XPATH, '//*[@id="password1"]')
    recur_password = (By.XPATH, '//*[@id="password2"]')
    name = (By.XPATH, '//*[@id="realname"]')
    root_password = (By.XPATH, '//*[@id="verifyPassword"]')
    # 职位选择
    position = (By.XPATH, '//select[@id="role"]/option[@title="{}"]')
    # 保存
    save = (By.XPATH, '//*[@id="submit"]')