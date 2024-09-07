#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : tTravel.py

import os
import requests

from utils.format2 import *


def city(par):
    return f"https://geoapi.qweather.com/v2/city/lookup?{par}"


def get_air_quality(loc: str, date, api_key, lang=None):
    """
    获取aqi的数据，用的是和风天气的时光机
    :param loc: 地区的编码，如上海则为101020100
    :param date: 日期，YYYYMMDD格式，如20240901
    :param api_key: API_KEY，那一串字符
    :param lang: 语言，没看明白咋用，反正就这个语言
    :return:如果搞到了就返回json，如果没就返回报错
    """
    url = "https://api.qweather.com/v7/historical/air?"

    params = {"location": loc, "date": date, "key": api_key}

    if lang:
        params["lang"] = lang
    headers = {'Accept-Encoding': 'gzip'}
    if (response := requests.get(url, params=params, headers=headers)).status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"


if __name__ == '__main__':
    key = '66752592f2e4422180e280e17e198973'
    resp = get_air_quality(loc='101020100', date='20240901', api_key=key)
    print(resp)
