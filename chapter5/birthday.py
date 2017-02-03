#encoding=utf-8
from __future__ import division

__author__ = 'zhuzhengwei'



# k个人 生日有n=365个

n = 365

p = 1/n

result = 0

for k in range(2,365):
    e = k(k-1)/2 * n
    if e >= 1.0:
        result = k

print result