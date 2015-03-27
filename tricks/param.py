#!/usr/bin/env python
# -*- coding: utf-8 -*-


def foo(param):  # pass the reference
    print id(param)


# immortal
a = 1
print id(a)
foo(a)

# mortal
b = [1, 2, 3]
print id(b)
foo(b)
