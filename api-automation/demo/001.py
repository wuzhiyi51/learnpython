#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   001.py
@Time    :   2019/06/20 17:46:58
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib
import json
import requests

data={'name': '张三', 'password': '123456', "male": True, "money": None}
str_data=json.dumps(data)
print(str_data)


url='http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=%E6%80%8E%E4%B9%88%E5%8F%88%E6%98%AF%E4%BD%A0'
req = requests.post(url)
print(req.text)
res_dict=req.json()
print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))# 重新转为文本


res_dict = {'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
f = open("demo1.json","w")
json.dump(res_dict, f)

#
f = open("demo2.json","r", encoding="utf-8")  # 文件中有中文需要指定编码
f_dict = json.load(f) # 反序列化将文件句柄转化为字典
print(f_dict['name']) # 读取其中参数
f.close()