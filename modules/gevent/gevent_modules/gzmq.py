#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent_zeromq import zmq
# Note: require `pip install gevent_zeromq`


#--- Global Context ----------------------------------------------
context = zmq.Context()


def server():
    server_socket = context.socket(zmq.REP)
    server_socket.bind("tcp://127.0.0.1:5000")

    for request in xrange(1, 10):
        server_socket.send("Hello")
        print "Switch to Server for {}".format(request)
        server_socket.recv()


def client():
    client_socket = context.socket(zmq.REP)
    client_socket.connect("tcp://127.0.0.1:5000")

    for request in xrange(1, 10):
        client_socket.recv()
        print "Switch to Client for {}".format(request)
        client_socket.send("World")


publisher = gevent.spawn(server)
client = gevent.spawn(client)

gevent.joinall([publisher, client])
