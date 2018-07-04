from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin

from selenium.webdriver.common.by import By


class Browser(object):
    # def __init__(self):
    #     chromepath = '/usr/local/bin/chromedriver'  # path to chrome needs to be specified here or in PATH variable
    #     self.driver = webdriver.Chrome(chromepath)
    #     self.driver.maximize_window()

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def get_driver(self):
        return self.driver

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, page=''):
        """
        navigate webdriver to different pages
        """
        self.driver.get(urljoin(settings['base_url'], page.lower()))

    def get_url(self):
        return self.driver.current_url

    def find_by_xpath(self, selector):
        """
        find a page element in the DOM
        """

        return self.driver.find_element(By.XPATH, selector)
