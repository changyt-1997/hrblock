from ads_power.auto_operate import AutoOperate
from core.information import search_one_data, change_value, search_index
from ads_power import ads_power_instance, s5_proxy, auto_operate
from core.config import settings


def created_ads_power():
    group_id = ads_power_instance.AdsPower.search_group_id(settings.ADS_GROUP_NAME)
    user_proxy_config = s5_proxy.get_proxy_guys()
    info_one, info_data = search_one_data()
    info_email = info_one["邮箱----密码"]
    email, password = info_email.split("----")
    print(email, password)
    # puuhxwbmts@hotmail.com----Mc7FxjqR
    # 创建浏览器
    user_id = ads_power_instance.AdsPower.create_user(email, group_id, user_proxy_config)
    info_data = change_value(user_id, "user_id", search_index(info_email, info_data), info_data)
    result = ads_power_instance.AdsPower.start_run_browser(user_id)
    return result, info_data, info_one


if __name__ == '__main__':
    result, info_data, info_one = created_ads_power()
    print(result)
    # operate = AutoOperate(result)
    # try:
    #     operate.run(info_one)
    # except:
    #     operate.run(info_one)