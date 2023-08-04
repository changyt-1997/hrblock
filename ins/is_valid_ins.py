import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from ads_power import ads_power_instance, s5_proxy
from core.config import settings
from core.error_info import InsTryAgenException
from ins.read_file import search_one_data, change_value, search_index


class AutoOperateIns(object):

    def __init__(self, address=None):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", address)
        # options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(180)
        self.driver.get("https://www.instagram.com/accounts/password/reset/")

    def start_ins(self, phone):
        time.sleep(2)
        self.driver.get("https://www.instagram.com/accounts/password/reset/")
        self.driver.find_element(By.XPATH, '//input[@name="cppEmailOrUsername"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="cppEmailOrUsername"]').send_keys(int(phone))
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[5]/div').click()
        time.sleep(3)
        result = False
        # No users found  找不到用户  Please wait a few minutes before you try again.
        for i in range(5):
            result = self.is_exist("No users found")
            if self.is_exist("Please wait a few minutes before you try again."):
                raise InsTryAgenException("TryAgen")

            time.sleep(2)
            if result:
                return self.is_exist("No users found")
        return result

    def is_exist(self, str_to_find):
        # print(self.driver.page_source)
        if str_to_find in self.driver.page_source:
            print(f"检测：{str_to_find}  在当前页面")
            return True
        print(f"检测：{str_to_find}  不在当前页面")
        return False


def main():
    print(f"开始创建指纹浏览器")
    group_id = ads_power_instance.AdsPower.search_group_id(settings.ADS_GROUP_NAME)
    if settings.PROXY_TYPE == "s5":
        user_proxy_config = s5_proxy.get_proxy()
    elif settings.PROXY_TYPE == "guys":
        user_proxy_config = s5_proxy.get_proxy_guys()
    elif settings.PROXY_TYPE == "mobilehop":
        user_proxy_config = s5_proxy.get_proxy_mobilehop()
    else:
        user_proxy_config = None
    result, data = search_one_data()

    # 创建浏览器
    user_id = ads_power_instance.AdsPower.create_user(f'ins-{str(result["电话"])}', group_id, user_proxy_config)
    address = ads_power_instance.AdsPower.start_run_browser(user_id)
    power = AutoOperateIns(address)
    while True:
        if power.start_ins(result["电话"]):

            change_value("无效", "is_completed", search_index(result["电话"], data))
        else:
            change_value("有效", "is_completed", search_index(result["电话"], data))
        result, data = search_one_data()


if __name__ == '__main__':
    ins = AutoOperateIns()
    ins.start_ins("chang22321312")