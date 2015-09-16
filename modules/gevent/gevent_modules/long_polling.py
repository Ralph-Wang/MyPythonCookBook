#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import gevent
from gevent.pywsgi import WSGIServer
from gevent.queue import Empty, Queue

data_source = Queue()


def producer():
    while True:
        data_source.put_nowait("Hello World!")
        gevent.sleep(1)


def ajax_endpoint(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "application/json")
    ]

    start_response(status, headers)

    while True: # this response will not stop
        try:
            datum = data_source.get(timeout=5)
            # response a "Hello World!" per seconds
            yield json.dumps(datum) + "\n"
        except Empty:
            pass

gevent.spawn(producer)

WSGIServer(("", 8000), ajax_endpoint).serve_forever()
