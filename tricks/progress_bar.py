#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
一个简单的 progress bar. 其实就是下面那个包的核心逻辑
高级需求可以 pip install progressbar. 这个功能更强大
'''

import sys
import time


class PBar(object):
    def __init__(self, title=None, maxval=100, fd=sys.stdout):
        self.maxval = maxval
        self.curval = 0
        self.title = title
        self.fd = fd
        self.width = 79

    def start(self):
        if self.title is not None:
            self.fd.write(self.title.center(self.width, '=') + '\n')
        self.update(1)
        return self

    def percentage(self):
        return self.curval*100.0 / self.maxval

    def update(self, val):
        assert 0 <= val <= self.maxval
        self.curval = val
        self.flush()

    def flush(self):
        if self.curval == self.maxval:
            line = self.format_line() + '\n'
        else:
            line = self.format_line() + '\r'
        self.fd.write(line)
        self.fd.flush()

    def format_line(self):
        line = ''
        p = self.percentage()
        line += '{0:0=4.1f}% ['.format(p)
        mark_num = int(71 * p / 100)
        marks = '#' * mark_num
        undo_marks = '-' * (71 - mark_num)
        line = line + marks + undo_marks + ']'
        return line

    def finish(self):
        self.update(self.maxval)


if __name__ == '__main__':
    p = PBar(title="Hello PBar", maxval=10000).start()
    for i in xrange(10000):
        p.update(i)
        time.sleep(0.0001)
    p.finish()
