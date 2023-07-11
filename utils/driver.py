# coding=utf-8
# @Time : 2023/7/9 23:14
# @Author : shenbq

from selenium import webdriver


class Driver:
    driver = None

    @staticmethod
    def get_driver():
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome()
        return Driver.driver

    @staticmethod
    def open(url):
        Driver.get_driver().get(url)

    @staticmethod
    def quit():
        if Driver.driver is not None:
            Driver.driver.quit()
            Driver.driver = None