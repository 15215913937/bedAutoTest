# coding=utf-8
# @Time : 2023/7/9 23:15
# @Author : shenbq
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import driver


class Helpers():
    @staticmethod
    def read_yaml(yaml_file_path):
        with open(yaml_file_path,'r') as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
    # @staticmethod
    # def write_yaml(yaml_file_path):
    #     with open(yaml_file_path,'a') as f:
    #         try:
    #             return