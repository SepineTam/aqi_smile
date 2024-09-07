#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : save_json.py

import json


def save_json(json_data, filename):
    with open(filename, 'w') as f:
        json.dump(json_data, f)
        print('Saved json to {}'.format(filename))
        return filename
