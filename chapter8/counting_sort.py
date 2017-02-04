#encoding=utf-8
__author__ = 'zhuzhengwei'


# 只能处理元素在 0...k之间的元素
def countingSort(A, k):
    size = len(A)
    C = [0]*(k+1)
    B = [0]*size
    for i in range(0, size):
        C[A[i]] += 1

    for j in range(1,k+1):
        C[j] += C[j-1]

    for i in range(size-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B

arr = [45,3,1,44,32,6,71,5,89,12,19]

print countingSort(arr,89)