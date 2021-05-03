import os
import shutil
import json
import logging
import subprocess

from PyQt5.QtCore import QThread, pyqtSignal

class ExportThread(QThread):
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
    signal11 = pyqtSignal()

    def __init__(self, config_file, relationship_file, dependency_file, vm_file, bool_file_list):
        logging.debug("ExportThread(): Instantiated")
        QThread.__init__(self)
        self.config_file = config_file
        self.relationship_file = relationship_file
        self.dependency_file = dependency_file
        self.vm_file = vm_file
        self.bool_file_list = bool_file_list
        logging.debug("ExportThread(): Complete")

    def run(self):
        logging.debug("run(): Instantiated")
        if self.bool_file_list[0]:
            self.signal9.emit()
            try:
                json_file = open(self.config_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + os.path.normpath('/GeneratedData/Config.JSON'), 'w') as outfile:
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
                with open(os.getcwd() + os.path.normpath('/GeneratedData/Relationships.JSON'), 'w') as outfile:
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
                with open(os.getcwd() + os.path.normpath('/GeneratedData/Dependency.JSON'), 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal5.emit()
                self.signal9.emit()
            except:
                self.signal6.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        self.signal9.emit()
        if self.bool_file_list[3]:
            self.signal9.emit()
            try:
                tempstr = os.path.normpath("C:/Users/peter/Desktop/abs/components/packager/Packager2.0/GeneratedData") #path that needs to change on install
                #newstr = '\\'.join(self.vm_file.split('/'))
                newstr = os.path.normpath(self.vm_file)
                os.system("copy " + f'"{newstr}"' + " " + f'"{tempstr}"')
                self.signal7.emit()
                self.signal9.emit()
            except:
                self.signal8.emit()
                self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        try:
            zip_location = os.getcwd() + os.path.normpath('/ExportZipData/ABSExport.zip')
            export_directory = os.getcwd() + os.path.normpath('/GeneratedData')
            os.system("tar.exe -a -c -f " + zip_location + " " + export_directory)
            self.signal10.emit()
        except:
            self.signal11.emit()
        logging.debug("run(): Complete")