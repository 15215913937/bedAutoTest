# coding=utf-8
# @Time : 2023/7/9 23:15
# @Author : shenbq

import logging
import os.path


class Log:

    @staticmethod
    def get_logger():
        # 创建日志器
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # 创建处理器并添加格式器
        log_path = os.path.dirname(os.getcwd()) + '/logs/auto.logs'
        fh = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # 添加处理器到日志器
        logger.addHandler(fh)

        # 返回日志器
        return logger


# 使用示例
# my_logger = Log.get_logger()
# my_logger.info('This is a logs message')