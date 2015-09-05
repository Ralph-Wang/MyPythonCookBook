#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta

class MyABC(object):

    __metaclass__ = ABCMeta


MyABC.register(tuple)


assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
