from core.information import search_one_data, change_value, search_index
from ads_power import ads_power, s5_proxy
from core.config import settings

group_id = ads_power.AdsPower.search_group_id(settings.ADS_GROUP_NAME)
user_proxy_config = s5_proxy.get_proxy()
info_email, info_data = search_one_data()
email, password = info_email.split("----")
print(email, password)
# puuhxwbmts@hotmail.com----Mc7FxjqR
user_id = ads_power.AdsPower.create_user(email, group_id, user_proxy_config)
info_data = change_value(user_id, "user_id", search_index(info_email, info_data), info_data)
result = ads_power.AdsPower.start_run_browser(user_id)
print(result)

