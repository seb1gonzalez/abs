from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QAction, QWidget, QFileDialog, \
    QTextEdit, QPushButton, QVBoxLayout, QGridLayout, QTreeView
import sys
import json
from JSONTREE.qjsonmodel import QJsonModel


# import queue

# = queue.Queue()

# hidden = []
# deleted = []

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class CausalRelationship(QWidget):
    deleted = []
    all_data = []
    def __init__(self, treeView: QWidget =None, artifact_id=None,wButtons=True):
        super(QWidget, self).__init__()
        self.artifact_id = artifact_id
        treeView.setMinimumHeight(300)

        self.originalColor = self.palette().color(QtGui.QPalette.Background)
        if wButtons:
            CausalRelationship.all_data.append(treeView)
            self.layout = QGridLayout()
            self.layout.addWidget(treeView, 0, 0, 0, 1)
            self.delete_button = QPushButton("Delete")
            self.delete_button.setMaximumWidth(50)
            self.delete_button.clicked.connect(self.clicked_delete)
            self.delete_button_check = 0
            self.layout.addWidget(self.delete_button, 0, 2)
        else:
            self.layout = QVBoxLayout()
            treeView.setMinimumWidth(800)
            self.layout.addWidget(treeView)
        self.setLayout(self.layout)

    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasText():
    #         event.acceptProposedAction()
    #
    # def dropEvent(self, event):
    #     pos = event.pos()
    #     text = event.mimeData().text()
    #     self.setText(text)
    #     event.acceptProposedAction()

    def clicked_delete(self):
        self.setAutoFillBackground(True)
        palette = self.palette()

        if self.delete_button_check == 0:
            CausalRelationship.deleted.append(self.artifact_id)
            self.delete_button_check = 1
            palette.setColor(QPalette.Window, QColor("red"))


        elif self.delete_button_check == 1:
            CausalRelationship.deleted.remove(self.artifact_id)
            self.delete_button_check = 0
            palette.setColor(QPalette.Window, self.originalColor)


        self.setPalette(palette)

    def get_deleted(self):
        return self.deleted
