#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Proper(type):
    def __new__(cls, cls_name, cls_parents, cls_attrs):
        cls_attrs.update({'mixin': lambda x: x})
        return type(cls_name, cls_parents, cls_attrs)



class Foo(object):
    __metaclass__ = Proper


f = Foo()

print f.mixin()
print dir(f)
