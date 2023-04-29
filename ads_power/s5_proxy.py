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
    requests.get(settings.GUYS_REFRESH, timeout=10)
    time.sleep(10)
    data = {"proxy_type": "socks5", "proxy_host": settings.GUYS_HOST,
            "proxy_port": settings.GUYS_PORT, "proxy_user": settings.GUYS_USER,
            "proxy_password": settings.GUYS_PASSWORD, "proxy_soft": "other"}
    logger.info(f"成功获取guys代理")
    return data


def get_proxy_mobilehop():
    """
    :return:
    """
    requests.get(settings.MOBILEHOP_REFRESH, timeout=10)
    time.sleep(10)
    data = {"proxy_type": "socks5", "proxy_host": settings.MOBILEHOP_HOST,
            "proxy_port": settings.MOBILEHOP_PORT, "proxy_user": settings.MOBILEHOP_USER,
            "proxy_password": settings.MOBILEHOP_PASSWORD, "proxy_soft": "other"}
    logger.info(f"成功获取mobilehop代理")
    return data


