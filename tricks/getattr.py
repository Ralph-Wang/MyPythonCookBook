#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Url(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        def chain(path):
            return Url('{0}/{1}'.format(self._path, path))

        if path == 'user': # rest 中参数化的 path
            return lambda s: chain(s)
        return chain(path)

    def __repr__(self):
        return self._path

    __str__ = __repr__



# /the/path/to/get
print Url().the.path.to.get


# /:user/repos: user -> ralph
print Url().user('ralph').repos
