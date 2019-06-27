#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   date-test.py
@Time    :   2019/06/27 11:08:06
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib

import time
import datetime

#1、获取秒级时间戳与毫秒级时间戳
t=time.time()

print(t)    #原始时间数据
print(int(t))   #秒级时间戳
print(int(round(t*1000)))   #毫秒级时间戳

nowTime = lambda: int(round(t*1000))
print(nowTime())    #毫秒级时间戳，基于lambda


print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))    #日期格式化

#2、将日期转为秒级时间戳
dt='2019-01-01 10:40:30'
ts = int(time.mktime(time.strptime(dt,'%Y-%m-%d %H:%M:%S')))
print(ts)

#3、将秒级时间戳转为日期
ts=1546310430
dt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))
print(dt)


#计算当前日期是一年中的第几天
dt='2019-01-01'
nt=datetime.datetime.now().strftime('%Y-%m-%d')
print('nt=',nt)

dts=int(time.mktime(time.strptime(dt,'%Y-%m-%d')))  #秒级时间戳
nts=int(time.mktime(time.strptime(nt,'%Y-%m-%d')))  #秒级时间戳
ds=nts-dts
print(ds/86400) #86400秒等于一天