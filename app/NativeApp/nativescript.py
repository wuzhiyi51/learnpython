#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   nativescript.py
@Time    :   2019/07/16 15:41:47
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib
from appium import webdriver
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.3'
        desired_caps['deviceName']='192.168.73.102:5555'
        desired_caps['appPackage']='com.android.calculator2'
        desired_caps['appActivity']='.Calculator'
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testAdd(self):
        number8=self.driver.find_element_by_id('digit8')
        number8.click()
        addoperation=self.driver.find_element_by_id('plus')
        number5=self.driver.find_element_by_id('digit5')
        number5.click()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()