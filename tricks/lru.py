#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DoublyLinkedNode(object):
    def __init__(self):
        self.empty = True
        self.key = None
        self.value = None

        self.prev = None
        self.next = None

class CacheMetrics(object):
    def __init__(self):
        self._hits = 0
        self._missed = 0
        self._access = 0

    @property
    def access(self):
        return self._access

    @property
    def hits(self):
        return self._hits

    def hit(self):
        self._hits += 1
        self._access += 1

    @property
    def missed(self):
        return self._missed

    def miss(self):
        self._missed += 1
        self._access += 1

    def hit_rate(self):
        return 1.0 * self._hits / self._access

    def miss_rate(self):
        return 1.0 * self._missed / self._access

    def dict(self):
        return {
                "hits": self.hits,
                "missed": self.missed,
                "access": self.access,
                "hits_rate": self.hit_rate(),
                "missed_rate": self.miss_rate()
                }

class LRUCache(object):

    """Docstring for LRUCache. """

    def __init__(self, capacity=10):
        self._table = {}
        self._capacity = capacity
        self._size = 0
        self._metrics = CacheMetrics()
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
            self._metrics.miss()
            return default

        self._metrics.hit()
        node = self._table[key]
        self._header = self._move_to_header(node)
        return node.value

    def set(self, key, value):
        if key in self._table:
            self._metrics.hit()
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

    def status(self):
        return self._metrics.dict()

if __name__ == "__main__":
    lru = LRUCache()
    lru.set("1", "2")
    lru.set("2", "3")
    lru.set("3", "4")
    lru.set("4", "5")
    lru.get("6", 7)
    lru.get("5", 7)
    lru.get("4", 7)
    lru.get("3", 7)
    lru.get("3", 7)
    print(lru.status())
