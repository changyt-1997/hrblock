import os
from environs import Env
from pathlib import Path


env = Env()
root_path = Path(__file__).resolve(strict=True).parent.parent
if os.path.exists(f"{root_path}/.env"):
    env.read_env(f"{root_path}/.env")


class Settings(object):
    S5PROXY_URL = env.str("S5PROXY_URL", None)
    ADS_POWER_URL = env.str("ADS_POWER_URL", None)
    ADS_POWER_KEY = env.str("ADS_POWER_KEY", None)
    ADS_GROUP_NAME = env.str("ADS_GROUP_NAME", None)
    BROWSER_KERNEL_CONFIG = env.str("BROWSER_KERNEL_CONFIG", "111")

    # file
    FILE_PATH = env.str("FILE_PATH", "/file/账号信息.xlsx")


settings = Settings()


