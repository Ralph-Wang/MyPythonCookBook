#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random, time, queue
from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
result_queue = queue.Queue()



class QueueManager(BaseManager):
    pass


# register queues
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# bind port, set authkey
manager = QueueManager(address=('0.0.0.0', 5000), authkey=b'secret')

manager.start()


# get queue from manager
task = manager.get_task_queue()
result = manager.get_result_queue()


# put tasks
for i in xrange(10):
    n = random.randrange(0, 10000)
    print 'Put task %d...' % n
    task.put(n)


print 'Trying to get results...'

for i in xrange(10):
    r = result.get(timeout=10)
    print 'Result: %s' % r

manager.shutdown()
print('manager exit.')
