#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Foo(object):

    def __getitem__(self, index):
        return 0

    def __len__(self):
        return 0

    def get_iterator(self):
        return iter(self)


class Bar(object):
    def __iter__(self):
        return iter(self)

class MyIterable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)

assert issubclass(Foo, MyIterable) # 注册了, 没实现 __iter__.
assert issubclass(Bar, MyIterable) # 没注册, 但仍被视为子类
