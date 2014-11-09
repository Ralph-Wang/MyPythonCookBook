#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
基于生成器的协程
-,- 不太理解协程是啥, 暂时就这样吧
'''


def producter():
    for i in xrange(100000):
        yield i


def consumer(cid):
    while True:
        value = yield
        print '[{0}] {1}'.format(cid, value)


cs = []
for cid in xrange(5):
    c = consumer(cid)
    c.next()
    cs.append(c)

for i in producter():
    cs[i%5].send(i)
