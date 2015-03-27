#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands

def use_system(cmd):
    'system 方法只能得到shell的返回状态, 不能得到输出'
    return os.system(cmd)

def use_popen(cmd):
    'popen 只能得到标准输出的内容, 标准错误的得不到'
    return os.popen(cmd).read()

def use_commands(cmd):
    'getstatusoutput 可以同时得到返回状态, 和输出(标准输出和标准错误)'
    return commands.getstatusoutput(cmd)
    # commands 里也有 getoutput 和 getstatus 两个方法
