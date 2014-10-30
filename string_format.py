#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "I'm {name}".format(name='Ralph')
print "I'm {[name]}".format({'name': 'Ralph'})

kv = {1: 123, 333: 456}
#formatter = '{0:0=10}:{1:0=10}'.format # 左补0至10位
#formatter = '{0:#<10}:{1:#<10}'.format # 右补#至10位,即左对齐
#formatter = '{0:>10}:{1:>10}'.format # 左补空格至10位,即右对齐
formatter = '{0:^10}:{1:^10}'.format # 居中对齐


for item in kv.items():
    print formatter(*item)

print "I'm {0}".format('Ralph')
