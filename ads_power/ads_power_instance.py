import requests
from core.config import settings


class AdsPower(object):
    request_status = {"url": "/status", "method": "get"}
    request_create_user = {"url": "/api/v1/user/create", "method": "post"}
    request_search_user = {"url": "/api/v1/user/list", "method": "get"}
    request_delete_user = {"url": "/api/v1/user/delete", "method": "post"}
    request_group_list = {"url": "/api/v1/group/list", "method": "get"}
    request_browser_start = {"url": "/api/v1/browser/start", "method": "get"}

    @staticmethod
    def get(request_data, data):
        url = f"{settings.ADS_POWER_URL}{request_data['url']}"
        param_data = {}
        if request_data["method"] == "post":
            param_data["json"] = data
        elif request_data["method"] == "get":
            param_data["params"] = data
        try:
            res = requests.request(method=request_data['method'], url=url, **param_data).json()
            if res["code"] != 0:
                print(f"请求失败：{request_data}, 数据：{data}, 返回数据：{res}")
        except Exception as e:
            print(f"请求失败：{request_data}, 数据：{data}")
            return None
        return res

    @staticmethod
    def create_user(email, group_id, user_proxy_config):
        data = {
            "name": email,
            "group_id": group_id,
            "user_proxy_config": user_proxy_config,
            "fingerprint_config": {
                "browser_kernel_config": {"version": settings.BROWSER_KERNEL_CONFIG, "type": "chrome"}}
        }
        result = AdsPower.get(AdsPower.request_create_user, data)
        return result['data']['id']

    @staticmethod
    def search_user(group_id, page_size=1):
        data = {
            "group_id": group_id,
            "page_size": page_size
        }
        result = AdsPower.get(AdsPower.request_search_user, data)
        return result['data']

    @staticmethod
    def search_group_id(group_name):
        data = {
            "group_name": group_name,
        }
        result = AdsPower.get(AdsPower.request_group_list, data)
        return result["data"]["list"][0]["group_id"]

    @staticmethod
    def start_run_browser(user_id):
        data = {
            "user_id": user_id,
            # "headless": 1
        }
        result = AdsPower.get(AdsPower.request_browser_start, data)
        return result["data"]["ws"]["selenium"]

    @staticmethod
    def delete_account(user_ids):
        data = {
            "user_ids": user_ids
        }
        result = AdsPower.get(AdsPower.request_delete_user, data)
        return result["msg"]


if __name__ == '__main__':
    group_id = AdsPower.search_group_id("auto_register")
    print(group_id)
    user_data = AdsPower.search_user(group_id, 10)
    print(user_data)
    user_ids = [i["user_id"] for i in user_data["list"]]
    AdsPower.delete_account(user_ids)
