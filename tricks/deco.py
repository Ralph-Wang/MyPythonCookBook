#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def deco_with_name(name):
    def _profiler(func):
        def _wrap(*args):
            start = time.time()
            res = func(*args)
            print name, 'cose:', time.time() - start
            return res
        return _wrap
    return _profiler

@deco_with_name('add')
def add_safe(x, y):
    return x + y


add_safe(1, 2)
