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


# 用 __call__ 来解决同名参数问题
class Url2(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Url2('{0}/{1}'.format(self._path, path))

    def __call__(self, path):
        path_list = self._path.split('/')
        path_list[-1] = path
        self._path = '/'.join(path_list)
        return self

    def __repr__(self):
        return self._path

    __str__ = __repr__

# /:user/repos: user -> ralph
print Url2().user('ralph').repos

# /user/1
print Url2().user.repos
