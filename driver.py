from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import pytest

class Base:
    @pytest.fixture()
    def set_up(self):
        path = 'chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(10)
        self.driver.get("https://app.dataheroes.pro/landing")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit() 