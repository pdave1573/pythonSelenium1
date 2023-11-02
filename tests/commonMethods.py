from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from conftest import getDriver

class common:

    def getDriver(self):
        self.driver = getDriver()

    def openBrowser(self, setup, page):       # Setup is passing the driver instance
        self.driver = setup
        self.driver.get(page)

    @staticmethod
    def closeBrowser(self, setup):
        self.driver = setup
        self.driver.quit()

    def sendKeys(setup, element, value):
        driver = setup
        driver.find_element(element).clear()
        driver.find_element(element).send_keys(value)

    def click(setup,element, value):
        driver = setup
        driver.find_element(element).click()