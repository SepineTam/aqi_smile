#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : load_env.py

import os
import sys

from dotenv import load_dotenv


def load_env(env_name):
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    value = os.getenv(env_name)

    # Check if environment variables are present
    if not value:
        raise ValueError(f"Environment variables {env_name} are missing.")

    # Return environment variables as dictionary
    return {
        f"{env_name}": value
    }


def load_all(): pass


if __name__ == "__main__":
    print(load_env("API_KEY"))
