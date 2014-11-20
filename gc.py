#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gc


def dump_garbage():
    '''展示回收的垃圾'''
    # 告诉 gc 不要直接删除对象, 而是收集到 gc.garbage
    gc.set_debug(gc.DEBUG_LEAK)
    print '\nGARBAGE:'
    gc.collect()
    print '\nGARBAGE OBJ:'
    for obj in gc.garbage:
        s = str(obj)
        if len(s) > 80:
            s = s[:77] + '...'
        print type(obj)
        print s

if __name__ == '__main__':
    l = []
    l.append(l)
    del l
    dump_garbage()
