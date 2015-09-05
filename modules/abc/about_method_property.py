#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty


class MyABC(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def say(self, msg):
        print msg

    @abstractproperty
    def x(self):
        return self._x

    @x.setter
    def x_setter(self, value):
        self._x = value

    def y_getter(self):
        return self._y

    def y_setter(self, value):
        self._y = value

    y = abstractproperty(y_getter, y_setter)


class Foo(MyABC):
    pass

f = Foo() # 未实现抽象方法和属性, 不能实例化
