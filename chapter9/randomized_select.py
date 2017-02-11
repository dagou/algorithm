#encoding=utf-8
__author__ = 'zhuzhengwei'

import  random

def partition(A,p,q):
    pivot = A[q]
    i = p - 1
    for j in range(p,q):
        if A[j] < pivot:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp

    i += 1
    A[q] = A[i]
    A[i] = pivot
    return i

def randomizedPartition(A,p,q):
    i = random.randint(p,q)
    pivot = A[q]
    A[q] = A[i]
    A[i] = pivot

    return partition(A,p,q)

def randomizedSelect(A,p,q,i):
    if p == q:
        return A[p]
    r = randomizedPartition(A,p,q)
    k = r - p + 1
    if k == i:
        return A[r]

    elif i < k:
        return randomizedSelect(A,p,r-1,i)
    else:
        return randomizedSelect(A,r+1,q,i-k)

