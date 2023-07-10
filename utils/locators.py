# coding=utf-8
# @Time : 2023/7/10 0:04
# @Author : shenbq

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    SEARCH_INPUT = (By.ID, 'search')


class LoginPageLocators(object):
    USERNAME = (By.ID, 'name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class ProfilePageLocators(object):
    AVATAR = (By.CLASS_NAME, 'avatar')
    USERNAME = (By.CLASS_NAME, 'username')