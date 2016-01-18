#!/usr/bin/env python
# -*- coding: utf-8 -*-


from timeit import timeit
import dis

def use_del():
    x = {}.fromkeys("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOOPQRSTUVWXYZ")
    del x["a"]

def use_pop():
    x = {}.fromkeys("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOOPQRSTUVWXYZ")
    x.pop("a")




print "use_del:", timeit("use_del", "from __main__ import use_del")
dis.dis(use_del)
print "use_pop:", timeit("use_pop", "from __main__ import use_pop")
dis.dis(use_pop)


