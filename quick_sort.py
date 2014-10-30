#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def quicksort(lst):
    if len(lst) <= 1:
        return lst

    less = []
    greater = []
    pivot = lst.pop()
    for other in lst:
        if other < pivot:
            less.append(other)
        else:
            greater.append(other)

    return quicksort(less) + [pivot] + quicksort(greater)


case = range(20)
random.shuffle(case)

print case
print quicksort(case)
