from selenium.webdriver.common.by import By


class Login_locators:
    username = (By.ID, 'account')
    password = (By.NAME, 'password')
    login_btn = (By.ID, 'submit')
