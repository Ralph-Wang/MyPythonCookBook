#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def switch(n):
    table = {
        1: 'one',
        2: 'two',
        3: 'three',
        'other': 'other'
    }
    if n not in table:
        n = 'other'
    return table[n]


print switch(random.randrange(7))
