from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QAction, QWidget, QFileDialog, \
    QTextEdit, QPushButton, QVBoxLayout, QGridLayout, QTreeView
import sys
import json
from JSONTREE.qjsonmodel import QJsonModel
import queue

 #= queue.Queue()

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class CasualRelationship(QWidget):
    def __init__(self,treeView:QWidget):
        super(QWidget, self).__init__()
        
        

        self.layout = QGridLayout()

        #self.hidden_items = queue.Queue()
        #self.deleted_items = queue.Queue()

        self.delete_button = QPushButton("Delete")
        self.delete_button.setMaximumWidth(50)
        self.delete_button.clicked.connect(self.clicked_delete)     
        self.delete_button_check = 0   

        self.hide_button = QPushButton("Hide")
        self.hide_button.setMaximumWidth(50)
        self.hide_button.clicked.connect(self.clicked_hidden)
        self.hide_button_check = 0

        self.layout.setColumnMinimumWidth(0,500)
        # self.layout.setColumnStretch(0,3)
        # self.layout.setColumnStretch(3,2)

        treeView.setMinimumHeight(200)
        self.layout.addWidget(treeView,0,0)
        self.layout.addWidget(self.hide_button,0,2)
        self.layout.addWidget(self.delete_button,0,3)

        self.setLayout(self.layout)

    def clicked_delete(self):
            if self.delete_button_check == 0:
                self.delete_button_check = 1
                self.setAutoFillBackground(True)
                palette = self.palette()
                palette.setColor(QPalette.Window, QColor("red"))
                self.setPalette(palette)
            elif self.delete_button_check == 1:
                self.delete_button_check = 0
                self.delete_button_check = 1
                self.setAutoFillBackground(True)
                palette = self.palette()
                palette.setColor(QPalette.Window, QColor("white"))
                self.setPalette(palette)
        
    def clicked_hidden(self):
        if self.hide_button_check == 0:
            self.hide_button_check = 1
            self.setAutoFillBackground(True)
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor("yellow"))
            self.setPalette(palette)
        else:
            if self.hide_button_check == 1:
                self.hide_button_check = 0
                self.hide_button_check = 0
                self.hide_button_check = 1
                self.setAutoFillBackground(True)
                palette = self.palette()
                palette.setColor(QPalette.Window, QColor("white"))
                self.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    demo = CasualRelationship()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()