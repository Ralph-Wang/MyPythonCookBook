#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

print socket.socket



from gevent import monkey
monkey.patch_socket()
print "After monkey patch"
print socket.socket


import select
print select.select

monkey.patch_select()
print select.select
