import time
from selenium.common.exceptions import StaleElementReferenceException
from core.error_info import ExistsNameException
from core.information import search_one_data, change_value, search_index
from ads_power import ads_power_instance, s5_proxy, auto_operate
from core.config import settings
from core.logger_info import logger


def created_ads_power():
    logger.info(f"开始创建指纹浏览器")
    group_id = ads_power_instance.AdsPower.search_group_id(settings.ADS_GROUP_NAME)
    user_proxy_config = s5_proxy.get_proxy_guys()
    info_one, info_data = search_one_data()
    info_email = info_one["邮箱----密码"]
    email, password = info_email.split("----")
    print(email, password)
    logger.info(f"正在为指纹浏览器创建数据：{info_email}")
    # puuhxwbmts@hotmail.com----Mc7FxjqR
    # 创建浏览器
    user_id = ads_power_instance.AdsPower.create_user(email, group_id, user_proxy_config)
    info_data = change_value(user_id, "user_id", search_index(info_email, info_data), info_data)
    result = ads_power_instance.AdsPower.start_run_browser(user_id)
    logger.info(f"启动指纹浏览器")
    logger.info(f"等待指纹浏览器连接网络.........")
    time.sleep(10)
    return result, info_data, info_one, user_id


def main():
    logger.info(f"开始运行程序")
    address, info_data, info_one, user_id = created_ads_power()
    logger.info(f"浏览器地址信息：{address}")
    operate = auto_operate.AutoOperate(address)
    try:
        result = operate.run(info_one)
        change_value(result, "is_completed", search_index(info_one["邮箱----密码"], info_data), info_data)
        logger.info(f"程序运行完成")
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
    except ExistsNameException:
        change_value("Name Error", "is_completed", search_index(info_one["邮箱----密码"], info_data), info_data)
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
        main()
    except StaleElementReferenceException:
        change_value("Network Error", "is_completed", search_index(info_one["邮箱----密码"], info_data), info_data)



if __name__ == '__main__':
    while True:
        main()


    # print(created_ads_power())
