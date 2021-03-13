#!/usr/bin/env python3

import sys
import logging
import os
import subprocess 

class Runner:
    def __init__(self):
        logging.debug("Runner(): Instantiated")

    def run_eceld(self):
        logging.debug("Runner(): run_eceld() method called")
        SCRIPT_NAME = "eceld_service"
        SCRIPT_DIR = "/home/kali/Desktop/eceld"
        ROOT = "sudo"
        
        os.chdir(SCRIPT_DIR)
        cmd = ROOT + " " + os.path.join(os.getcwd(), SCRIPT_NAME)
        running_subprocess = subprocess.run(cmd, shell=True)
        logging.debug("Runner(): Process ran with exit code %d" %running_subprocess.returncode)

        



