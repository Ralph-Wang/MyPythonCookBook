#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Point(x={0}, y={1})".format(self.x, self.y)


# adapt
def adapt_point(point):
    return "%f;%f" % (point.x, point.y)
sqlite3.register_adapter(Point, adapt_point)

# convert
def convert_point(s):
    x, y = map(float, s.split(";"))
    return Point(x, y)
sqlite3.register_converter("point", convert_point)

## make defination possible
conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)

cur = conn.cursor()

cur.execute("create table test(p point)")

p = Point(4.0, -3.2)

cur.execute("insert into test values(?)", (p,))

cur.execute("select * from test")

print cur.fetchone()

## parse from column names
conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)

cur = conn.cursor()

cur.execute("create table test(p)")

p = Point(4.0, -3.2)

cur.execute("insert into test values(?)", (p,))

cur.execute("select p as 'p [point]' from test")

print cur.fetchone()
