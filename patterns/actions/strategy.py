#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


# 权限系统

# 普通的解决
class NormalDeleteUser(object):
    " 删除用户操作, 只能管理员操作"

    def __init__(self, admin=True):
        self._admin = admin

    def do(self):
        if self._admin:
            return "do delete"
        else:
            return "failed. not admin"


# 使用策略模式解决
class ABSDelete(object):
    " 抽象操作 "
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do(self):
        pass

# 优势在这里. 后续增加操作类型会更容易
class AdminDelete(object):
    def do(self):
        return "do delete"

class NormalUserDelete(object):
    def do(self):
        return "failed. not amdin"

# 在这里利用 python 的 "鸭子"类型,
# 任何有 do 方法的实例都可以传过来使用
# 如果要严格做类型检查, 检查是否是 ABSDelete 的实例即可
class StrategyDeleteUser(object):
    def __init__(self, delete):
        self._delete = delete

    def do(self):
        return self._delete.do()
