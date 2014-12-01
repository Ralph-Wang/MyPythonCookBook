#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

try:
    raise IOError
except IOError:
    pass

try:
    raise ValueError
except ValueError:
    pass

traceback.print_exc()  # 只打印出最近一次的 Exception
