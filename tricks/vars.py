#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Fib(object):
    def __init__(self):
        self._t = {0: 0, 1: 1}

    def calc(self, n):
        if n not in self._t:
            self._t[n] = self.calc(n-1) + self.calc(n-2)
        return self._t[n]

    def __call__(self, n):
        return self.calc(n)


fib = Fib()

print vars(fib) # => fib.__dict__
print vars() # => locals()
