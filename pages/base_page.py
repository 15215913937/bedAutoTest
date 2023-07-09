# coding=utf-8
# @Time : 2023/7/9 23:11
# @Author : shenbq

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(*locator))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda d: d.find_elements(*locator))

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def input(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # 其他通用方法,例如alert处理、iframe切换等