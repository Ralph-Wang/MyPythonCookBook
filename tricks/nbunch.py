#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NBunch(dict):

    def __init__(self, default=None, *args, **kwargs):
        """扩展 dict 使其支持点号(.)访问"""
        super(NBunch, self).__init__(*args, **kwargs)
        self.__dict__ = self
        self.__default = default

        # 处理嵌套
        for key in self:
            if isinstance(self[key], dict):
                self[key] = NBunch(self[key])

    def __getattr__(self, key):
        """"""
        return self.get(key, self.__default)


nb = NBunch({'a': 1, 'b': {'c': 2}})

print nb.a
print nb.b.c
