#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : path_os.py

import os
from datetime import datetime, timedelta


def strip(file_path):
    base_dir = os.path.dirname(file_path)
    full_name = os.path.basename(file_path)
    name, ext = os.path.splitext(full_name)
    ext = ext.lstrip('.').lower()
    return {"dir": base_dir, "name": name, "ext": ext}


def full_path(base: str, name: str, ext: str) -> str:
    return os.path.join(base, f"{name}.{ext.lstrip('.')}")


def generate_file_list(start, end, loca, csv_base_root):
    start_date = datetime.strptime(start, "%Y%m%d")
    end_date = datetime.strptime(end, "%Y%m%d")

    # 检查日期范围是否恰好为7天
    date_range = (end_date - start_date).days + 1
    if date_range != 7:
        print(f"Warning: Date range is not 7 days. Adjusting to 7 days from start date.")
        end_date = start_date + timedelta(days=6)

    file_list = []
    current_date = start_date

    while current_date <= end_date:
        filename = f"{current_date.strftime('%Y%m%d')}_{loca}.csv"
        full_path = os.path.abspath(os.path.join(csv_base_root, filename))

        if os.path.exists(full_path):
            file_list.append(full_path)
        else:
            print(f"Warning: File {filename} not found in {csv_base_root}")

        current_date += timedelta(days=1)

    return file_list


if __name__ == '__main__':
    path = os.path.abspath("../src/data/json/20240814_SH.json")
    di = strip(path)
    print(full_path(f"{di['dir']}/", di["name"], ".csv"))
    print(full_path(f"{di['dir']}", di["name"], ".json"))
