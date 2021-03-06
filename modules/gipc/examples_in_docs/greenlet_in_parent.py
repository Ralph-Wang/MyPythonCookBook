#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import gipc

def main():
    with gipc.pipe() as (r, w):
        p = gipc.start_process(target=child_process, args=(r,))
        wg = gevent.spawn(writegreenlet, w)
        try:
            p.join()
        except KeyboardInterrupt:
            wg.kill(block=True)
            p.terminate()
        p.join() # here `p.join()` is waiting for `p.terminate()` done.

def writegreenlet(writer):
    while True:
        writer.put("written to pipe from a greenlet running in the main process")
        gevent.sleep(1)

def child_process(reader):
    while True:
        print "Child process got message from pipe:\n {}".format(reader.get())

if __name__ == "__main__":
    main()
