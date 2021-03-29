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


class CasualRelationship(QWidget):
    deleted = []
    def __init__(self, treeView: QWidget =None, artifact_id=None,wButtons=True):
        super(QWidget, self).__init__()
        self.artifact_id = artifact_id

        treeView.setMinimumHeight(300)
        self.originalColor = self.palette().color(QtGui.QPalette.Background)
        if wButtons:
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


    def clicked_delete(self):
        self.setAutoFillBackground(True)
        palette = self.palette()

        if self.delete_button_check == 0:
            CasualRelationship.deleted.append(self.artifact_id)
            self.delete_button_check = 1
            palette.setColor(QPalette.Window, QColor("red"))


        elif self.delete_button_check == 1:
            CasualRelationship.deleted.remove(self.artifact_id)
            self.delete_button_check = 0
            palette.setColor(QPalette.Window, self.originalColor)


        self.setPalette(palette)

    def get_deleted(self):
        return self.deleted
    # def clicked_hidden(self):
    #     if self.hide_button_check == 0:
    #         CasualRelationship.hidden.append(self.artifact_id)
    #         self.hide_button_check = 1
    #         self.setAutoFillBackground(True)
    #         palette = self.palette()
    #         palette.setColor(QPalette.Window, QColor("yellow"))
    #         self.setPalette(palette)
    #     else:
    #         if self.hide_button_check == 1:
    #             CasualRelationship.hidden.remove(self.artifact_id)
    #             self.hide_button_check = 0
    #             self.setAutoFillBackground(True)
    #             palette = self.palette()
    #             palette.setColor(QPalette.Window, self.originalColor)
    #             self.setPalette(palette)


# def main():
#     app = QApplication(sys.argv)
#     demo = CasualRelationship()
#     demo.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
