#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit

import imported_as

print id(timeit)
print id(imported_as._timeit)
# print id(importtest0.timeit)    # Attribute Error

print sys.modules['timeit']
# print sys.modules['_timeit']    # Key Error
