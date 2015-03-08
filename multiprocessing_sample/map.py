#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Pool, cpu_count
from time import sleep
from random import random

def foo(n):
    s = random()
    sleep(s)
    return n, s

p = Pool(processes=cpu_count() * 2)

# 在 map 时会阻塞, 要全部调用完成后才进行 print
# 但 foo 必须接收一个参数
for i in p.map(foo, xrange(100)):
    print i


# 返回 MapResult, ApplyResult 的子类, get 过返回的是所有调用的结果集
# 但 foo 必须接收一个参数
m = p.map_async(foo, xrange(100))
