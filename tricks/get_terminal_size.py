#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
import sys
import termios
from fcntl import ioctl


def get_terminal_size():
    return struct.unpack('hh', ioctl(sys.stdout, termios.TIOCGWINSZ, '1234'))


print get_terminal_size()
