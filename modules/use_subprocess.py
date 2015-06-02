#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit Code:', r)



## communicate()

print '$ nslookup'
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate('set q=mx\npython.org\n')
print 'output:'
print output
print 'err:'
print err
print('Exit Code:', p.returncode)
