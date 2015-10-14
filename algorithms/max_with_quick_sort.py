#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import shuffle

def top(lst, n=0):
    """ find the top n number in lst

    :type lst: list
    :type n: int
    :returns: int

    """
    if lst == []:
        return None
    needed_idx = len(lst) - 1 - n
    left = []
    right = []
    pivot = lst.pop()
    while lst:
        x = lst.pop()
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    pivot_idx = len(left)
    if pivot_idx == needed_idx:
        return pivot
    elif pivot_idx > needed_idx:
        # 如果在左边, 那么第 N 的位置要减掉右边和 pivot 的总数
        return top(left, n - len(right) - 1)
    else:
        # 如果在右边, 其第 N 顺序不变
        return top(right, n)

def test(length, n):
    """ test top

    :type length: TODO
    :type n: TODO
    :returns: TODO

    """
    l = range(length)
    shuffle(l)
    return top(l, n)

def main():
    """ program entry """
    length = 10
    for i in xrange(0, length):
        x = test(length, i)
        print x
        assert x == length - i - 1


if __name__ == "__main__":
    main()
