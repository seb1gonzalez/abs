import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QVBoxLayout, QWidget)

class ImportWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Import")
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(125,100)
        #self.pushButton.clicked.connect(self.mainWin)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton("Import Data", self)
        self.pushButton.move(200,200)
        self.pushButton2 = QPushButton("Export Data", self)
        self.pushButton2.move(400,200)
        self.pushButton.clicked.connect(self.secWin)
        self.mainWin()

    def mainWin(self):
        self.setWindowTitle("Packager")
        self.setGeometry(100,100,700,500)
        self.show()

    def secWin(self):
        self.w = ImportWindow()
        self.w.setGeometry(275,250,350,250)
        self.w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())