#!/usr/bin/env python3

import sys
import logging
import os
import subprocess 

class Runner:
    def __init__(self):
        logging.debug("Runner(): Instantiated")

    def run_eceldnetsys():
        logging.debug("Runner(): run_eceldnetsys() method called")
        SCRIPT_NAME = "ECELD-Netsys.desktop"
        ROOT = "sudo"
        os.chdir("/home/kali/Desktop")
        cmd = ROOT + " " + os.path.join(os.getcwd(), SCRIPT_NAME)
        running_subprocess = subprocess.run(cmd, shell=True)
        logging.debug("Runner(): Process ran with exit code %d" %running_subprocess.returncode)
<<<<<<< HEAD

        
=======
    
>>>>>>> 7c32c6826138ebe5b2a79ec39ea9fdb7b1d43633



