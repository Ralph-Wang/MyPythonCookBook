#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
            return
        listeners = self._listeners[name]
        for listener in listeners:
            listener(data)


events = Events()

def consumer_generator(index):
    def consumer(data):
        print('consumer %s' % index)
        print('data %s' % data)
        print('-----------')
    return consumer

for i in range(10):
    events.on('test', consumer_generator(i))

events.fire('test', 'empty')
