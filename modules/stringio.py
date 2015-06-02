#!/usr/bin/env python
# -*- coding: utf-8 -*-


from io import StringIO
from io import BytesIO


with StringIO() as f:
    print f.write(u'unicode') # unicode is needed
    print f.read() # cause of cursor, read returns u''
    print f.getvalue() # ignore cursor, return all in the buffer
    f.seek(0)
    print f.read()

with BytesIO() as f:
    print f.write(u'中文'.encode('utf-8')) # python2 has no real bytes
    print f.read()
    print type(f.getvalue())
    f.seek(0)
    print f.read()
