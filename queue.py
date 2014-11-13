#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue

# q = Queue.Queue(10) # queue
q = Queue.LifoQueue(10) # stack

for i in xrange(10):
# for i in xrange(11):
    # q.put(i) # 11 的话会 block
    q.put(i, block=False) # 11 的话会直接抛异常


print q.qsize()
while q.qsize():
    print 'full:', q.full()
    print 'empty:', q.empty()
    print 'get:', q.get()

print 'empty:', q.empty()
