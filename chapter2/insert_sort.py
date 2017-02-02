#encoding=utf-8
__author__ = 'zhuzhengwei'


def insertSort(arr):
    length = len(arr)
    for j in range(1,length):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key


arr = [45,3,1,44,32,6,71,5,89,12]

print '排序前:'
print arr

insertSort(arr)
print '排序后:'
print arr