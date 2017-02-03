#encoding=utf-8
__author__ = 'zhuzhengwei'


def violence(A,B):
    aRowLen = len(A)
    aColLen = len(A[0])
    bRowLen = len(B)
    bColLen = len(B[0])

    C = [[0 for x in range(bColLen)] for x in range(aRowLen)]

    if aColLen != bRowLen:
        raise Exception('Matrix can not multiple')

    for i in range(0, aRowLen):
        for j in range(0,bColLen):
            C[i][j] = 0
            for k in range(0,aColLen):
                C[i][j] += (A[i][k] * B[k][j])

    return C






A = [[1,2,3],[3,4,5],[3,1,2],[4,1,2]]

B = [[2,1],[2,2],[5,2]]

print violence(A,B)