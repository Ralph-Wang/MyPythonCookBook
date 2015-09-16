#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

# value=2 this sem can be acquired twice
sem = BoundedSemaphore(value=2)

def worker1(n):
    sem.acquire()
    print "Worker {} acquireed semaphore".format(n)
    sleep(0)
    sem.release()
    print "Worker {} released semaphore".format(n)


def worker2(n):
    with sem:
        print "Worker {} acquired semaphore".format(n)
        sleep(0)
    print "Worker {} release semaphore".format(n)


p = Pool()

p.map(worker1, xrange(2))
print "2"
p.map(worker2, xrange(3, 6))
