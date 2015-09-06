#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Signleton(object):
    """ 单例的壳子, 壳子并不是单例的 """

    class _Singleton(object):
        """ 真正单例的类, 外部不可见"""

        def __init__(self):
            pass

        def display(self):
            return id(self)

    _instance = None

    def __init__(self):
        if Signleton._instance is None:
            Signleton._instance = Signleton._Singleton()

    def __getattr__(self, attr):
        return getattr(self._instance, attr)

if __name__ == "__main__":
    s1 = Signleton()
    s2 = Signleton()
    print id(s1)
    print id(s2)
    print s1.display()
    print s2.display()
