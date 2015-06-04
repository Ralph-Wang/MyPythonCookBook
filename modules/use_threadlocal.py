#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

local = threading.local()

def request():
    url = local.url
    print '[{0}] request {1}'.format(threading.current_thread().name, url)


def prepare(querystring):
    url = 'http://test/' + threading.current_thread().name + '?' + querystring
    local.url = url
    request()


t1 = threading.Thread(target=prepare, args=('size=1',), name='user')
t2 = threading.Thread(target=prepare, args=('size=2',), name='pictures')
t1.start()
t2.start()
t1.join()
t2.join()
