#!/usr/bin/python

import logging
from runner import Runner

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Main(): Instantiated")
    Runner() 