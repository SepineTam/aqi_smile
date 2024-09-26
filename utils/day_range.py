#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : day_range.py

from datetime import datetime, timedelta


def get_day_range(days):
    """
    获取指定天数范围内的日期列表。

    :param days: 要获取的天数
    :return: 包含指定天数范围内日期的列表,格式为'YYYY-MM-DD'
    """
    # 获取当前日期
    today = datetime.now().date()

    # 生成日期列表
    date_list = [(today - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(days)]

    # 返回反转后的列表,使日期按升序排列
    return date_list[::-1]


def get_date_range(start, end):
    start_date = datetime.strptime(start, "%Y%m%d")
    end_date = datetime.strptime(end, "%Y%m%d")

    date_list = []
    current_date = start_date

    while current_date <= end_date:
        date_list.append(current_date.strftime("%Y%m%d"))
        current_date += timedelta(days=1)

    return date_list


def missing_day(start=None, end=None):
    # print(start, end)
    if start is not None and end is not None:
        return start, end

    elif start is None and end is not None:
        print("Missing start but exist end!\nGenerating end day...")
        end_date = datetime.strptime(end, "%Y%m%d")
        date_list = [(end_date - timedelta(days=x)).strftime('%Y%m%d') for x in range(7)]
        return date_list[-1], date_list[0]

    elif start is not None and end is None:
        print("Missing end but exist start!\nGenerating start day...")
        start_date = datetime.strptime(start, "%Y%m%d")
        date_list = [(start_date + timedelta(days=x)).strftime('%Y%m%d') for x in range(7)]
        return date_list[0], date_list[-1]
    else:
        print("Start and end date must exist one!\nUse the default end day.")
        end_date = datetime.today() - timedelta(days=1)
        date_list = [(end_date - timedelta(days=x)).strftime('%Y%m%d') for x in range(7)]
        return date_list[-1], date_list[0]


if __name__ == '__main__':
    today = '20240902'
    ssd, een = missing_day(end=today)
    print(ssd, een)
