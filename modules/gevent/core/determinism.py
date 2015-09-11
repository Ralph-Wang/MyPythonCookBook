#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def echo(i):
    time.sleep(0.001)
    return i

# Non Deterministic Process Pool

from multiprocessing.pool import Pool as mPool

mp = mPool(10)

run1 = [a for a in mp.imap_unordered(echo, xrange(10))]
run2 = [a for a in mp.imap_unordered(echo, xrange(10))]
run3 = [a for a in mp.imap_unordered(echo, xrange(10))]
run4 = [a for a in mp.imap_unordered(echo, xrange(10))]

print run1 == run2 == run3 == run4

# Deterministic Gevent Pool

from gevent.pool import Pool as gPool

gp = gPool(10)

run1 = [a for a in gp.imap_unordered(echo, xrange(10))]
run2 = [a for a in gp.imap_unordered(echo, xrange(10))]
run3 = [a for a in gp.imap_unordered(echo, xrange(10))]
run4 = [a for a in gp.imap_unordered(echo, xrange(10))]

print run1 == run2 == run3 == run4
