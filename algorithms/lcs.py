#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
lcs 算法: 计算两个序列的最长公共子序列
子序列: 不需要在原序列中连接
矩阵算法:
1. 相同字符记录, 取(左上角 + 1)
2. 不相同字符, 取上/左更大的
"""


def lcs(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    array = []
    the_lcs = []
    # 初始化矩阵
    for dummy_i in xrange(n1+1): # 行 str1 长度+1, 这里不能用列表乘法
        array.append([0] * (n2+1)) # 列 str2 长度+1

    for i in xrange(n1+1):
        for j in xrange(n2+1):
            if i == 0 or j == 0: # 行0, 列0 都是哨兵
                continue
            if str1[i-1] == str2[j-1]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i-1][j], array[i][j-1])

    i = n1
    j = n2
    # 回溯
    while i > 0 and j > 0:
        if array[i-1][j-1] + 1 == array[i][j] and str1[i-1] == str2[j-1]:
            the_lcs.append(str1[i-1]) # 如果按 str2 取, 则 else 为 j -= 1
            i -= 1
            j -= 1
        else:
            if array[i-1][j] < array[i][j-1]:
                j -= 1
            else:
                i -= 1

    the_lcs.reverse()

    return ''.join(the_lcs), array[n1][n2]


def test():
    cases = [
            ('abcdefg', 'abcdefg', ('abcdefg', 7)),
            ("GCCCTAGCG", "GCGCAATG", ('GCCTG', 5)),
            ('abcdefg', 'afebcg', ('abcg', 4)),
            ]
    for s1 ,s2, expect in cases:
        result = lcs(s1, s2)
        assert result == expect, '%s, %s, %s' %(s1, s2, result)

test()
