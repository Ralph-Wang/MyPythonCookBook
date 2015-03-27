#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit

def kn_recur(capacity, value, size, n):
    if n == 0 or capacity == 0:
        return 0
    if capacity < size[n-1]:
        return kn_recur(capacity, value, size, n-1)
    else:
        return max(value[n-1] + kn_recur(capacity-size[n-1], value, size, n-1),
                kn_recur(capacity, value, size, n - 1))

def kn_dp(capacity, value, size, n):
    l = [[0] * (capacity + 1) for dummy in xrange(n+1)]
    for i in xrange(n+1):
        for j in xrange(capacity+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            else:
                if j >= size[i-1]:
                    l[i][j] = max(value[i-1] + l[i-1][j-size[i-1]], l[i-1][j])
                else:
                    l[i][j] = l[i-1][j]
    return l[n][capacity]

def time_recur():
    kn_recur(capacity, value, size, n)

def time_dp():
    kn_dp(capacity, value, size, n)

value = [4, 5, 10, 11, 13];
size = [3, 4, 7, 8, 9];
capacity = 16;
n = len(size);

print kn_recur(capacity, value, size, n)
print timeit.timeit('time_recur()', 'from __main__ import time_recur');
print kn_dp(capacity, value, size, n)
print timeit.timeit('time_dp()', 'from __main__ import time_dp');
