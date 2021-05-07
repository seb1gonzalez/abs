import os
import json
import logging
import platform
import zipfile
import glob

from PyQt5.QtCore import QThread, pyqtSignal

class ImportThread(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal()
    signal3 = pyqtSignal()
    signal4 = pyqtSignal()

    def __init__(self, zip_file, bool_file_list):
        logging.debug("ImportThread(): Instantiated")
        QThread.__init__(self)
        self.zip_file = zip_file
        self.bool_file_list = bool_file_list
        self.os_name = platform.system()
        logging.debug("ImportThread(): Complete")

    def run(self):
        logging.debug("run(): Instantiated")
        if self.os_name == "Linux":
            self.linux_run()
        elif self.os_name == "Windows":
            self.windows_run()
        logging.debug("run(): Complete")
        
    def linux_run(self):
    	logging.debug("linux_run(): Instantiated")
    	if self.bool_file_list[0]:
    		self.signal3.emit()
    		try:
    			head, tail = os.path.split(self.zip_file)
    			tail = os.path.splitext(tail)[0]
    			tail = os.path.splitext(tail)[0]
    			flag = 0
    			
    			os.system("unzip " + self.zip_file + " -d /home/osboxes/Desktop/abs/src/Data")
    			for file in os.listdir("/home/osboxes/Desktop/abs/src/Data/" + tail):
    				if file.endswith(".ova"):
    					flag = 1
    					filename = file
    					
    			if flag == 1:
    				os.chdir("/../../../../../../../Program Files/Oracle/VirtualBox/")  # change path for windows directory of vboxmanage executable
    				os.system("vboxmanage import C:/Users/peter/Desktop/abs/src/Data/" + tail + "/" + filename)
    				os.chdir("/../../../Users/peter/Desktop/abs/components/packager/Packager2.0") #change path for windows
    					
    			self.signal1.emit()
    			self.signal3.emit()
    		except:
    			self.signal2.emit()
    			self.signal3.emit()
    		self.signal4.emit()
    	logging.debug("linux_run(): Complete")

    def windows_run(self):
        logging.debug("windows_run(): Instantiated")
        if self.bool_file_list[0]:
            self.signal3.emit()
            try:
                print(self.zip_file)
                head, tail = os.path.split(self.zip_file)
                tail = os.path.splitext(tail)[0]
                tail = os.path.splitext(tail)[0]
                flag = 0
                os.system("tar -C /Users/peter/Desktop/abs/src/Data -zxvf " + self.zip_file)
                for file in os.listdir("C:/Users/peter/Desktop/abs/src/Data/" + tail):
                    if file.endswith(".ova"):
                        flag = 1
                        filename = file

                if flag == 1:
                    os.chdir("/../../../../../../../Program Files/Oracle/VirtualBox/")  # change path for windows directory of vboxmanage executable
                    os.system("vboxmanage import C:/Users/peter/Desktop/abs/src/Data/" + tail + "/" + filename)
                    os.chdir("/../../../Users/peter/Desktop/abs/components/packager/Packager2.0") #change path for windows

                self.signal1.emit()
                self.signal3.emit()
            except:
                self.signal2.emit()
                self.signal3.emit()
        self.signal4.emit()
        logging.debug("windows_run(): Complete")