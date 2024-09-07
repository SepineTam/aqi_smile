#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : cities.py

import pandas as pd


def get_cities(city_list=None, level: str = 'city_A', city_path: str = 'qweather/cities_list.csv'):
    if city_list is None:
        city_list = ['Shanghai', 'Beijing']

    # A省级 & B市级
    level_dict: dict = {"city_A": "Adm1_Name_EN",
                        "city_B": "Adm2_Name_EN"}
    level_column = level_dict.get(level, "Adm1_Name_EN")

    df = pd.read_csv(city_path)  # 读取城市的csv文件
    city_dataframes = {}  # 创建城市字典，key为city list

    # df['Location_Name_EN'] = df['Location_Name_EN'].str.lower()  # location name 变为小写
    # df[level_column] = df[level_column].str.lower()  # adm1 name en 变成小写

    for city in city_list:
        city_df = df[df[level_column] == city][['Location_Name_EN', 'Location_ID', 'Adm1_Name_EN']]
        if not city_df.empty:
            city_df = city_df.reset_index(drop=True)
            city_dataframes[city.capitalize()] = city_df
    return city_dataframes


def little_cities(city_path, mother_city) -> list:
    cities_dict = get_cities(city_path=city_path)
    son_cities = []
    for city in cities_dict[mother_city]['Location_Name_EN']:
        son_cities.append(city)

    return son_cities


# TODO: 这个函数以后再写吧
def get_id(cities_dict):
    id_dict = {}
    for city, city_df in cities_dict.items():
        print(city)
        # print(city_df)
        for id in city_df['Location_ID']:
            print(id)


if __name__ == '__main__':
    get_id(cities_dict=get_cities(city_path='cities_list.csv'))
