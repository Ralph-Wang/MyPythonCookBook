#!/usr/bin/env python
#coding=utf-8

import codecs

with codecs.open('test.txt', 'w', encoding='utf-8') as fobj:
    fobj.write('Hello World')


# fobj 已经被关闭了
