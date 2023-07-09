# coding=utf-8
# @Time : 2023/7/9 23:14
# @Author : shenbq

from selenium import webdriver


class Driver:
    # 单例模式获取driver对象
    __instance = None

    def __init__(self):
        if Driver.__instance is None:
            Driver.__instance = webdriver.Chrome()
        else:
            raise Exception("Driver class is a singleton!")

    @staticmethod
    def get_driver():
        return Driver.__instance

    @staticmethod
    def quit_driver():
        if Driver.__instance:
            Driver.__instance.quit()
            Driver.__instance = None