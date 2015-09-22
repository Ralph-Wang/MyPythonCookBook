#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent.server import StreamServer
from gevent import socket
import gipc
import time

PORT = 1337
N_CLIENTS = 10000
MSG = "HELLO\n"

def serve(sock, addr):
    f = sock.makefile()
    f.write(f.readline())
    f.flush()
    f.close()

def server():
    StreamServer(("localhost", PORT), serve).serve_forever()


def clientprocess():
    t1 = time.time()
    clients = [gevent.spawn(client) for _ in xrange(N_CLIENTS)]
    gevent.joinall(clients)
    duration = time.time() - t1
    print "{} clients served within {:.2f} s".format(N_CLIENTS, duration)

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", PORT))
    f = sock.makefile()
    f.write(MSG)
    f.flush()
    assert f.readline() == MSG
    f.close()

if __name__ == "__main__":
    s = gevent.spawn(server)
    c = gipc.start_process(clientprocess)
    c.join()
    s.kill()
    s.join()
