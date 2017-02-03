#encoding=utf-8
__author__ = 'zhuzhengwei'


def partition(A,p,q):
    pivot = A[q]
    i = p - 1
    for j in range(p,q):
        if A[j] < pivot:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp

    A[q] = A[i+1]
    A[i+1] = pivot

    return i+1

def quickSort(A, p, q):
    if p < q:
        r = partition(A, p, q)
        quickSort(A,p,r-1)
        quickSort(A,r+1,q)


arr = [45,3,1,44,32,6,71,5,89,12,19]

quickSort(arr,0,len(arr)-1)

print arr