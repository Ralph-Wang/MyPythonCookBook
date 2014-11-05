#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = range(10)

# 不重复组, 不足一组的尾巴会被去掉
print zip(*[iter(lst)] * 2)
print zip(*[iter(lst)] * 3)
print zip(*[iter(lst)] * 4)


# 连续组
print zip(*[iter(lst[i:]) for i in xrange(2)])
print zip(*[iter(lst[i:]) for i in xrange(3)])
