#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# a sqlite shell to show how to use sqlite


# connect to file database
# conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('sample.db')
# :memory: for a RAM database
conn = sqlite3.connect(':memory:')
conn.isolation_level = None


# get cursor
cur = conn.cursor()

buffer = ""

print "Enter your SQL to execute in sqlite3."
print "Enter `quit` line to quit."


while True:
    line = raw_input("sql>> ")
    if line.strip() == "quit":
        break
    buffer += line
    # check if buffer is one or more COMPLETE SQL.
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            # if SELECT, display the result
            if buffer.lstrip().upper().startswith("SELECT"):
                print cur.fetchall()
        except sqlite3.Error as e:
            print "Error occurred:", e.args[0]
        buffer = ""

cur.close()
conn.close()
