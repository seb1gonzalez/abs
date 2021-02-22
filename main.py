#!/usr/bin/env python3

import logging
import sys
import os
import subprocess
from runner import Runner


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Main(): Instantiated")

    logging.debug("Main(): Calling runner.py constructor")
    Runner()


    logging.debug("Main(): Calling ECELD-Netsys from main.py")
    Runner.run_eceldnetsys()

    sys.exit(0)