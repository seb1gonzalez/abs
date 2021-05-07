import os
import shutil
import json
import logging
import subprocess
import platform

from PyQt5.QtCore import QThread, pyqtSignal

class ExportThread(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal()
    signal3 = pyqtSignal()
    signal4 = pyqtSignal()
    signal5 = pyqtSignal()

    def __init__(self, zip_file, bool_file_list):
        logging.debug("ExportThread(): Instantiated")
        QThread.__init__(self)
        self.zip_file = zip_file
        self.bool_file_list = bool_file_list
        self.os_name = platform.system()
        logging.debug("ExportThread(): Complete")

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
    			flag = 0
    			os.system("mv " + self.zip_file + " /home/osboxes/Desktop/abs/components/packager/Packager2.0")
    			for file in os.listdir("/home/osboxes/Desktop/abs/components/packager/Packager2.0/" + tail):
    				if file.endswith(".ova"):
    					flag = 1
    					name = file
    					filename = file
    			
    			if flag == 1:
    				filename = os.path.splitext(filename)[0]
    				os.chdir("/home/osboxes/Desktop/abs/components/packager/Packager2.0/" + tail)
    				os.system("rm " + name)
    				os.chdir("/home/osboxes/Desktop/abs/components/packager/Packager2.0")
    				
    				os.chdir("/../../../../../../../Program Files/Oracle/VirtualBox/")  # change path for windows directory of vboxmanage executable
    				os.system("vboxmanage export " + filename + " -o C:/Users/peter/Desktop/abs/components/packager/Packager2.0/" + tail + "/" + filename + ".ova")
    				os.chdir("/../../../Users/peter/Desktop/abs/components/packager/Packager2.0")  # change path for windows
    				
    			os.system("zip -r " + tail + ".zip " + tail)
    			os.system("mv " + tail + ".zip /home/osboxes/Desktop")
    			os.system("rm -rf " + tail)
    			
    			self.signal1.emit()
    			self.signal3.emit()
    			self.signal4.emit()
    			
    		except:
    			self.signal2.emit()
    			self.signal3.emit()
    			self.signal5.emit()    				
    				
    	logging.debug("linux_run(): Complete")

    def windows_run(self):
        logging.debug("windows_run(): Instantiated")
        if self.bool_file_list[0]:
            self.signal3.emit()
            try:
                head, tail = os.path.split(self.zip_file)
                flag = 0
                os.system("move " + self.zip_file + " C:/Users/peter/Desktop/abs/components/packager/Packager2.0")
                for file in os.listdir("C:/Users/peter/Desktop/abs/components/packager/Packager2.0/" + tail):
                    if file.endswith(".ova"):
                        flag = 1
                        name = file
                        filename = file

                if flag == 1:
                    filename = os.path.splitext(filename)[0]
                    os.chdir("C:/Users/peter/Desktop/abs/components/packager/Packager2.0/" + tail)
                    os.system("del /q " + name)
                    os.chdir("C:/Users/peter/Desktop/abs/components/packager/Packager2.0")

                    os.chdir("/../../../../../../../Program Files/Oracle/VirtualBox/")  # change path for windows directory of vboxmanage executable
                    os.system("vboxmanage export " + filename + " -o C:/Users/peter/Desktop/abs/components/packager/Packager2.0/" + tail + "/" + filename + ".ova")
                    os.chdir("/../../../Users/peter/Desktop/abs/components/packager/Packager2.0")  # change path for windows

                os.system("tar -C /Users/peter/Desktop/abs/components/packager/Packager2.0 -cvf " + tail + ".tar.gz " + tail)
                os.system("move " + tail + ".tar.gz C:/Users/peter/Desktop")
                os.system("rmdir " + tail + " /s /q")

                self.signal1.emit()
                self.signal3.emit()
                self.signal4.emit()
            except:
                self.signal2.emit()
                self.signal3.emit()
                self.signal5.emit()
        logging.debug("windows_run(): Complete")