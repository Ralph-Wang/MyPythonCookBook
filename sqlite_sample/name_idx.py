#!/usr/bin/env python
# -*- coding: utf-8 -*-q

import sqlite3

conn = sqlite3.connect(':memory:')

# default, row_factory is tuple
conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("select 'John' as name, 42 as age")

for row in cur:
    print row
    print type(row)
    print row['name'] # sqlite3.Row
