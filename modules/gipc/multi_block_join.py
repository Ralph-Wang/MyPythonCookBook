#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gevent
import multiprocessing


def writelet(c):
    """
    send once
    """
    while True:
        c.send(0) # non-coperatively

def readchild(c):
    """
    read twice
    """
    while True: # will block write cause of p.join()
        gevent.sleep(0)
        print 1
        assert c.recv() == 0 # non-coperatively

def main():
    c1, c2 = multiprocessing.Pipe()
    g = gevent.spawn(writelet, c1) # will be forked, hence send twice message
    p = multiprocessing.Process(target=readchild, args=(c2,))
    p.start()
    p.join() # it's blocking function, non-coperatively
    g.join()

if __name__ == "__main__":
    main()
