import os
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

    def __init__(self, config_file, relationship_file, dependency_file, bool_file_list):
        logging.debug("ExportThread(): Instantiated")
        QThread.__init__(self)
        self.config_file = config_file
        self.relationship_file = relationship_file
        self.dependency_file = dependency_file
        self.bool_file_list = bool_file_list
        logging.debug("ExportThread(): Complete")

    def run(self):
        logging.debug("run(): Instantiated")
        if self.bool_file_list[0]:
            self.signal7.emit()
            try:
                json_file = open(self.config_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + '/../../src/GeneratedData/ExportFiles/ConfigExport.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal1.emit()
                self.signal7.emit()
            except:
                self.signal2.emit()
                self.signal7.emit()
        else:
            self.signal7.emit()
            self.signal7.emit()
        if self.bool_file_list[1]:
            self.signal7.emit()
            try:
                json_file = open(self.relationship_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + '/../../src/GeneratedData/ExportFiles/RelationshipsExport.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal3.emit()
                self.signal7.emit()
            except:
                self.signal4.emit()
                self.signal7.emit()
        else:
            self.signal7.emit()
            self.signal7.emit()
        if self.bool_file_list[2]:
            self.signal7.emit()
            try:
                json_file = open(self.dependency_file)
                temp_data = json.load(json_file)
                json_file.close()
                with open(os.getcwd() + '/../..\src/GeneratedData/ExportFiles/nejfladlfjlasjflslkfjlskjffExport.JSON', 'w') as outfile:
                    json.dump(temp_data, outfile, ensure_ascii=False, indent=4)
                self.signal5.emit()
                self.signal7.emit()
            except:
                self.signal6.emit()
                self.signal7.emit()
        else:
            self.signal7.emit()
            self.signal7.emit()
        self.signal7.emit()
        try:
            zip_location = os.getcwd() + '/../../src/GeneratedData/ExportZipData/ABSExport.zip'
            export_directory = os.getcwd() + '/../../src/GeneratedData/ExportFiles/'
            subprocess.run(["zip", "-j", "-r", zip_location, export_directory])
            self.signal8.emit()
        except:
            self.signal9.emit()
        logging.debug("run(): Complete")