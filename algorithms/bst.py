#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value):
        self._value = value
        self._count = 1
        self.left = None
        self.right = None

    def set_value(self, value):
        self._value = value

    def set_count(self, n):
        self._count = n

    def get_value(self):
        return self._value

    def get_count(self):
        return self._count

    def __repr__(self):
        return str(self.get_value()) + ':' + str(self.get_count())

    def increment(self, n):
        self._count += n


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            cur = self.root
            inserted = False
            while not inserted:
                parent = cur
                if value < cur.get_value():
                    cur = cur.left
                    if cur is None:
                        parent.left = Node(value)
                        inserted = True
                elif value > cur.get_value():
                    cur = cur.right
                    if cur is None:
                        parent.right = Node(value)
                        inserted = True
                else: # value == cur.get_value()
                    cur.increment(1)
                    inserted = True

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, node):
        if node is None:
            return ''
        return self._inOrder(node.left) + '\n' + \
                str(node) + '\n' + \
                self._inOrder(node.right)

    def getMax(self, node=None):
        cur = node or self.root
        while cur.right is not None:
            cur = cur.right
        return cur

    def getMin(self, node=None):
        cur = node or self.root
        while cur.left is not None:
            cur = cur.left
        return cur

    def remove(self, value):
        self.root = self._remove_helper(self.root, value)

    def _remove_helper(self, node, value):
        if node is None:
            return None
        if value < node.get_value():
            node.left = self._remove_helper(node.left, value)
            return node
        elif value > node.get_value():
            node.right = self._remove_helper(node.right, value)
            return node
        else: # value == node.get_value()
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            tmpNode = self.getMin(node.right)
            node.set_value(tmpNode.get_value())
            node.set_count(tmpNode.get_count())
            node.right = self._remove_helper(node.right, tmpNode.get_value())
            return node

if __name__ == '__main__':
    bst = BST()
    bst.insert(23)
    bst.insert(45)
    bst.insert(16)
    bst.insert(16)
    bst.insert(37)
    bst.insert(3)
    bst.insert(3)
    bst.insert(99)
    bst.insert(22)
    print bst.inOrder()
    print '-' * 10
    print bst.getMin()
    print bst.getMax()
    print '-' * 10
    bst.remove(22)
    print bst.inOrder()
    print '-' * 10
