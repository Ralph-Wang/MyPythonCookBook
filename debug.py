#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dis

debug = False

def foo():
    if __debug__:
        print 'built-in debug'

def woo():
    if debug:
        print 'user debug'


dis.dis(foo)
# 使用 python -O, 会 __debug__ 下面的代码块不会被编译

print '=' * 50

dis.dis(woo)
