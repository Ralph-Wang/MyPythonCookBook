#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DoublyLinkedNode(object):
    def __init__(self):
        self.empty = True
        self.key = None
        self.value = None

        self.prev = None
        self.next = None

class LRUCache(object):

    """Docstring for LRUCache. """

    def __init__(self, capacity=10):
        self._table = {}
        self._capacity = capacity
        self._size = 0
        self._init_header()

    def size(self):
        return self._size

    def _init_header(self):
        self._header = DoublyLinkedNode()
        self._header.next = self._header
        self._header.prev = self._header
        for i in range(self._capacity):
            node = DoublyLinkedNode()
            node.next = self._header
            node.prev = self._header.prev

            self._header.prev.next = node
            self._header.prev = node


    def iter(self):
        cur = self._header
        for i in range(self.size()):
            yield cur
            cur = cur.next

    def _move_to_header(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

        node.next = self._header.prev.next
        node.prev = self._header.prev

        self._header.prev.next = node
        self._header.prev = node

        return node

    def get(self, key, default=None):
        if key not in self._table:
            return default

        node = self._table[key]
        self._header = self._move_to_header(node)
        return node.value

    def set(self, key, value):
        if key in self._table:
            node = self._table[key]
            self._header = self._move_to_header(node)
            return


        node = self._header.prev
        if not node.empty:
            self._table.pop(node.key)
        else:
            self._size += 1

        node.key = key
        node.value = value
        node.empty = False
        self._table[key] = node
        self._header = node

if __name__ == "__main__":
    lru = LRUCache()
    lru.set("1", "2")
    lru.set("3", "4")
    for i in lru.iter():
        print(i.key,i.value)
