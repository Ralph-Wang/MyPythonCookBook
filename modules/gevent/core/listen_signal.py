#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import signal

def run_forever():
    gevent.sleep(1000)


gevent.signal(signal.SIGQUIT, gevent.kill)
thread = gevent.spawn(run_forever)
thread.join()
