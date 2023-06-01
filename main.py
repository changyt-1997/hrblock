import multiprocessing
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from core.error_info import ExistsNameException, NotDataException, SSNisUseException
from core.information import search_one_data, change_value, search_index
from ads_power import ads_power_instance, s5_proxy, auto_operate
from core.config import settings
from core.logger_info import logger


def created_ads_power():
    logger.info(f"开始创建指纹浏览器")
    group_id = ads_power_instance.AdsPower.search_group_id(settings.ADS_GROUP_NAME)
    if settings.PROXY_TYPE == "s5":
        user_proxy_config = s5_proxy.get_proxy()
    elif settings.PROXY_TYPE == "guys":
        user_proxy_config = s5_proxy.get_proxy_guys()
    elif settings.PROXY_TYPE == "mobilehop":
        user_proxy_config = s5_proxy.get_proxy_mobilehop()
    else:
        user_proxy_config = None
    info_one, info_data = search_one_data()
    info_email = info_one["邮箱----密码"]
    email, password = info_email.split("----")
    print(email, password)
    logger.info(f"正在为指纹浏览器创建数据：{info_email}")
    # puuhxwbmts@hotmail.com----Mc7FxjqR
    # 创建浏览器
    user_id = ads_power_instance.AdsPower.create_user(email, group_id, user_proxy_config)
    info_data = change_value(user_id, "user_id", search_index(info_email, info_data))
    result = ads_power_instance.AdsPower.start_run_browser(user_id)
    logger.info(f"启动指纹浏览器")
    logger.info(f"等待指纹浏览器连接网络.........")
    time.sleep(10)
    return result, info_data, info_one, user_id


def main(address, info_data, info_one, user_id):
    logger.info(f"开始运行程序")
    logger.info(f"浏览器地址信息：{address}")
    operate = auto_operate.AutoOperate(address)
    try:
        result = operate.run(info_one)
        change_value(result, "is_completed", search_index(info_one["邮箱----密码"], info_data))
        logger.info(f"************程序运行完成*************")
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
    except ExistsNameException as exists:
        logger.error(f"程序运行失败：{exists}")
        change_value("Name Error", "is_completed", search_index(info_one["邮箱----密码"], info_data))
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
        # main(address, info_data, info_one, user_id)
    except SSNisUseException as ssn_use:
        logger.error(f"程序运行失败：{ssn_use}")
        change_value("ssn_use Error", "is_completed", search_index(info_one["邮箱----密码"], info_data))
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
        # main(address, info_data, info_one, user_id)
    except StaleElementReferenceException as stale:
        logger.error(f"程序运行失败：{stale}")
        change_value("Network Error", "is_completed", search_index(info_one["邮箱----密码"], info_data))
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
    except NoSuchElementException as no_such:
        logger.error(f"程序运行失败：{no_such}")
        change_value("no_such Error", "is_completed", search_index(info_one["邮箱----密码"], info_data))
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
    except TimeoutException as no_such:
        logger.error(f"程序运行失败：{no_such}")
        change_value("Timeout Error", "is_completed", search_index(info_one["邮箱----密码"], info_data))
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])
    except Exception as e:
        logger.error(f"程序运行失败：{e}")
        change_value("Error", "is_completed", search_index(info_one["邮箱----密码"], info_data))
        ads_power_instance.AdsPower.stop_browser(user_id)
        ads_power_instance.AdsPower.delete_account([user_id])



if __name__ == '__main__':
    multiprocessing.freeze_support()
    try:
        while True:
            processes = []
            for i in range(settings.POWER_RUN_COUNT):
                try:
                    address, info_data, info_one, user_id = created_ads_power()
                except NotDataException as NotData:
                    logger.info(f"程序运行失败：{NotData}")
                    raise SystemExit
                p = multiprocessing.Process(target=main, args=(address, info_data, info_one, user_id,))
                processes.append(p)
                p.start()
            for p in processes:
                p.join()
                print(f"**************Worker {p.pid} exited with code {p.exitcode}*****************")
            time.sleep(1)
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("press input enter")
    # print(created_ads_power())
