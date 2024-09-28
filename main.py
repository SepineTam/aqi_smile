#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : main.py

import os
from dotenv import load_dotenv

import time
from datetime import datetime, timedelta

from qweather.cities import get_cities, little_cities
from qweather.tTravel import get_air_quality

from utils.path_os import generate_file_list
from utils.day_range import get_date_range, missing_day
from utils.format2 import dict2json, json2csv

from semana.sort import sort_semana
from semana.qplot import *

# 加载环境变量
load_dotenv()

# 获取环境变量
API_KEY = os.getenv("API_KEY")
PUBLIC_ID = os.getenv("PUBLIC_ID")

# 设置相关的路径
ROOT_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(ROOT_PATH, "src/data")
FIGURES_BASE = os.path.join(ROOT_PATH, "src/figures")

CSV_BASE = os.path.join(DATA_PATH, "csv")
JSON_BASE = os.path.join(DATA_PATH, "json")
SEMANA_BASE = os.path.join(DATA_PATH, "semana")
SEMANA_FIGURE = os.path.join(FIGURES_BASE, "semana")


def gen_fig(): pass


def convert_semana(start_day, end_day, city):
    days = get_date_range(start_day, end_day)
    if len(days) == 7:
        semana_path = sort_semana(
            start_day=start_day, end_day=end_day, city=city,
            csv_root=CSV_BASE, out_base=os.path.join(SEMANA_BASE, city)
        )
        return semana_path
    else:
        print(f'{start_day} to {end_day} 不是一周，请更改')


def catch_data(start_day, end_day, cities=None, is_show: bool = False):
    print(end_day)
    print()
    print()
    if cities is None:
        cities = ['Shanghai']
    cities_name_list = []
    cities_data = get_cities(city_list=cities)
    days = get_date_range(start_day, end_day)

    for city in cities:
        for day in days:
            city_data = cities_data[city]

            for i in range(len(city_data)):
                location = city_data.loc[i, "Location_Name_EN"]
                location_id = city_data.loc[i, "Location_ID"]

                file_name = f"{day}_{location}"
                if os.path.exists((jf_path := os.path.join(JSON_BASE, f"{file_name}.json"))):
                    # 如果存在就pass，进行下一个
                    print(f'{day} of {location} is exist, next')
                    if os.path.exists((csv_path := os.path.join(CSV_BASE, f"{file_name}.csv"))):
                        _convert_flag, _convert_state = json2csv(jf_path, CSV_BASE)
                        if not _convert_flag:
                            print(_convert_state)
                    continue

                result: dict = get_air_quality(
                    loc=location_id, date=day, api_key=API_KEY
                )

                if (response_code := result['code']) == "200":
                    print(f"info:\nday: {day}\ncity: {location}")
                    if is_show:
                        print(f"state: {response_code}\n-----\nresult:\n{result}")
                    else:
                        print(f"state: {response_code}")
                    print("OK")

                    json_flag, save_state = dict2json(result, JSON_BASE, file_name)
                    if json_flag:
                        convert_flag, convert_state = json2csv(jf_path, CSV_BASE)
                        if not convert_flag:
                            print(convert_state)
                    else:
                        _error_code = result["code"]
                else:
                    print(f"state:\t{response_code}")


def main(start_day, end_day, cities):
    last_end = datetime.strptime(start_day, "%Y%m%d") - timedelta(days=1)
    last_start = last_end - timedelta(days=6)

    last_end_str = last_end.strftime("%Y%m%d")
    last_start_str = last_start.strftime("%Y%m%d")

    DETAIL_TYPES = ["no2", "so2", "co", "o3", "pm10", "pm2p5"]
    catch_data(start_day, end_day, cities)
    for city in cities:
        l_cities = little_cities(city_path='./qweather/cities_list.csv', mother_city=city)
        for l_city in l_cities:
            loca_csv = generate_file_list(start_day, end_day, l_city, CSV_BASE)
            semana_path = convert_semana(start_day, end_day, l_city)
            last_semana_path = convert_semana(last_start_str, last_end_str, l_city)
            if semana_path is not None:
                figure_name = f"{start_day}_{end_day}_{city}_{l_city}"
                # aqi_figure_path = qplot_aqi(data_path=semana_path, figure_base=SEMANA_FIGURE,
                #                             figure_name=figure_name, is_show=False)
                # print("Figure", aqi_figure_path, "is OK")
                for detail_type in DETAIL_TYPES:
                    details_figure_path = qplot_details(data_path=semana_path, last_data_path=last_semana_path,
                                                        figure_base=SEMANA_FIGURE, figure_name=figure_name,
                                                        d_type=detail_type, is_show=False)
                    if details_figure_path == "Wrong":
                        ValueError("Missing the path of last data!")
                    else:
                        print("Figure", details_figure_path, "is OK")


if __name__ == "__main__":
    count_begin = time.time()
    _cities = ['Jiangsu', 'Zhejiang', 'Shanghai', 'Beijing']
    ssd, end = missing_day(os.getenv("START_DAY"), os.getenv("END_DAY"))
    main(start_day=ssd, end_day=end, cities=_cities)
    count_end = time.time()
    print(f"{(time_use := count_end - count_begin):.2f}s")
