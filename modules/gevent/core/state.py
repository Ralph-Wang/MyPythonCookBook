#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent

def win():
    return "You win!"

def fail():
    raise Exception("You fail!!!")


winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print "winner started?", winner.started
print "looser started?", loser.started

try:
    gevent.joinall([winner, loser])
except Exception:
    print "This will never be reached"

print "winner value:", winner.value
print "loser value:", loser.value

print "winner ready?", winner.ready()
print "loser ready?", loser.ready()

print "winner succ?", winner.successful()
print "loser succ?", loser.successful()

# fail 中抛出的异常不会导致主进程停止, 但会输出其堆栈信息
print loser.exception
