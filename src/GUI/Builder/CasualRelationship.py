from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QAction, QWidget, QFileDialog, \
    QTextEdit, QPushButton, QVBoxLayout, QGridLayout, QTreeView
import sys
import json
from src.GUI.JSONTREE.qjsonmodel import QJsonModel

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
        self.delete_button = QPushButton("Delete")
        self.hide_button = QPushButton("Hide")
        self.delete_button.setMaximumWidth(50)
        self.hide_button.setMaximumWidth(50)
        self.layout.setColumnMinimumWidth(0,500)
        # self.layout.setColumnStretch(0,3)
        # self.layout.setColumnStretch(3,2)

        treeView.setMinimumHeight(200)
        self.layout.addWidget(treeView,0,0)
        self.layout.addWidget(self.hide_button,0,2)
        self.layout.addWidget(self.delete_button,0,3)

        self.setLayout(self.layout)


def main():
    app = QApplication(sys.argv)
    demo = CasualRelationship()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()