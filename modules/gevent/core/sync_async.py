#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0, 2)*0.001)
    print "Task {0} done".format(pid)

def sync():
    for i in xrange(1, 10):
        task(i)

def async():
    threads = [gevent.spawn(task, i) for i in xrange(1, 10)]
    gevent.joinall(threads)


print "Sync:"
sync()
print "Async:"
async()
