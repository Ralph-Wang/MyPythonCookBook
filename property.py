#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Getter(object):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


class Setter(object):

    def __init__(self, value):
        self._value = value % 5

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value % 5

t = Getter(123)
print t.value
# t.value = 123  # raise AtrributeError


s = Setter(123)
print s.value
s.value = 999
print s.value
