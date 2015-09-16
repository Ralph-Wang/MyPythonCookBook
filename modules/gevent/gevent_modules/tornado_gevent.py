#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.wsgi
from gevent.wsgi import WSGIServer


class Index(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello World")


# app = tornado.web.Application([
app = tornado.wsgi.WSGIApplication([
    (r"/", Index)
])

if __name__ == "__main__":
    # app.listen(5000)
    # tornado.ioloop.IOLoop.instance().start()
    WSGIServer(("", 5000), app).serve_forever()
