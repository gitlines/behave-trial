from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin


class Base(object):
    def __init__(self, base_url=settings['base_url']):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url = base_url

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, url=None, page=''):
        """
        navigate webdriver to different pages
        """
        url = url if url is not None else urljoin(self.base_url, page.lower())
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def submit(self, *locator):
        """
        click submit button
        """
        submit_button = self.driver.find_element(*locator)
        submit_button.click()

    def find_element(self, *locator):
        """
        find a page element in the DOM
        """

        return self.driver.find_element(*locator)
