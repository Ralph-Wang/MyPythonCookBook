#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent.queue import Queue
import abc

class Actor(gevent.Greenlet):

    __metaclass = abc.ABCMeta

    def __init__(self):
        self.inbox = Queue()
        super(Actor, self).__init__()

    @abc.abstractmethod
    def receive(self, message):
        raise NotImplementedError()

    def _run(self):
        self.running = True

        while self.running:
            # get message from inbox && take independent actions
            message = self.inbox.get()
            self.receive(message)

class Pinger(Actor):
    def receive(self, message):
        print message
        pong.inbox.put("ping")
        gevent.sleep(2)

class Ponger(Actor):
    def receive(self, message):
        print message
        ping.inbox.put("pong")
        gevent.sleep(2)

ping = Pinger()
pong = Ponger()


ping.start()
pong.start()

ping.inbox.put("start")
gevent.joinall([ping, pong])
