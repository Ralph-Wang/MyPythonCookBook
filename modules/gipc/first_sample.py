#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import gipc

def writelet(w):
    """
    This function runs as a Greenlet in the parent process.
    Put a Python object into the write end of the transport channel
    """
    w.put(0)

def readchild(r):
    """
    This function runs in a child process
    Read and vlidate object from the read end of the transport channel
    """
    assert r.get() == 0


def main():
    with gipc.pipe() as (readend, writeend):
        # Start "writer" Greenlet. Provide it with the pipe with write end
        g = gevent.spawn(writelet, writeend)
        # Start "reader" child process. Provide it with the pipe read end
        p = gipc.start_process(target=readchild, args=(readend,))

        g.join()
        p.join()


if __name__ == "__main__":
    main()
