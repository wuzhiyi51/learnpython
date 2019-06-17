#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   008.py
@Time    :   2019/06/14 14:54:09
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib
# 字典运算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price=min(zip(prices.values(), prices.keys())) #zip反转 k,v
print(min_price)

max_price=max(zip(prices.values(), prices.keys()))
print(max_price)