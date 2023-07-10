# coding=utf-8
# @Time : 2023/7/10 0:00
# @Author : shenbq

from base_page import BasePage
from utils.locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, username, password):
        self.input(LoginPageLocators.USERNAME, username)
        self.input(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

