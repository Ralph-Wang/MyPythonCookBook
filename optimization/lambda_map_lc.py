#!/usr/bin/env python
# -*- coding: utf-8 -*-


import timeit

l = open("test_file").readlines()

def m(l):
    return map(lambda s: s.strip(), l)


def c(l):
    return [s.strip() for s in l]


print "map:", timeit.timeit("m(l)", "from __main__ import m, l")
print "lc:", timeit.timeit("c(l)", "from __main__ import c, l")
# output:
# map: 28.9558811188
# lc: 18.584084034
