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
            self.button_save = QPushButton("Save")
            self.button_undo = QPushButton("Undo")
            self.button_import.clicked.connect(self.get_text_file)
            self.button_save.clicked.connect(self.save_changes)

            self.document = None
            self.casual_relationship = None
            self.casual_dependency = None
            self.json_model = None
            self.json_tree_view = None
            self.data = None

            self.hbox = QHBoxLayout()
            self.vbox = QVBoxLayout()

            self.hbox.addWidget(self.button_import)
            self.hbox.addWidget(self.button_save)
            self.hbox.addWidget(self.button_undo)
            self.hbox.setAlignment(Qt.AlignTop)
            self.hbox_rel_dep = QHBoxLayout()

            self.vbox_relationship = QVBoxLayout()
            self.vbox_dependencies = QVBoxLayout()

            self.hbox_rel_dep.addLayout(self.vbox_relationship)
            self.hbox_rel_dep.addLayout(self.vbox_dependencies)
            self.hbox_rel_dep.setAlignment(Qt.AlignTop)

            self.scroll_left = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
            self.scroll_wid_left = QWidget()  # Widget that contains the collection of Vertical Box
            self.vbox_scroll_left = QVBoxLayout()

            self.scroll_wid_left.setMinimumSize(300,700)

            self.scroll_right = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
            self.scroll_wid_right = QWidget()  # Widget that contains the collection of Vertical Box

            # Scroll Area Properties
            self.scroll_left.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scroll_left.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroll_left.setWidgetResizable(True)

            self.vbox.addLayout(self.hbox)
            self.vbox.addLayout(self.hbox_rel_dep)

            self.setLayout(self.vbox)
        except Exception:
            traceback.print_exc()
    
    def save_changes(self):
        if len(CasualRelationship.deleted) == 0 and len(CasualRelationship.hidden) == 0:
            return
        try:
            for i in range(len(self.document)):
                data = self.document[i]
                json_model = QJsonModel()
                json_tree_view = QTreeView()
                json_tree_view.setModel(json_model)
                json_model.load(data)
                self.casual_dependency = CasualRelationship(json_tree_view, data['Artifact_id'])
                self.vbox_dependencies.addWidget(self.casual_dependency)
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
                    self.document: dict = json.load(json_file)
                    print(self.document)
                    try:
                        for i in range(len(self.document)):
                            self.data = self.document[i]
                            self.json_model = QJsonModel()
                            self.json_tree_view = QTreeView()
                            self.json_tree_view.setModel(self.json_model)
                            self.json_model.load(self.data)
                            self.casual_relationship = CasualRelationship(self.json_tree_view, self.data['Artifact_id'])
                            self.vbox_scroll_left.addWidget(self.casual_relationship)
                        self.scroll_wid_left.setLayout(self.vbox_scroll_left)
                        self.vbox_relationship.addWidget(self.scroll_wid_left)

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
