#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lcs(w1, w2):
    max_length, end_idx = 0, 0
    l = [[0] * (len(w2)+1) for i in xrange(len(w1) + 1)]

    for i in xrange(len(w1)+1):
        for j in xrange(len(w2)+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            else:
                if w1[i-1] == w2[j-1]:
                    l[i][j] = l[i-1][j-1] + 1
                    print l[i][j], i, j
                else:
                    l[i][j] = 0
            if l[i][j] > max_length:
                max_length = l[i][j]
                end_idx = i

    return w1[end_idx-max_length:max_length+1]




w1 = 'abcdefg'
w2 = 'aabbcdef'
print lcs(w1, w2)
