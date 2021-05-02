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
    #flag1 = 0
    #flag2 = 0
    #flag3 = 0
    #flag4 = 0
    #flag5 = 0

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
                with open(os.getcwd() + '\\GeneratedData\\Config.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal1.emit()
                self.signal9.emit()
            except:
                #flag1 = 1
                self.signal2.emit()
                self.signal9.emit()
            #if flag1 = 1: #linux
                #flag1 = 0
                #try:
                #    json_file = open(self.config_file)
                #    temp_data = json.load(json_file)
                #    json_file.close()
                #    with open(os.getcwd() + '/GeneratedData/Config.JSON', 'w') as outfile:
                #        json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                #    self.signal1.emit()
                #    self.signal9.emit()
                #except:
                #    self.signal2.emit()
                #    self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[1]:
            self.signal9.emit()
            try:
                json_file = open(self.relationship_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + '\\GeneratedData\\Relationships.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal3.emit()
                self.signal9.emit()
            except:
                #flag2 = 1
                self.signal4.emit()
                self.signal9.emit()
            #if flag2 = 1: #linux
            #    flag2 = 0
            #    try:
            #        json_file = open(self.relationship_file)
            #        temp_data = json.load(json_file)
            #        json_file.close()
            #        with open(os.getcwd() + '/GeneratedData/Relationships.JSON', 'w') as outfile:
            #            json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
            #        self.signal3.emit()
            #        self.signal9.emit()
            #    except:
            #        self.signal4.emit()
            #        self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        if self.bool_file_list[2]:
            self.signal9.emit()
            try:
                json_file = open(self.dependency_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + '\\GeneratedData\\Dependency.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal5.emit()
                self.signal9.emit()
            except:
                #flag3 = 1
                self.signal6.emit()
                self.signal9.emit()
            #if flag3 = 1:
            #    flag3 = 0
            #    try:
            #        json_file = open(self.dependency_file)
            #        temp_data = json.load(json_file)
            #        json_file.close()
            #        with open(os.getcwd() + '/GeneratedData/Dependency.JSON', 'w') as outfile:
            #            json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
            #        self.signal5.emit()
            #        self.signal9.emit()
            #    except:
            #        self.signal6.emit()
            #        self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        self.signal9.emit()
        if self.bool_file_list[3]:
            self.signal9.emit()
            try:
                tempstr = "C:\\Users\\peter\\Desktop\\abs\\components\\packager\\Packager2.0\\GeneratedData" #path that needs to change on install
                newstr = '\\'.join(self.vm_file.split('/'))
                os.system("copy " + f'"{newstr}"' + " " + f'"{tempstr}"')
                self.signal7.emit()
                self.signal9.emit()
            except:
                #flag4 = 1
                self.signal8.emit()
                self.signal9.emit()
            #if flag4 = 1:
            #    flag4 = 0
            #    try:
            #        os.system("cp " + f'"{self.vm_file}"' + " " + "/GeneratedData")
            #        self.signal7.emit()
            #        self.signal9.emit()
            #    except:
            #        self.signal8.emit()
            #        self.signal9.emit()
        else:
            self.signal9.emit()
            self.signal9.emit()
        try:
            zip_location = os.getcwd() + '\\ExportZipData\\ABSExport.zip'
            export_directory = os.getcwd() + '\\GeneratedData'
            os.system("tar.exe -a -c -f " + zip_location + " " + export_directory)
            self.signal10.emit()
        except:
            #flag5 = 1
            self.signal11.emit()
        #if flag5 = 1:
        #    flag5 = 0
        #    try:
        #        zip_location = os.getcwd() + '/ExportZipData/ABSExport.zip'
        #        export_directory = os.getcwd() + '/GeneratedData'
        #        subprocess.run(["zip", "-j", "-r", zip_location, export_directory])
        #        self.signal10.emit()
        #    except:
        #        self.signal11.emit()
        logging.debug("run(): Complete")