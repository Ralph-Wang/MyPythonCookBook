#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
in-place 的归并排序.
'''

def merge_sort(lst):
    n = len(lst)
    if n < 2:
        return
    step = 1
    while step < n:
        l = 0
        r = l + step
        while r + step < n:
            merge(lst, l, l+step, r, r+step)
            l = r + step
            r = l + step
        if r < n:
            merge(lst, l, l+step, r, n)
        step *= 2

def merge(lst, lstart, lstop, rstart, rstop):
    l = lst[lstart:lstop] + [float('inf')]
    r = lst[rstart:rstop] + [float('inf')]
    m = n = 0
    for i in xrange(lstart, rstop):
        if l[m] < r[n]:
            lst[i] = l[m]
            m += 1
        else:
            lst[i] = r[n]
            n += 1
    pass


import random

lst = range(10)
random.shuffle(lst)
print lst
merge_sort(lst)
print lst
