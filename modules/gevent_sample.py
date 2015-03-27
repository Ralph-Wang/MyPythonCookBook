#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import requests

def f(url):
    print 'request: {0}'.format(url)
    res = requests.get(url)
    print '{0} bytes received from {1}'.format(len(res.content), url)


g2 = gevent.spawn(f, 'http://pypi.python.org')
g3 = gevent.spawn(f, 'http://www.python.org')
g1 = gevent.spawn(f, 'http://www.bing.com')
g1.join()
g2.join()
g3.join()
