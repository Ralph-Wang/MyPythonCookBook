#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = range(20)

print lst[::2]  # step 2
print lst[::3]  # step 3


print lst[::-1]  # reverse

# named
last_three = slice(-3, None, None)  # start, stop, step
head_three = slice(3)  # stop

print lst[last_three]
print lst[head_three]
