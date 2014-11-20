#!/usr/bin/env python
# -*- coding: utf-8 -*-


import copy

# shallow copy 浅拷贝
a = {'a': {'b': 1}, 'c': 2}
print a

b = a.copy()
print b

b['a']['b'] += 1

print a  # {'a': {'b': 2}, 'c': 2}
print b  # {'a': {'b': 2}, 'c': 2}

print '-' * 20
# 深拷贝
a = {'a': {'b': 1}, 'c': 2}
print a

b = copy.deepcopy(a)

print b

b['a']['b'] += 1

print a  # {'a': {'b': 1}, 'c': 2}
print b  # {'a': {'b': 2}, 'c': 2}
