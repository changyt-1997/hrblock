import time

import requests
from core.config import settings
from core.logger_info import logger

def get_proxy():
    try:
        proxy = requests.get(settings.S5PROXY_URL).text
        host, port = proxy.split(':')
        data = {"proxy_type": "socks5", "proxy_host": host,
                "proxy_port": port.strip(), "proxy_user": "ExemplWinke@gmail.com",
                "proxy_password": "Qwe123321..", "proxy_soft": "other"}
        logger.info(f"成功获取s5代理")
        return data
    except Exception as e:
        logger.error(f"获取代理失败：{str(e)}")


def get_proxy_guys():
    """
209.248.72.241:8083
    :return:
    """

    data = {"proxy_type": "socks5", "proxy_host": "209.248.72.241",
            "proxy_port": "9093", "proxy_user": "pg_bgadkbc2.custom1",
            "proxy_password": "45201981fa", "proxy_soft": "other"}
    logger.info(f"成功获取guys代理")
    return data


def get_proxy_mobilehop():
    """
    :return:
    """
    requests.get("https://portal.mobilehop.com/proxies/2e9dc7da8d804394a6da31e737bc4b84/reset")
    time.sleep(5)
    data = {"proxy_type": "socks5", "proxy_host": "192.154.249.3",
            "proxy_port": "9000", "proxy_user": "proxy",
            "proxy_password": "CTu5YQY", "proxy_soft": "other"}
    logger.info(f"成功获取mobilehop代理")
    return data


