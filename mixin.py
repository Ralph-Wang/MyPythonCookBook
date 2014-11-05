#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GameMixin(object):

    def play(self):
        print '{0} playing game'.format(self.name)


class CodeMixin(object):

    def play(self):
        print '{0} coding'.format(self.name)


class AnimeMixin(object):

    def play(self):
        print '{0} watching Naruto'.format(self.name)


class Man(object):

    def __init__(self, name):
        self.name = name
        self.__bases__ = ()

    @staticmethod
    def type(type_name):
        type_table = {
            'code': CodeMixin,
            'game': GameMixin,
            'anime': AnimeMixin
        }
        if type_name not in type_table:
            type_name = 'code'
        return type_table[type_name]

    @staticmethod
    def create(name, type_name):
        man = Man(name)
        man.__class__ = type('',
                             (man.type(type_name), Man),
                             {})
        return man


a = Man.create('anime fan', 'anime')
c = Man.create('coder', 'code')
g = Man.create('game fan', 'game')

a.play()
c.play()
g.play()
