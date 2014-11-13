#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import time


def foo(msg):
    for i in xrange(3):
        print msg
        time.sleep(1)
    return 'done ' + msg


if __name__ == '__main__':
    # p = multiprocessing.Process(target=foo, args=('Hello',))
    p = multiprocessing.Pool(processes=4)
    results = []
    for i in xrange(10):
        msg = "Hello " + str(i)
        results.append(p.apply_async(foo, (msg,)))
    p.close()
    p.join()
    for result in results:
        print result.get()
    print 'Sub-process done.'
