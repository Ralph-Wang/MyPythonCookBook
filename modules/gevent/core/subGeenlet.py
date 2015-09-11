#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent import Greenlet

class SubGeenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self): # subGreenlet need override _run method
        print self.message
        gevent.sleep(self.n)



g = SubGeenlet("Hi, there!", 3)
g.start()
g.join()
