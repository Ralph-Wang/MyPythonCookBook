#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent.event import Event

evt = Event()


def setter():
    """ After 3 seconds wake all threads waiting on the value """
    print "A: Hey wait for me, I have to do something."
    gevent.sleep(3)
    print "A: Ok, I'm done"
    evt.set()


def waiter():
    """ After 3 seconds the get call will unblock
    """
    print "I'll wait for you"
    evt.wait()
    print "It's about time"


def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),

    ])

if __name__ == "__main__":
    main()
