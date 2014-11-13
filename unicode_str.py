#!/usr/bin/env python
# -*- coding: utf-8 -*-



try:
    x = '中文' + u'字符' # 用 ascii 字符没问题
except ValueError:
    print 'err'


import sys
reload(sys)
sys.setdefaultencoding('utf8')


x = '中文' + u'字符'

print x
