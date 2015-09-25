#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import mylib

def main():
    """ nothing
    :returns: TODO

    """
    logging.basicConfig(filename="myapp.log", level=logging.DEBUG)
    logging.info("Started")
    mylib.do_something()
    logging.info("Fin")

if __name__ == "__main__":
    main()
