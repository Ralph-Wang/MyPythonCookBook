#!/usr/bin/env python
# coding=utf-8


def trap1():
    while True:
        try:
            raise IndexError("Index Error")
        except ValueError:
            print 'Value Error'
        finally:
            print 'do finally'
            break                       # 会丢弃 Indexerror
            # return                      # 同样会丢弃


trap1()


def trap2():
    try:
        return 2
        raise ValueError("ValueError")
        # raise IndexError("IndexError") # 同样会被丢弃
    except ValueError:
        print "Any Error"
    finally:
        print 'do finally'
        return 1


print trap2()                   # 1
