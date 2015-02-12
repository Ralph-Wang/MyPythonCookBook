#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
有100（N）个囚犯被判了死刑，他们被排成一圈，从第一个囚犯开始数数，数到7（M）的那个人将被拉出去枪毙。
   然后下一个人再从1开始数，直到剩下的最后一个人将被释放。请问最后幸存的囚犯编号是多少？
      当然，这道题不是让你口算出最后的囚犯是几号，而是请你给出一个 int
      getLastOne(n, m) 的函数
"""

def getLast(n, m, left):
    l = range(1, n+1)
    while len(l) > left:
        # 第 (m-1) % len(l) 个人就是数 m 的人
        # 索引是从 0 开始, 故 m - 1
        l.remove(l[(m-1)%len(l)])
    return l

print getLast(100, 7, 4)
