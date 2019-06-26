#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   select-sorted.py
@Time    :   2019/06/26 11:16:07
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib

# 从数列中找出最小数的函数
def findSmall(arr):
    smallest=arr[0]
    smallestIndex=0
    for i in range(1, len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallestIndex=i # 从数列中找出最小数的函数
    return smallestIndex

# 选择排序函数
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findSmall(arr)
        newArr.append(arr[smallest])
        arr.pop(smallest)
    return newArr

print(selectionSort([1, 1, 3, 5, 9, 7,2,3,33,55,11,22,33,222]))