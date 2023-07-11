# coding=utf-8
# @Time : 2023/7/9 23:15
# @Author : shenbq

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import driver


class Helpers():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def input(self, locator, text):
        self.wait_for_element(locator).clear()
        self.wait_for_element(locator).send_keys(text)

    # 使用示例


# from locators import MainPageLocators
#
# helpers = Helpers(driver)
# helpers.click(MainPageLocators.LOGIN_BTN)
# helpers.input(MainPageLocators.SEARCH_BOX, "Automation")