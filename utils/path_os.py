#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : path_os.py

import os


def strip(file_path):
    base_dir = os.path.dirname(file_path)
    full_name = os.path.basename(file_path)
    name, ext = os.path.splitext(full_name)
    ext = ext.lstrip('.').lower()
    return {"dir": base_dir, "name": name, "ext": ext}


def full_path(base: str, name: str, ext: str) -> str:
    return os.path.join(base, f"{name}.{ext.lstrip('.')}")


if __name__ == '__main__':
    path = os.path.abspath("../src/data/json/20240814_SH.json")
    di = strip(path)
    print(full_path(f"{di['dir']}/", di["name"], ".csv"))
    print(full_path(f"{di['dir']}", di["name"], ".json"))
