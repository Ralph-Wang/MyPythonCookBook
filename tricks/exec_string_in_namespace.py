#!/usr/bin/env python
# -*- coding: utf-8 -*-


namespace = {
        "name": "loudou",
        "data": [3, 7, 9],
        }

code = """
def hello():
    return "name: {0}, age: {1}".format(name, data[0])
"""


func = compile(code, "<string>", "exec")

exec func in namespace

result = namespace["hello"]()
print result
