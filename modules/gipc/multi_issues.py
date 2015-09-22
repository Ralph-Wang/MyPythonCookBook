#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gevent
import multiprocessing


def writelet(c):
    """
    send once
    """
    c.send(0) # non-coperatively

def readchild(c):
    """
    read twice
    """
    gevent.sleep(0)
    assert c.recv() == 0 # non-coperatively
    assert c.recv() == 0 # need to raise error, but not

def main():
    c1, c2 = multiprocessing.Pipe()
    g = gevent.spawn(writelet, c1) # will be forked, hence send twice message
    p = multiprocessing.Process(target=readchild, args=(c2,))
    p.start()
    g.join()
    p.join() # it's blocking function, non-coperatively

if __name__ == "__main__":
    main()
