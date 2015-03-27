#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import timeit


# 使用局部变量

def g(lst):
    for i in xrange(len(lst)):
        lst[i] = math.sin(lst[i])
    return lst

def l(lst):
    sin = math.sin
    for i in xrange(len(lst)):
        lst[i] = sin(lst[i])
    return lst

def m(lst):
    return map(math.sin, lst)

print 'glboal:', timeit.timeit('g(range(100))', 'from __main__ import g;import math')
print 'local:', timeit.timeit('l(range(100))', 'from __main__ import l;import math')
print 'map:', timeit.timeit('m(range(100))', 'from __main__ import m;import math')
# output:
# glboal: 19.1356389523
# local: 14.3132870197

# 类里面用局部变量, 也有优化哦

class A:
    def __init__(self):
        self.items = range(100)

    def use_self(self):
        for i in self.items:
            self.items[i] = self.items[i] * 2

    def use_local(self):
        self_items = self.items
        for i in self_items:
        # for i in self.items: # 相同结果, 优化在计算部分
            self_items[i] = self_items[i] * 2

print 'use_self: ', timeit.timeit('a=A();a.use_self()', 'from __main__ import A')
print 'use_local: ', timeit.timeit('a=A();a.use_local()', 'from __main__ import A')
# output:
# use_self:  17.1078062057
# use_local:  10.9118049145

# 用公式代替循环

def loop_sum(n):
    sum = 0
    for i in xrange(n):
        sum += i
    return sum

def exp_sum(n): # 数学大法好
    return n * (n + 1) / 2

print 'loop:', timeit.timeit('loop_sum(100)', 'from __main__ import loop_sum')
print 'expression:', timeit.timeit('exp_sum(100)', 'from __main__ import exp_sum')
# output:
# loop: 4.4805328846
# expression: 0.186967849731
