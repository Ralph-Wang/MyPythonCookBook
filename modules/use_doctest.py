#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    """
    >>> fib(0)
    0
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(10) # Failed
    10
    """
    pre = 1
    cur = 0
    for i in xrange(n):
        cur, pre = cur + pre, cur
    return cur



if __name__ == '__main__':
    # same as use python -m doctest <file_name>
    import doctest
    doctest.testmod()
