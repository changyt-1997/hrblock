import os
from environs import Env
from pathlib import Path


env = Env()
# root_path = Path(__file__).resolve(strict=True).parent.parent
if os.path.exists(f"./.env"):
    env.read_env(f"./.env")


class Settings(object):
    S5PROXY_URL = env.str("S5PROXY_URL", None)
    ADS_POWER_URL = env.str("ADS_POWER_URL", None)
    ADS_POWER_KEY = env.str("ADS_POWER_KEY", None)
    ADS_GROUP_NAME = env.str("ADS_GROUP_NAME", "auto_register")
    BROWSER_KERNEL_CONFIG = env.str("BROWSER_KERNEL_CONFIG", "111")

    # file
    FILE_PATH = env.str("FILE_PATH", "/file/账号信息.xlsx")

    # tesseract
    TESSERACT_PATH = env.str("TESSERACT_PATH", r"D:\Program Files\Tesseract-OCR\tesseract.exe")

    # baidu orc
    APP_ID = env.str("APP_ID", None)
    API_KEY = env.str("API_KEY", None)
    SECRET_KEY = env.str("SECRET_KEY", None)

    POWER_RUN_COUNT = env.int("POWER_RUN_COUNT", 10)

    HEADLESS = env.int("HEADLESS", 0)

    PROXY_TYPE = env.str("PROXY_TYPE", "s5")
    PROXY = env.str("PROXY", "http")

    MOBILEHOP_HOST = env.str("MOBILEHOP_HOST")
    MOBILEHOP_PORT = env.str("MOBILEHOP_PORT")
    MOBILEHOP_USER = env.str("MOBILEHOP_USER")
    MOBILEHOP_PASSWORD = env.str("MOBILEHOP_PASSWORD")
    MOBILEHOP_REFRESH = env.str("MOBILEHOP_REFRESH")

    GUYS_HOST = env.str("GUYS_HOST")
    GUYS_PORT = env.str("GUYS_PORT")
    GUYS_USER = env.str("GUYS_USER")
    GUYS_PASSWORD = env.str("GUYS_PASSWORD")
    GUYS_REFRESH = env.str("GUYS_REFRESH")


settings = Settings()


