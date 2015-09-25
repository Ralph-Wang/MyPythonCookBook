#!/usr/bin/env python
# -*- coding: utf-8 -*-


import timeit
import math

l = open("test_file").readlines()

def m(l):
    return map(lambda s: s.strip(), l)


def c(l):
    return [s.strip() for s in l]


def m2(l):
    return map(math.sin, l)

def c2(l):
    return [math.sin(x) for x in l]

print "map with lambda strip()", timeit.timeit("m(l)", "from __main__ import m, l")
print "lc without lambda strip():", timeit.timeit("c(l)", "from __main__ import c, l")
print "map2 without lambda:", timeit.timeit("m2(range(1000))", "from __main__ import m2;import math")
print "lc2 without lambda:", timeit.timeit("c2(range(1000))", "from __main__ import c2;import math")
# output:
# map with lambda strip() 29.0766270161
# lc without lambda strip(): 19.6075670719
# map2 without lambda: 116.784960032
# lc2 without lambda: 171.118189812
