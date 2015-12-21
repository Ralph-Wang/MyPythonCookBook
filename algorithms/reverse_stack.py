#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack(object):

    """normal stack"""

    def __init__(self):
        self._stack = []

    def pop(self):
        return self._stack.pop()

    def push(self, val):
        self._stack.append(val)

    def is_empty(self):
        return self._stack == []

    def peek(self):
        if self.is_empty():
            return None
        return self.peek[-1]




def move_bottom_to_top(stack):
    if stack.is_empty():
        return
    peek = stack.pop()
    if not stack.is_empty():
        move_bottom_to_top(stack)
        bottom = stack.pop()
        stack.push(peek)
        stack.push(bottom)
    else:
        stack.push(peek)


def reverse_stack(stack):
    if stack.is_empty():
        return
    move_bottom_to_top(stack)
    bottom = stack.pop()
    reverse_stack(stack)
    stack.push(bottom)


s = Stack()

for item in xrange(10):
    s.push(item)

reverse_stack(s)

while not s.is_empty():
    print s.pop()
