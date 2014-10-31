#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TaskList(object):
    def __init__(self, lst=[]): # defaut value always be same object(same id)
        self._lst = lst

    def append(self, item):
        """docstring for append"""
        self._lst.append(item)


    def print_tasks(self):
        """docstring for print_tasks"""
        for item in self._lst:
            print item


ta = TaskList()
tb = TaskList()


ta.append('91 sugguest')
tb.append('CookBook')

ta.print_tasks()  # 91 sugguest & CookBook
print '-' * 20
tb.print_tasks()  # 91 sugguest & CookBook
