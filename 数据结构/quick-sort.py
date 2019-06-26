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

def partition(arr, low, high):
    i = (low - 1) # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):
        # 当前元素小于或等于 pivot 
        if arr[j] <= pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 
for i in range(n): 
    print ("%d" %arr[i])




#算法图解版、快速排序
def quickSorted(arr):
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
        return quickSorted(less) + [pivot] + quickSorted(more)

print(quickSorted([5, 7, 1, 4, 2, 9, 7,11,33,55,22,56]))