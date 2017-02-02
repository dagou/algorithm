#encoding=utf-8
__author__ = 'zhuzhengwei'


def bubbleSort(arr):
    size = len(arr)
    for i in range(0,size-1):
        for j in range(size-1,i,-1):
            if arr[j] < arr[j - 1]:
                ex = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = ex

arr = [45,3,1,44,32,6,71,5,89,12,19]

bubbleSort(arr)

print arr