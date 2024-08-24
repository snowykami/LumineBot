# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/24 上午11:07
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : main.py.py
@Software: PyCharm
"""

from liteyuki import LiteyukiBot
from liteyuki.config import load_config_in_default

if __name__ == "__main__":
    bot = LiteyukiBot(**load_config_in_default())
    bot.run()
