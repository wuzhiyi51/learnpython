#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test-sorted.py
@Time    :   2019/06/21 15:22:18
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib

#直接插入排序
def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i]<array[j]:
                array.insert(j, array.pop(i))
                break
    return array

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i]>array[j]:
                array[i], array[j]=array[j], array[i]
    return array


def selection_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index=i
        for j in range(i+1, n):
            if alist[j]<alist[min_index]:
                min_index=j
        alist[min_index], alist[i]=alist[i], alist[min_index]

        

arr=[1,3,4,2,6,99,33,22,55,11]
print(bubble_sort(arr))
print(insert_sort(arr))
print(selection_sort(arr))