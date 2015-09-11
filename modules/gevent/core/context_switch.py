#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" First Sample for Context Switch """

import gevent


def foo():
    print "Running in foo"
    gevent.sleep(0)
    print "Explicit context switch to foo again"


def bar():
    print "Explicit context to bar"
    gevent.sleep(0)
    print "Implicit context switch back to bar"

gevent.joinall(
    [
        gevent.spawn(foo),
        gevent.spawn(bar),
    ]
)
## output
# Running in foo
# Explicit context to bar
# Explicit context switch to foo again
# Implicit context switch back to bar
