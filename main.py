import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.resize(1250, 750)
        self.setWindowTitle("PyQt5")
        # bar = self.menuBar()
        # file = bar.addMenu("File")
        # file.addAction("New")

        # save = QAction("Save", self)
        # save.setShortcut("Ctrl+S")
        # file.addAction(save)

        # edit = file.addMenu("Edit")
        # edit.addAction("copy")
        # edit.addAction("paste")

        # quit = QAction("Quit", self)
        # file.addAction(quit)

        self.label = QLabel(self)
        self.label.setText("Hello World")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50, 20)


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

''' 
Possible GUI to connect all

Main ABS GUI - can move to tabs freely - "no file found" handling
//////////////////////////////////////////////////////////////////
|  tab[exctractor] / tab[builder] / tab[runner]  / tab[packager]  |
|     GUI? button  /     GUI      /  button?GUI  /     GUI        |
|                  /              /shows terminal/                |
|                  /              /              /                |
|                  /              /              /                |
///////////////////////////////////////////////////////////////////
'''