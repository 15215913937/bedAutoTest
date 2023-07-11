# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/7/10 10:11
import time

import pytest
from pages.login_page import LoginPage
from utils.driver import Driver


class TestLogin:

    def setup_class(self):
        self.driver = Driver.driver
        self.login_page = LoginPage(self.driver)
        self.driver.open("http://bed.test.cnzxa.cn")

    def teardown_class(self):
        Driver.quit_driver()

    @pytest.mark.parametrize("username, password", [
        ("test123", "123456"),
        ("test456", "456789")
    ])
    def test_valid_login(self, username, password):

        self.login_page.login(username, password)
        return "success"
    #     assert self.login_page.is_login_successful()
    #
    # def test_invalid_username(self):
    #     self.login_page.login("wronguser", "123456")
    #     assert self.login_page.get_error_message() == "用户不存在"
    #
    # def test_invalid_password(self):
    #     self.login_page.login("test123", "wrongpass")
    #     assert self.login_page.get_error_message() == "密码错误"
