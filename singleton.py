#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Parent(object):
    singletons = {}
    def __new__(cls, *args):
        key = (cls, str(args))
        if key not in Parent.singletons:
            Parent.singletons[key] = object.__new__(cls)
        return Parent.singletons[key]

    def hello(self):
        print self


class Child1(Parent):
    pass

class Child2(Parent):
    pass


child1 = Child1(10)
child2 = Child2(10)
child3 = Child2(10) # same object as child2
child4 = Child2(20) # another object of Child2


child1.hello()
child2.hello()
child3.hello()
child4.hello()
