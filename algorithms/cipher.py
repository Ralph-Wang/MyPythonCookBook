#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Caesar(object):

    """Caesar cipher"""

    def __init__(self, key):
        """init the Caesar

        :key: <int> caesar key

        """
        self._key = key

    @property
    def key(self):
        return self._key

    def encrypt(self, origin):
        """encrypt the origin string

        :origin: origin string
        :returns: encrypted string
        """
        l = []
        for c in origin:
            l.append(unichr((ord(c) + self.key) % 0x10000))
        return ''.join(l)

    def decrypt(self, encrypted):
        """decrypt the encrypted string

        :encrypted: encrypted string
        :returns: origin string
        """
        l = []
        for c in encrypted:
            l.append(unichr((ord(c) - self.key + 0x10000) % 0x10000))
        return ''.join(l)


if __name__ == '__main__':
    origin = u'abcdefg'
    c = Caesar(123984702934)
    encrypted = c.encrypt(origin)
    print encrypted
    print c.decrypt(encrypted)
