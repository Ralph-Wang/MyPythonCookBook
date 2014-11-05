#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = range(10)
chs = [chr(i) for i in xrange(65, 76)]

print lst
print chs

zipped = zip(lst, chs)  # zip
print zipped

print zip(*zipped)  # unzip
