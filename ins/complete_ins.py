import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ads_power import ads_power_instance, s5_proxy
from core.config import settings
from core.hotemail import get_mail_ins
from ins.read_file import change_value, search_index, search_complete_one_data


class AutoOperateIns(object):

    def __init__(self, address=None):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", address)
        # options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(180)
        self.driver.get("https://instagrambipasettlement.com/submit-claim")

    def start_ins(self, result):
        self.driver.find_element(By.XPATH, '//*[@id="skip-guard"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="first_name"]').send_keys(result["名"])
        self.driver.find_element(By.XPATH, '//*[@id="last_name"]').send_keys(result["姓"])
        self.driver.find_element(By.XPATH, '//*[@id="street_address_1"]').send_keys(result["地址"])
        # self.driver.find_element(By.XPATH, '//*[@id="street_address_2"]').send_keys(int(phone))
        self.driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(result["城市"])

        select_element = self.driver.find_element(By.XPATH, '//*[@id="state"]')
        select = Select(select_element)
        select.select_by_visible_text("Illinois")

        self.driver.find_element(By.XPATH, '//*[@id="zip_code"]').send_keys(str(int(result["zip"])))

        select_element = self.driver.find_element(By.XPATH, '//*[@id="country"]')
        select = Select(select_element)
        select.select_by_visible_text("United States")

        self.driver.find_element(By.XPATH, '//*[@id="email_address"]').send_keys(result["email"])
        self.driver.find_element(By.XPATH, '//*[@id="confirm_email_address"]').send_keys(result["email"])
        self.driver.find_element(By.XPATH, '//*[@id="instagram_username"]').send_keys(f'{result["名"]} {result["姓"]}')
        self.driver.find_element(By.XPATH, '//*[@id="instagram_phone"]').send_keys(str(int(result["电话"])))

        self.driver.find_element(By.XPATH, '//*[@id="former_street_address_1_0"]').send_keys(result["地址"])
        self.driver.find_element(By.XPATH, '//*[@id="former_city_1"]').send_keys(result["城市"])

        select_element = self.driver.find_element(By.XPATH, '//*[@id="former_state_2"]')
        select = Select(select_element)
        select.select_by_visible_text("Illinois")

        self.driver.find_element(By.XPATH, '//*[@id="former_zip_code_3"]').send_keys(str(int(result["zip"])))
        self.driver.find_element(By.XPATH, '//*[@id="signature"]').send_keys(f'{result["名"]} {result["姓"]}')

        print("切换iframe 1")
        # //*[@id="dst-payment"]/iframe[1]
        iframe = self.driver.find_element(By.XPATH, '//*[@id="dst-payment"]/iframe[1]')
        self.driver.switch_to.frame(iframe)
        #  //*[@id="payment"]/div/div/fieldset/div/div[1]/div/div[3]/button
        # self.driver.find_element(By.XPATH, '//*[@id="payment"]/div/div/fieldset/div/div[1]/div/div[3]/button').click()
        element = self.driver.find_element(By.XPATH, '//*[@id="payment"]/div/div/fieldset/div/div[1]/div/div[3]/button')
        self.driver.execute_script("arguments[0].click();", element)

        self.driver.switch_to.default_content()

        print("切换iframe 3")
        iframe = self.driver.find_element(By.XPATH, '//*[@id="dst-payment"]/iframe[3]')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/input').send_keys(result["email"])
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/button/span[1]').click()

        time.sleep(10)
        code = get_mail_ins(result["email"], result["password"])
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/input').send_keys(code)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/button').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/button').click()

        self.driver.switch_to.default_content()
        element = self.driver.find_element(By.XPATH, '//*[@id="submit-claim"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.driver.find_element(By.XPATH, '//*[@id="submit-claim"]').click()

        # /html/body/div[2]/div[2]/div/div[3]/button   /html/body/div[2]/div[2]/div/div[3]/button
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[3]/button').click()
        ins_id = self.driver.find_element(By.XPATH, '//*[@id="confirmation_correlation_id"]').text
        return ins_id

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
    result, data = search_complete_one_data()

    # 创建浏览器
    user_id = ads_power_instance.AdsPower.create_user(f'ins-complete-{str(result["电话"])}', group_id, user_proxy_config)
    address = ads_power_instance.AdsPower.start_run_browser(user_id)
    try:
        power = AutoOperateIns(address)
        ins_id = power.start_ins(result)
        change_value(ins_id, "ins_id", search_index(result["电话"], data))
    except:
        pass
    ads_power_instance.AdsPower.stop_browser(user_id)
    ads_power_instance.AdsPower.delete_account([user_id])


if __name__ == '__main__':
    ins = AutoOperateIns()
    ins.start_ins("chang22321312")
