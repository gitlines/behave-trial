from pages.base import Base
from pages.locators import *


class Login(Base):

    def login(self, usr, pw):
        username_field = self.find_element(*LoginPageLocators.USERNAME_FIELD)
        password_field = self.find_element(*LoginPageLocators.PASSWORD_FIELD)
        username_field.send_keys(usr)
        password_field.send_keys(pw)
        self.submit(*LoginPageLocators.SUBMIT_BTN)


