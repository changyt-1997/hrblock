import os
from pathlib import Path
import pandas as pd
from core.logger_info import logger
from core.config import settings
from core.error_info import NotDataException

# root_path = Path(__file__).resolve(strict=True).parent.parent


def read_file(path) -> pd.DataFrame:
    path = f"./.{path}"
    df = pd.read_excel(path)
    return df


def save_file(data: pd.DataFrame, path):
    path = f"./.{path}"
    data.to_excel(path)


def search_one_data():
    result = read_file(settings.FILE_PATH)
    df_filtered = result[result['is_completed'].isnull() & result["user_id"].isnull()]
    if df_filtered.empty:
        raise NotDataException("未获取到数据")
    return df_filtered.iloc[0], result


def search_index(value, data: pd.DataFrame):
    """
    根据值查找索引
    :param value:
    :param data:
    :return:
    """
    index = data[data["邮箱----密码"] == value].index.values[0]
    return index


def change_value(value, value_title, index):
    """
    更改值，并保存文件
    :param value:
    :param index:
    :param data:
    :return:
    """
    print(index)
    data = read_file(settings.FILE_PATH)
    logger.info(f"更改数据：{value_title}-->{value}")
    data.at[index, value_title] = value
    save_file(data, settings.FILE_PATH)
    return data


if __name__ == '__main__':
    print(search_one_data())