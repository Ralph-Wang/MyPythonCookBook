#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

"""
也可以理解为模板类为某件事定义了一种协议, 要完成这件事必须遵守这个协议
"""

class Fishing(object):
    __metaclass__ = abc.ABCMeta

    def fishing(self):
        """ 预置钓鱼需要的步骤 """
        self.prepare_bait()
        self.go_to_bank()
        self.find_location()
        print "开始钓鱼"

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_bank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass

class SeaFishing(Fishing):
    """ 海钓 """

    def prepare_bait(self):
        print "买海钓用饵"

    def go_to_bank(self):
        print "到海边"

    def find_location(self):
        print "找到海浪小(雾)的地方"

class RiverFishing(Fishing):
    """ 河钓 """

    def prepare_bait(self):
        print "买河钓用饵"

    def go_to_bank(self):
        print "去河边"

    def find_location(self):
        print "去水略浑的地方"

if __name__ == "__main__":
    s = SeaFishing()
    s.fishing()

    print "=" * 50

    r = RiverFishing()
    r.fishing()
