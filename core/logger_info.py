import time
import sys
import os
from pathlib import Path

import loguru

sys.path.append(os.getcwd())

# log_time = time.strftime("%Y%m%d%H-%M", time.localtime())
# log_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), f'log\log:{log_time}.log')
root_path = Path(__file__).resolve(strict=True).parent.parent


class Logger(object):

    def __init__(self, need_log=True):
        self.my_logger = loguru.logger

        # 判断是否需要写入日志
        if need_log is True:
            self.my_logger.add(f"{root_path}/logs/run.log", encoding='utf-8')

    def info(self, content):
        self.my_logger.info(content)

    def debug(self, content):
        self.my_logger.debug(content)

    def error(self, content):
        self.my_logger.error(content)

    def critical(self, content):
        self.my_logger.critical(content)

    def warning(self, content):
        self.my_logger.warning(content)

    def success(self, content):
        self.my_logger.success(content)

    def trace(self, content):
        self.my_logger.trace(content)

    def traceback(self):
        import traceback
        self.my_logger.error(f'执行失败！！！失败信息：\n {traceback.format_exc()}')


logger = Logger()
