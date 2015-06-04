#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess

print('cd / && ls')
r = subprocess.call(['cd', '/'])
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
