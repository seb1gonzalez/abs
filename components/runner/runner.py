#!/usr/bin/env python3

import sys
import logging
import os
import subprocess 

class Runner:
    def __init__(self):
        logging.debug("Runner(): Instantiated")

    def run_eceldnetsys(self):
        logging.debug("Runner(): run_eceldnetsys() method called")
        SCRIPT_NAME = "ECELD-Netsys.desktop"
        SCRIPT_DIR = "/home/kali/Desktop"
        ROOT = "sudo"
        
        os.chdir(SCRIPT_DIR)
        cmd = ROOT + " " + os.path.join(os.getcwd(), SCRIPT_NAME)
        running_subprocess = subprocess.run(cmd, shell=True)
        logging.debug("Runner(): Process ran with exit code %d" %running_subprocess.returncode)

        



