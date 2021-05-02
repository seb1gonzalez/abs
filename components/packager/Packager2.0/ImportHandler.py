import os
import json
import logging
import platform

from PyQt5.QtCore import QThread, pyqtSignal

class ImportThread(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal()
    signal3 = pyqtSignal()
    signal4 = pyqtSignal()
    signal5 = pyqtSignal()
    signal6 = pyqtSignal()
    signal7 = pyqtSignal()
    signal8 = pyqtSignal()
    signal9 = pyqtSignal()
    signal10 = pyqtSignal()

    def __init__(self, config_file, relationship_file, dependency_file, vm_file, bool_file_list):
        logging.debug("ImportThread(): Instantiated")
        QThread.__init__(self)
        self.config_file = config_file
        self.relationship_file = relationship_file
        self.dependency_file = dependency_file
        self.vm_file = vm_file
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
            self.signal9.emit()
            try:
                json_file = open(self.config_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))) + '/src/Config/Config.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal1.emit()
                self.signal9.emit()
            except:
                self.signal2.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[1]:
            self.signal9.emit()
            try:
                json_file = open(self.relationship_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))) + '/src/GeneratedData/Relationships.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal3.emit()
                self.signal9.emit()
            except:
                self.signal4.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[2]:
            self.signal9.emit()
            try:
                json_file = open(self.dependency_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))) + '/src/dependency/Dependency.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal5.emit()
                self.signal9.emit()
            except:
                self.signal6.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        self.signal10.emit()
        logging.debug("linux_run(): Complete")

    def windows_run(self):
        logging.debug("windows_run(): Instantiated")
        if self.bool_file_list[0]:
            self.signal9.emit()
            try:
                json_file = open(self.config_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + os.path.normpath('/../../../src/Config/Config.JSON'), 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal1.emit()
                self.signal9.emit()
            except:
                self.signal2.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[1]:
            self.signal9.emit()
            try:
                json_file = open(self.relationship_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + os.path.normpath('/../../../src/Relations/Relationships.JSON'), 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal3.emit()
                self.signal9.emit()
            except:
                self.signal4.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[2]:
            self.signal9.emit()
            try:
                json_file = open(self.dependency_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + os.path.normpath('/../../../src/dependency/Dependency.JSON'), 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal5.emit()
                self.signal9.emit()
            except:
                self.signal6.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[3]:
            self.signal9.emit()
            try:
                head, tail = os.path.split(self.vm_file)
                tail = os.path.splitext(tail)[0]
                os.chdir("/../../../../../../Program Files/Oracle/VirtualBox/") #change path for windows directory of vboxmanage executable
                os.system("vboxmanage export " + str(tail) + " -o " + str(tail) + ".ova")
                os.chdir("/../../../Users/peter/Desktop/abs/components/packager/Packager2.0") #change path for windows
                tempstr = os.getcwd() + os.path.normpath('/../../../src/OVAFile')
                newstr = os.path.normpath("C:/Program Files/Oracle/VirtualBox/") + str(tail) + ".ova"
                os.system("copy " + f'"{newstr}"' + " " + f'"{tempstr}"')
                self.signal7.emit()
                self.signal9.emit()
            except:
                self.signal8.emit()
                self.signal9.emit()
        self.signal10.emit()
        logging.debug("windows_run(): Complete")