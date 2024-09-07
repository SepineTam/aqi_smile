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


def json2csv(json_path: str, csv_root: str) -> (bool, str):
    with open(json_path, 'r', encoding='utf-8') as file:
        file_data = json.load(file)

    name = strip(json_path)["name"]
    csv_path = full_path(base=csv_root, name=name, ext="csv")
    if (_state := state(file_data["code"]))[0]:
        airHourly = file_data["airHourly"]
        csvDF = pd.DataFrame(airHourly)
        csvDF.to_csv(csv_path, index=False, encoding='utf-8')
        return True, csv_path
    else:
        return False, _state[1]


def dict2json(dictionary: dict, json_base: str, name: str) -> (bool, str):
    json_path = full_path(base=json_base, name=name, ext="json")
    try:
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
            return True, json_path
    except IOError as e:
        _error = f"写入文件时发生错误:\t{e}"
        IOError(_error)
        return False, _error
    except TypeError as e:
        _error = f"数据类型错误，无法序列化为JSON:\t{e}"
        TypeError(_error)
        return False, _error

