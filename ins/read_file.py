import pandas as pd

from core.config import settings
from core.error_info import NotDataException


def read_file(path) -> pd.DataFrame:
    df = pd.read_excel(path)
    return df


def save_file(data: pd.DataFrame, path):
    data.to_excel(path, index=False)


def search_one_data():
    result = read_file(settings.INS_PATH)
    df_filtered = result[result['is_completed'].isnull()]
    if df_filtered.empty:
        raise NotDataException("未获取到数据")
    return df_filtered.iloc[0], result


def search_complete_one_data():
    result = read_file(settings.INS_PATH)
    df_filtered = result[result['ins_id'].isnull()]
    if df_filtered.empty:
        raise NotDataException("未获取到数据")
    return df_filtered.iloc[0], result


def search_valid_one_data():
    result = read_file(settings.INS_PATH)
    df_filtered = result[result['is_completed'] == "有效"]
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
    index = data[data["电话"] == value].index.values[0]
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
    data = read_file(settings.INS_PATH)
    print(f"更改数据：{value_title}-->{value}")
    data.at[index, value_title] = value
    save_file(data, settings.INS_PATH)
    return data

