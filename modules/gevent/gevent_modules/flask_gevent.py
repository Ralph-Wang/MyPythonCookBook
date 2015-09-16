#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from gevent.wsgi import WSGIServer

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!"


if __name__ == "__main__":
    WSGIServer(("", 5000), app).serve_forever()
