import os
from pathlib import Path
import pandas as pd

from core.config import settings


root_path = Path(__file__).resolve(strict=True).parent.parent


def read_file(path) -> pd.DataFrame:
    path = f"{root_path}{path}"
    df = pd.read_excel(path)
    return df


def save_file(data: pd.DataFrame, path):
    path = f"{root_path}{path}"
    data.to_excel(path)


def search_one_data():
    result = read_file(settings.FILE_PATH)
    df_filtered = result[result['is_completed'].isnull()]
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


def change_value(value, value_title, index, data: pd.DataFrame):
    """
    更改值，并保存文件
    :param value:
    :param index:
    :param data:
    :return:
    """
    print(index)
    data.at[index, value_title] = value
    save_file(data, settings.FILE_PATH)
    return data


if __name__ == '__main__':
    search_one_data()