#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(format="%(levelname)s:%(message)s",
        datefmt="%m/%d/%Y %H:%M:%S")

logging.debug("This message should appear on the console.")
logging.info("So should this.")
logging.warning("And this, too.")
