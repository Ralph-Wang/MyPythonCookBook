#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import json

def fetch(pid):
    response = urllib2.urlopen("http://localhost:8080/time.php")
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result["datetime"]
    print "Process {0}: {1}".format(pid, datetime)
    return json_result["datetime"]

def sync():
    for i in xrange(1, 10):
        fetch(i)

def async():
    threads = [gevent.spawn(fetch, i) for i in xrange(1, 10)]
    gevent.joinall(threads)

print "Sync:"
sync()
print "Async:"
async()
