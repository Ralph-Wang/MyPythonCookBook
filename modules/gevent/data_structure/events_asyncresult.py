#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent.event import AsyncResult

a = AsyncResult()


def setter():
    """ After 3 seconds set the result of a.
    :returns: TODO

    """
    gevent.sleep(3)
    a.set("Hello!")


def waiter():
    """ After 3 seconds the get call will unblock after setter
    puts a value into the AsyncResult
    """
    print a.get()


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
