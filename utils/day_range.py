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

# 示例使用
if __name__ == '__main__':
    # 获取过去7天的日期范围
    print(get_day_range(7))
