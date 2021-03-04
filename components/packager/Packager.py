import sys
import time
import logging
from PyQt5.QtWidgets import *
from JSONFileDialog import JSONFileDialog

class ImportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Import")
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(25, 25, 150, 50)
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(125,100)
        self.pushButton2 = QPushButton("Download", self)
        self.pushButton2.move(200, 35)
        self.pushButton.clicked.connect(self.actionButton2)
        self.pushButton2.clicked.connect(self.actionButton)

    def actionButton(self):
        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)

    def actionButton2(self):
        file_chosen = JSONFileDialog().json_dialog()

class ExportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Export")
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(25, 25, 150, 50)
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(125, 100)
        self.pushButton2 = QPushButton("Create ZIP", self)
        self.pushButton2.move(200, 35)
        self.pushButton.clicked.connect(self.actionButton2)
        self.pushButton2.clicked.connect(self.actionButton)

    def actionButton(self):
        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)

    def actionButton2(self):
        file_chosen = JSONFileDialog().json_dialog()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton("Import Data", self)
        self.pushButton.move(200,200)
        self.pushButton2 = QPushButton("Export Data", self)
        self.pushButton2.move(400,200)
        self.pushButton.clicked.connect(self.importWin)
        self.pushButton2.clicked.connect(self.exportWin)
        self.mainWin()

    def mainWin(self):
        self.setWindowTitle("Packager")
        self.setGeometry(100,100,700,500)
        self.show()

    def importWin(self):
        self.w = ImportWindow()
        self.w.setGeometry(275,250,350,250)
        self.w.show()

    def exportWin(self):
        self.wi = ExportWindow()
        self.wi.setGeometry(275,250,350,250)
        self.wi.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())