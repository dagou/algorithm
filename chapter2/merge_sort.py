#encoding=utf-8
__author__ = 'zhuzhengwei'


def merge(left,right):
    leftLen = len(left)
    rightLen = len(right)
    r = []
    total = leftLen + rightLen
    i = 0
    j = 0
    for k in range(0, total):
        if i == leftLen and j == rightLen:
            break
        if i == leftLen:
            r.append(right[j])
            j += 1
            continue
        if j == rightLen:
            r.append(left[i])
            i += 1
            continue
        if left[i] <= right[j]:
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1

    return r

def merge_sort(arr):
    size = len(arr)
    if size == 1:
        return arr
    mid = size/2
    arr_left = arr[0:mid]
    arr_right = arr[mid:size]
    l = merge_sort(arr_left)
    r = merge_sort(arr_right)
    m = merge(l,r)
    return m


arr = [45,3,1,44,32,6,71,5,89,12,19]

print merge_sort(arr)
