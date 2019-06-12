#!/usr/bin/env python
#-*-code: utf-8-*-

#lambda
g=lambda x:x*2
print g(3)

print (lambda x:x*3)(3)

from selenium import webdriver
import time

dr=webdriver.Firefox()
url='http://mail.sina.com.cn'
dr.get(url)

dr.find_element_by_id('freename').send_keys('wuzhiyi51@sina.com')
time.sleep(2)
dr.find_element_by_id('freepassword').send_keys('wuzhiyi541')
dr.find_element_by_class_name('loginBtn').click()

time.sleep(10)
dr.quit()