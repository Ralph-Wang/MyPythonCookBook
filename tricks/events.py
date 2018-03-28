#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

class Events(object):
    def __init__(self):
        self._listeners = {}

    def on(self, name, function):
        if name not in self._listeners:
            self._listeners[name] = []
        self._listeners[name].append(function)

    def fire(self, name, data=None):
        if name not in self._listeners:
            ## TODO log and return, OR raise an Exception
            print("event(%s) is not registered" % name)
            return
        listeners = self._listeners[name]
        for listener in listeners:
            t = threading.Thread(target=listener, args=(data,))
            t.start()

    def on_event(self, name):
        def _wrapper(function):
            self.on(name, function)
            return function
        return _wrapper



events = Events()

def consumer_generator(index):
    def consumer(data):
        print('consumer %s with data(%s)' % (index, data))
    return consumer

for i in range(10):
    events.on('test', consumer_generator(i))

@events.on_event('test')
def deco_version(data):
    print('deco version consumer with data(%s)' % (data))

events.fire('test', 'Here\'s the data')
events.fire('test2', 'Here\'s the data')
