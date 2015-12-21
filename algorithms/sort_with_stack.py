#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(object):

    """ a normal stack with pop, push, is_empty, peek"""

    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return self._stack == []

    def peek(self):
        return self._stack[-1]


def move_min_to_top(stack):
    if stack.is_empty():
        return
    peek = stack.pop()
    if not stack.is_empty():
        move_min_to_top(stack)
        peek2 = stack.peek()
        if peek > peek2:
            stack.pop()
            stack.push(peek)
            stack.push(peek2)
            return
    stack.push(peek)




def sort_with_stack(stack):
    if stack.is_empty():
        return
    move_min_to_top(stack)
    peek = stack.pop()
    sort_with_stack(stack)
    stack.push(peek)


s = Stack()
s.push(3)
s.push(5)
s.push(4)
s.push(2)
s.push(7)
s.push(1)
s.push(6)

sort_with_stack(s)

while not s.is_empty():
    print s.pop()
