#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute("create table person(name, age)")

who = "Ralph"
age = 4

# ? style
cur.execute("insert into person values (?, ?)", (who, age))

# named style
cur.execute("select * from person where name=:who and age=:age", (who, age))

print cur.fetchall()
