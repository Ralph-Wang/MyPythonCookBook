#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect(":memory:")

# Create Table
conn.execute("create table person ("
             "firstname text, lastname text)")

# data prepare
persons = [
        ("Ralph", "Wang"),
        ("Doubi", "Wang"),
        ]

# Insert some data
conn.executemany("insert into person values(?, ?)",persons)

for row in conn.execute("select * from person"):
    print row

print "delete", conn.execute("delete from person").rowcount, "rows"
