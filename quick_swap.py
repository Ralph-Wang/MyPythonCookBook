#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 1
b = 2

print a, b  # 1, 2

a, b = b, a

print a, b  # 2, 1

a = 1
b = 2
c = 3

print a, b, c  # 1, 2, 3

a, b, c = b, c, a

print a, b, c  # 2, 3, 1
