#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : format2.py

import json
import pandas as pd

from utils.response_code import response_state as state
from utils.path_os import *


def json2csv(json_path: str, csv_root: str) -> tuple[bool, str]:
    """
    将JSON文件转换为CSV文件
    
    :param json_path: JSON文件的路径
    :param csv_root: CSV文件保存的根目录
    :return: 元组(是否成功, CSV文件路径或错误信息)
    """
    # 读取JSON文件
    with open(json_path, 'r', encoding='utf-8') as file:
        file_data = json.load(file)

    # 获取文件名(不含扩展名)，使用path_os模块中的strip函数
    name = strip(json_path)["name"]
    # 生成CSV文件的完整路径，使用path_os模块中的full_path函数
    csv_path = full_path(base=csv_root, name=name, ext="csv")
    
    # 检查响应状态，使用response_code模块中的state函数
    if (_state := state(file_data["code"]))[0]:
        # 如果状态正常，提取airHourly数据
        airHourly = file_data["airHourly"]
        # 将数据转换为pandas DataFrame
        csvDF = pd.DataFrame(airHourly)
        # 将DataFrame保存为CSV文件，不包含索引
        csvDF.to_csv(csv_path, index=False, encoding='utf-8')
        return True, csv_path  # 返回成功状态和CSV文件路径
    else:
        return False, _state[1]  # 返回失败状态和错误信息

def dict2json(dictionary: dict, json_base: str, name: str) -> (bool, str):
    """
    将字典转换为JSON文件
    
    :param dictionary: 要转换的字典
    :param json_base: JSON文件保存的基础目录
    :param name: 文件名(不含扩展名)
    :return: 元组(是否成功, JSON文件路径或错误信息)
    """
    # 生成JSON文件的完整路径，使用path_os模块中的full_path函数
    json_path = full_path(base=json_base, name=name, ext="json")
    try:
        # 尝试将字典写入JSON文件
        with open(json_path, 'w', encoding='utf-8') as file:
            # 使用json.dump将字典转换为JSON格式并写入文件
            # ensure_ascii=False 确保非ASCII字符正确编码
            # indent=4 使JSON文件具有良好的缩进格式
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
        return True, json_path  # 返回成功状态和JSON文件路径
    except IOError as e:
        # 捕获IO错误（如文件无法写入）
        _error = f"写入文件时发生错误:\t{e}"
        IOError(_error)  # 抛出IOError异常
        return False, _error  # 返回失败状态和错误信息
    except TypeError as e:
        # 捕获类型错误（如字典中包含无法序列化的对象）
        _error = f"数据类型错误，无法序列化为JSON:\t{e}"
        TypeError(_error)  # 抛出TypeError异常
        return False, _error  # 返回失败状态和错误信息

