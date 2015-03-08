#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import cpu_count, Pool
from time import sleep
from random import random

def foo(n):
    s = random()
    sleep(s)
    return n, s

p = Pool(processes=cpu_count() * 2)


# 基本就是 apply_async 然后 ApplyResult 的阻塞写法
# 但 foo 必须接收一个参数
for i in p.imap(foo, xrange(100)):
    print i

# 基本就是 apply_async 然后 ApplyResult 的非阻塞写法
# 但 foo 必须接收一个参数
for i in p.imap_unordered(foo, xrange(100)):
    print i
