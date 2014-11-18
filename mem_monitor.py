#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from functools import partial

# 因为访问了 /proc 伪文件系统, 所以只在 Linux 系统上有效
_proc_status = '/proc/{0}/status'.format(os.getpid())
_scale = {'kB': 1024.0, 'mB': 1024.0 * 1024.0,
          'KB': 1024.0, 'MB': 1024.0 * 1024.0}

def _VmB(VmKey):
    '''给定VmKey字符串, 返回字节数'''
    try:
        with open(_proc_status) as fobj:
            v = fobj.read()
    except IOError:
        return 0.0
    # i = v.index(VmKey)
    i = v.find(VmKey)
    v = v[i:].split(None, 3)
    if len(v) < 3:
        return 0.0
    return float(v[1]) * _scale[v[2]]


def _VmB_since(key, since=0.0):
    return _VmB(key) - since

# 虚拟内存
memory = partial(_VmB_since, 'VmSize:')

# 常驻内存
resident = partial(_VmB_since, 'VmRSS:')

# 栈
stacksize = partial(_VmB_since, 'VmStk:')

def foo():
    sleep = time.sleep
    l = []
    mem = memory()
    rss = resident()
    stk = stacksize()
    for i in xrange(100):
        l.append(range(100000))
        mem = memory()
        rss = resident()
        stk = stacksize()
        # mem = memory(mem)
        # rss = resident(rss)
        # stk = stacksize(stk)
        print '内存:', mem
        print '常驻:', rss
        print '栈:', stk
        sleep(1)

if __name__ == '__main__':
    foo()
