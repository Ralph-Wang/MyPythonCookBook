#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

import gevent
from gevent import select

start = time.time()


tic = lambda: "at {0:1.1f} seconds".format(time.time() - start)


def g1():
    print "Start Polling: {0}".format(tic())
    select.select([], [], [], 2)
    print "Ended Polling: {0}".format(tic())


def g2():
    print "Start Polling: {0}".format(tic())
    select.select([], [], [], 2)
    print "Ended Polling: {0}".format(tic())


def g3():
    print "Hey lets do some stuff while the greenlets poll, {0}".format(tic())
    gevent.sleep(1)

gevent.joinall(
    [
        gevent.spawn(g1),
        gevent.spawn(g2),
        gevent.spawn(g3),

    ]
)
