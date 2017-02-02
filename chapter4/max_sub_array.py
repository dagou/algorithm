#encoding=utf-8
__author__ = 'zhuzhengwei'


def violence(prices):
    maxVal = 0
    leftIdx = 0
    rightIdx = 0
    size = len(prices)
    for i in range(0,size-1):
        for j in range(i+1,size):
            if maxVal < (prices[j] - prices[i]):
                maxVal = (prices[j] - prices[i])
                leftIdx = i
                rightIdx = j
    return (leftIdx, rightIdx, maxVal)

def diff(prices):
    diffs = []
    size = len(prices)
    for i in range(0, size -1):
        diffs.append(prices[i+1]-prices[i])
    return diffs

def maxSubArray(prices):
    diffs = diff(prices)
    size = len(diffs)
    maxVal = 0
    for i in range(0,size - 1):
        for j in range(i+1, size):
            sumVal = 0
            for k in range(i,j+1):
                sumVal += diffs[k]
                if maxVal < sumVal:
                    maxVal = sumVal
    return maxVal


def findCrossMaxSunArray(prices, low, mid, high):
    leftIdx = 0
    rightIdx = 0
    leftSum = 0
    rightSum = 0
    leftMax = 0
    rightMax = 0

    for i in range(mid,low-1,-1):
        leftSum += prices[i]
        if leftSum > leftMax:
            leftMax = leftSum
            leftIdx = i
    for j in range(mid+1,high+1):
        rightSum += prices[j]
        if rightSum > rightMax:
            rightMax = rightSum
            rightIdx = j

    return (leftIdx, rightIdx, leftMax + rightMax)


def findMaxSubArray(prices, low, high):
    if low == high:
        return (low, high, prices[low])
    mid = (high + low  ) / 2
    (leftLow, leftHigh, leftMax) = findMaxSubArray(prices, low, mid)
    (rightLow, rightHigh, rightMax) = findMaxSubArray(prices, mid+1, high)
    (crossLow, crossHigh, crossMax) = findCrossMaxSunArray(prices, low, mid, high)
    if leftMax >= rightMax and leftMax >= crossMax:
        return (leftLow, leftHigh, leftMax)
    elif rightMax >= leftMax and rightMax >= crossMax:
        return (rightLow, rightHigh, rightMax)
    else:
        return (crossLow, crossHigh, crossMax)





prices = [100,113,110,85,105,102,86,63,81, 101,94,106,101,79,94,90,97]


print violence(prices)

print maxSubArray(prices)

diffs = diff(prices)
print diffs
print findMaxSubArray(diffs, 0, len(diffs)-1)