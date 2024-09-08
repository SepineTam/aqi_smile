#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : sort.py

import os
import pandas as pd

from utils.day_range import get_date_range


class DayDate:
    def __init__(self, date, location_code, root):
        self.date = date
        self.location_code = location_code
        self.root = root

        self.file_path = os.path.join(self.root, f"{self.date}_{self.location_code}.csv")
        self.data = self._load_csv()

    def _load_csv(self) -> pd.DataFrame:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"CSV file not found: {self.file_path}")
        return pd.read_csv(self.file_path)


def sort_semana(start_day, end_day, csv_root, city, out_base=None):
    csv_root = os.path.abspath(csv_root)
    if out_base is None:
        out_base = os.path.join(csv_root, f'../semana/{city}')
    os.makedirs(out_base, exist_ok=True)
    out_path = os.path.join(out_base, f'{start_day}_{end_day}_{city}.csv')

    if os.path.exists(out_path):
        print(f'{out_path} already exists')
        return os.path.abspath(out_path)
    week = get_date_range(start=start_day, end=end_day)
    days: list[DayDate] = [DayDate(date, city, csv_root) for date in week]
    semana_data = pd.concat([day.data for day in days], ignore_index=True)
    semana_data.to_csv(out_path, index=False)

    return os.path.abspath(out_path)


if __name__ == '__main__':
    print(sort_semana(start_day='20240829', end_day='20240904', csv_root='../data/csv', city='Shanghai'))
