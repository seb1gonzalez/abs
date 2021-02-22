#!/usr/bin/python3

import logging
import sys
from runner import Runner

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Main(): Instantiated")
    Runner()
    sys.exit(0)