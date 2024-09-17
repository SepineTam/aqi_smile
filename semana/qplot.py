#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : qplot.py

import os
import re

import pandas as pd
import matplotlib.pyplot as plt

from utils.path_os import strip


def split_and_format_figure_name(figure_name):
    """
    解析并格式化图表名称
    
    :param figure_name: 原始图表名称字符串
    :return: 格式化后的日期、城市信息列表,或None(如果格式不匹配)
    """
    pattern = r'(\d{8})_(\d{8})_(.+)_(.+)'
    match = re.match(pattern, figure_name)
    if match:
        start_day, end_day, city, l_city = match.groups()

        # 格式化日期
        start_day_formatted = f"{start_day[:4]}.{start_day[4:6]}.{start_day[6:]}"
        end_day_formatted = f"{end_day[:4]}.{end_day[4:6]}.{end_day[6:]}"

        return [start_day_formatted, end_day_formatted, city, l_city]
    else:
        return None  # 如果输入字符串不匹配预期格式,返回None


def qplot_aqi(data_path, figure_base, figure_name, is_show=False):
    """
    生成AQI周变化图表
    :param data_path: CSV数据文件路径
    :param figure_base: 图表保存的基础目录
    :param figure_name: 图表文件名
    :param is_show: 是否显示图表(默认False)
    :return: 保存的图表文件路径
    """
    # 解析图表名称并创建保存目录
    figure_info = split_and_format_figure_name(figure_name)
    figure_base = os.path.join(figure_base, f"aqi/{figure_info[2]}/{figure_info[3]}")
    if not os.path.exists(figure_base):
        os.makedirs(figure_base)

    day_range = f"{figure_info[0]}-{figure_info[1]}"
    
    # 读取和处理数据
    week_data = pd.read_csv(data_path)
    week_data['pubTime'] = pd.to_datetime(week_data['pubTime'])

    week_data['hour'] = week_data['pubTime'].dt.hour
    week_data['day'] = week_data['pubTime'].dt.day_name()

    # 数据透视
    days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    pivot = week_data.pivot(index='hour', columns='day', values='aqi')
    pivot = pivot.reindex(columns=days_order)

    # 绘图
    plt.figure(figsize=(12, 6))
    for day in pivot.columns:
        plt.plot(pivot.index, pivot[day], label=day, marker='o')

    # 设置图表标题和轴标签
    plt.title(f"AQI Variation Throughout the week\n{day_range}")
    plt.xlabel("Hour of the Day")
    plt.ylabel("AQI")
    plt.legend(title="Day of week")
    # 设置网格和刻度
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.xticks(range(0, 24))
    plt.ylim(0, max(pivot.max()) + 10)
    plt.yticks(range(0, int(max(pivot.max()) + 10), 20))

    # 添加AQI等级线
    aqi_levels = [(0, 50, 'Good', 'green'),
                  (51, 100, 'Moderate', 'yellow'),
                  (101, 150, 'Unhealthy', 'orange')]

    for low, high, label, color in aqi_levels:
        plt.axhline(y=high, color=color, linestyle='--', label=label, alpha=0.5)
        plt.text(24, high, label, verticalalignment='center', horizontalalignment='center')

    # 保存和显示图表
    figure_path = os.path.join(figure_base, f"{figure_name}.png")
    plt.savefig(figure_path)
    if is_show:
        plt.show()
    plt.close()

    return figure_path


def qplot_details(data_path_list, figure_base, figure_name, d_type, is_show=False):
    figure_info = split_and_format_figure_name(figure_name)
    figure_base = os.path.join(figure_base, f"{d_type}/{figure_info[2]}/{figure_info[3]}")
    if not os.path.exists(figure_base):
        os.makedirs(figure_base)
    """plt"""
    # 保存和显示图表
    figure_path = os.path.join(figure_base, f"{figure_name}.png")
    plt.savefig(figure_path)
    if is_show:
        plt.show()
    plt.close()
    return figure_path


if __name__ == '__main__':
    qplot_aqi(data_path='../src/data/semana/20240829_20240904_Shanghai.csv',
              figure_base='../src/figures/semana/Shanghai/Shanghai/20240829_20240904.png',
              figure_name='20240829_20240904_Shanghai.png')
