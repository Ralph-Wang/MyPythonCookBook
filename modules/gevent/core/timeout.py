#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent import Timeout

seconds = 1

timeout = Timeout(seconds)
timeout.start()


def wait():
    gevent.sleep(seconds+1)

try:
    gevent.spawn(wait).join()
except Timeout:
    print "Couldn't complete"


# use as a context manager

time_to_wait = 1

class TooLong(Exception):
    pass


try:
    with Timeout(time_to_wait, TooLong):
        gevent.sleep(time_to_wait+1)
except:
    import traceback
    traceback.print_exc()


# use timeout argument

timer1 = Timeout(seconds).start()
thread1 = gevent.spawn(wait)

try:
    thread1.join(timeout=timer1)
except Timeout:
    print "Thread 1 time out"

timer2 = Timeout.start_new(seconds)
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer2)
except Timeout:
    print "Thread 2 time out"

try:
    gevent.with_timeout(seconds, wait)
except Timeout:
    print "Thread 3 time out"
