#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   quick-sort.py
@Time    :   2019/06/26 10:23:21
@Author  :   Wu ZhiYi 
@Version :   1.0
@Contact :   wuzhiyi51@gmail.com
@License :   (C)Copyright 2019-20120, wuzhiyi
@Desc    :   None
'''

# here put the import lib

#算法图解版、快速排序
def quickSort(arr):
    if len(arr) < 2:    # 数列只剩一个数的时候不需要排序
        return arr
    else:
        pivot = arr[0]  # 取第一个数作为基准
        less = []   #大于pivot的
        more = []   #小于pivot的

        for i in range(len(arr)-1):
            # 遍历除了第一个数以外的数，根据大小分别存入less和more数列
            if arr[i+1] < pivot:
                less.append(arr[i+1])
            else:
                more.append(arr[i+1])
        return quickSort(less) + [pivot] + quickSort(more)

print(quickSort([5, 7, 1, 4, 2, 9, 7,11,33,55,22,56]))