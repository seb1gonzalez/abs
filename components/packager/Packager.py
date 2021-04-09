import sys
import time
import gzip
import json
import ntpath
import logging
import zipfile

from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from JFileDialog import JFileDialog

list = [] #filenames to display in import
list2 = [] #filenames to display in export
dataFile = [] #imported data
dataFile2 = [] #exporting to zip data
dataFile3 = []
dataFile4 = []
substring = ".json"

class ImportWindow(QWidget):
    def __init__(self):
        super().__init__()
        global list
        list = []
        self.setWindowTitle("Import")
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(130, 25, 150, 50)
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(125,100)
        self.label1 = QLabel("", self)
        self.label1.setFixedWidth(10000)
        self.label1.move(30, 150)
        self.pushButton.clicked.connect(self.actionButton2)

    def actionButton2(self):
        file_chosen = JFileDialog().json_dialog() #file select
        for i in range(101): #progress bar
            time.sleep(0.05)
            self.pbar.setValue(i)
        head, name = ntpath.split(file_chosen) #obtain file name
        list.append(name) #add to list
        if substring in name:
            with open(file_chosen) as f:
                data = json.load(f)
                dataFile.append(data)
        else:
            data2 = open(file_chosen)
            dataFile.append(data2.read())
        #print(list)
        print(dataFile)
        temp = " ".join(list)
        self.label1.setText(temp)

class ExportWindow(QWidget):
    def __init__(self):
        super().__init__()
        global list2
        list2 = []
        self.setWindowTitle("Export")
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(25, 25, 150, 50)
        self.pbar2 = QProgressBar(self)
        self.pbar2.setGeometry(25, 85, 150, 50)
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(200, 92)
        self.pushButton2 = QPushButton("ZIP File", self)
        self.pushButton2.move(200, 32)
        self.label2 = QLabel("", self)
        self.label2.setFixedWidth(10000)
        self.label2.move(30, 150)
        self.pushButton.clicked.connect(self.actionButton2)
        self.pushButton2.clicked.connect(self.actionButton)

    def actionButton(self):
        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)

        fileData = json.dumps(dataFile2, indent=2).encode("utf-8")
        print(fileData)
        output = gzip.open("test.json.gz", "wb")
        output.write(fileData)
        output.close()

    def actionButton2(self):
        file_chosen = JFileDialog().json_dialog()
        for i in range(101):
            time.sleep(0.05)
            self.pbar2.setValue(i)
        head, name = ntpath.split(file_chosen)
        list2.append(name)
        if substring in name:
            with open(file_chosen) as f:
                data = json.load(f)
                dataFile2.append(data)
        else:
            data2 = open(file_chosen, "r")
            dataFile2.append(data2.read())
        temp = " ".join(list2)
        self.label2.setText(temp)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton("Import Data", self)
        self.pushButton.move(100,50)
        self.pushButton2 = QPushButton("Export Data", self)
        self.pushButton2.move(100,100)
        self.pushButton.clicked.connect(self.importWin)
        self.pushButton2.clicked.connect(self.exportWin)
        self.mainWin()

    def mainWin(self):
        self.setWindowTitle("Packager")
        self.setGeometry(100,100,300,200)
        self.show()

    def importWin(self):
        self.w = ImportWindow()
        self.w.setGeometry(275,250,350,200)
        self.w.show()

    def exportWin(self):
        self.wi = ExportWindow()
        self.wi.setGeometry(275,250,350,200)
        self.wi.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())