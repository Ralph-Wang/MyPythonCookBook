#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.server import StreamServer

def handle(socket, address):
    socket.send("Hello From a telnet!\n")
    for i in xrange(5):
        socket.send(str(i) + "\n")
    socket.close()

server = StreamServer(("0.0.0.0", 5000), handle)

server.serve_forever()
