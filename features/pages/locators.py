from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.XPATH, '//*[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="login-button"]')
