#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time, sys, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# register
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


# connect server
server_addr = '127.0.0.1'
print 'connect to server %s...' % server_addr

m = QueueManager(address=(server_addr, 5000), authkey=b'secret')

m.connect() # start for server, connect for client

task = m.get_task_queue()
result = m.get_result_queue()

for i in xrange(10):
    try:
        n = task.get(timeout=1)
        print 'run task %d * %d...' % (n, n)
        r = '%d * %d = %d' % (n, n, n * n)
        result.put(r)
    except queue.Queue.Empty:
        print 'task queue is empty.'


print 'worker exit.'
