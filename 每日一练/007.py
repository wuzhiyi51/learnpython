#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   007.py
@Time    :   2019/06/14 14:48:40
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib
from collections import OrderedDict

#字典排序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
#json序列
import json
json.dumps(d)