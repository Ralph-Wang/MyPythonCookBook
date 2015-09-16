#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent.pool import Pool

pool = Pool(2)


def hello_from(n):
    print "Size of pool {}".format(len(pool))
    print "Hello from Geenlet of {}".format(gevent.getcurrent())


pool.map(hello_from, xrange(3))
