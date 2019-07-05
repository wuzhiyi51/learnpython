#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2019/07/05 17:18:13
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib

import time, os
class App():
    def __init__(self, pagename, firstActivity):
        """构造方法"""
        self.pagename = pagename
        self.firstActivty= firstActivity
        self.content="" #执行命令的文本
        self.startTime="" #启动的时间

    def startApp(self):
        '''开启app'''
        cmd="adb shell am start -W -n "+self.pagename+self.firstActivty
        self.content = os.popen(cmd)

    def stopApp(self):
        '''停止APP'''
        cmd = "adb shell am force-stop "+self.pagename
        os.popen(cmd)

    def getStartTime(self):
        """获取启动时间"""
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return  self.startTime