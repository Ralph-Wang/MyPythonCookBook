#!/usr/bin/env python
# -*- coding: utf-8 -*-


def meta(cls_name, cls_parents, cls_attr):
    attrs = {}.fromkeys(['a', 'b'], property(lambda self: self))
    cls_attr.update(attrs)
    return type(cls_name, cls_parents, cls_attr)

class Foo(object):
    __metaclass__ = meta

    def __repr__(self):
        return  "I'm foo"


f = Foo()

print f.a
print f.b
print dir(f)
