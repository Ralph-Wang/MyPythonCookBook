#!/usr/bin/env python
# -*- coding: utf-8 -*-


# pipe 库需要额外安装
from pipe import *


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# 小于 1000 的斐波那契数的奇数和

answer = fib() |\
        take_while(lambda x : x < 1000) |\
        where(lambda x : x%2 == 1) |\
        add

print answer
