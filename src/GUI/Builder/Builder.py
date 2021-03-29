import json
from JSONTREE.qjsonmodel import QJsonModel
import traceback

import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QAction, QWidget, QFileDialog, \
     QTextEdit, QPushButton, QVBoxLayout, QGridLayout, QTreeView, QListView, QListWidget, QScrollArea, QComboBox
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QDir
from Builder.CasualRelationship import CasualRelationship
# from BuilderTreeView import TreeviewBuilder

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Builder(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        try:

            self.button_import = QPushButton("Import")
            self.button_import.clicked.connect(self.get_text_file)

            self.button_save = QPushButton("Save")
            self.button_undo = QPushButton("Undo")

            self.hbox = QHBoxLayout()
            self.vbox = QVBoxLayout()


            self.hbox.addWidget(self.button_import)
            self.hbox.addWidget(self.button_save)
            self.hbox.addWidget(self.button_undo)
            self.hbox.setAlignment(Qt.AlignTop)

            self.vbox.addLayout(self.hbox)
            self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
            self.widget = QWidget()# Widget that contains the collection of Vertical Box
            self.vbox_scroll = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
            self.vbox_scroll.setAlignment(Qt.AlignTop)
            size = QRect()
            size.setWidth(300)
            size.setHeight(800)
            self.vbox_scroll.setGeometry(size)
            self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroll.setWidgetResizable(True)



            self.setLayout(self.vbox)


        except Exception:
            traceback.print_exc()

    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        dialog.setNameFilter(("JSON (*.json *.JSON)"))
        if dialog.exec_():
            file_name = dialog.selectedFiles()
            if file_name[0].endswith(('.json', '.JSON')):
                # Opens any file in the JSON format / Abre el JSON file y lo guarda como 'json_file'
                with open(file_name[0]) as json_file:
                    document: dict = json.load(json_file)
                    try:
                        for i in range(len(document)):
                            data = document[i]
                            json_model = QJsonModel()
                            json_tree_view = QTreeView()
                            json_tree_view.setModel(json_model)
                            json_model.load(data)
                            casual_relationship = CasualRelationship(json_tree_view)
                            self.vbox_scroll.addWidget(casual_relationship)
                        self.widget.setLayout(self.vbox_scroll)
                        self.scroll.setWidget(self.widget)
                        self.vbox.addWidget(self.scroll)

                    except Exception:
                        traceback.print_exc()
                    json_file.close()
            else:
                pass

#  if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo = DialogApp()
#     demo.show()
#     sys.exit(app.exec_())
