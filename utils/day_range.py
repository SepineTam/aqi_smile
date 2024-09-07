#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : day_range.py

from datetime import datetime, timedelta


def get_date_range(start_day, end_day):
    start = datetime.strptime(start_day, '%Y%m%d')
    end = datetime.strptime(end_day, '%Y%m%d')

    date_range = []
    current = start
    while current <= end:
        date_range.append(current.strftime('%Y%m%d'))
        current += timedelta(days=1)

    return date_range


if __name__ == '__main__':
    date_range = get_date_range('20180101', '20180909')
    print(date_range)
