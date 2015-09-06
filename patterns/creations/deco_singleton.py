#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):

    """ 单例装饰器, 可使其它类成为单例. 线程不安全 """

    def __init__(self, cls):
        """ 每个装饰器实例都保存其装饰的类和单例 """
        self._cls = cls
        self._instance = None

    def Instance(self):
        if self._instance is None:
            self._instance = self._cls()
        return self._instance

    def __call__(self):
        return self.Instance()

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class Foo(object):

    def __init__(self):
        pass

    def display(self):
        return id(self)

if __name__ == "__main__":
    s1 = Foo()
    s2 = Foo()
    print s1, s1.display()
    print s2, s2.display()
    print s1 is s2
