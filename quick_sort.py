#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
用来证明 python 列表推导的强大
'''

import random


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    return quicksort([lt for lt in lst[1:] if lt < lst[0]]) + [lst[0]]\
        + quicksort([gt for gt in lst[1:] if gt >= lst[0]])


case = range(20)
random.shuffle(case)

print case
print quicksort(case)
