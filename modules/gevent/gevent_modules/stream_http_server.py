#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gevent.wsgi import WSGIServer

def application(environ, start_response):
    status = "200 OK"

    header = [
            ("Content-Type", "text/html")
            ]

    start_response(status, header)
    yield "<p> Hello"
    yield "World! </p>"


WSGIServer(("", 8000), application).serve_forever()
