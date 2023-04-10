import requests
from core.config import settings


def get_proxy():
    try:
        proxy = requests.get(settings.S5PROXY_URL).text
        host, port = proxy.split(':')
        data = {"proxy_type": "socks5", "proxy_host": host,
                "proxy_port": port.strip(), "proxy_user": "ExemplWinke@gmail.com",
                "proxy_password": "Qwe123321..", "proxy_soft": "other"}
        return data
    except Exception as e:
        print("获取代理失败：", str(e))


if __name__ == '__main__':
    result = get_proxy()
    print(result)
