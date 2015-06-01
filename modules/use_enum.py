#!/usr/bin/env python
# -*- coding: utf-8 -*-

# `pip install enum34` if in a previous version of 3.4

from enum import Enum
from enum import unique

@unique
class Week(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6



for i in Week:
    print i, '=>', i.name, ',', i.value

for i in xrange(0, 7):
    print Week(i)
