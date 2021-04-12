import json
from JSONTREE.qjsonmodel import QJsonModel
import traceback

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QAction, QWidget, QFileDialog, \
     QTextEdit, QPushButton, QVBoxLayout, QGridLayout, QTreeView, QListView, QListWidget, QScrollArea, QComboBox
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QDir
from Builder.CausalRelationship import CausalRelationship
# from BuilderTreeView import TreeviewBuilder

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Builder(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        try:

            self.button_import = QPushButton("Import")
            self.button_import.setMaximumWidth(80)

            self.button_save = QPushButton("Save")
            self.button_save.setMaximumWidth(80)

            self.button_undo = QPushButton("Undo")
            self.button_undo.setMaximumWidth(80)

            self.button_generate = QPushButton("Generate")
            self.button_generate.setMaximumWidth(100)
            self.button_generate.setEnabled(False)

            self.button_import.clicked.connect(self.get_text_file)
            self.button_generate.clicked.connect(self.generate_dependencies)

            self.document = None
            self.causal_relationship = None
            self.causal_dependency = None
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
            self.hbox_rel_dep.addWidget(self.button_generate)
            self.hbox_rel_dep.addLayout(self.vbox_dependencies)
            self.hbox_rel_dep.setAlignment(Qt.AlignTop)

            self.scroll_left_area = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
            self.widget_scroll_left = QWidget()  # Widget that contains the collection of Vertical Box
            self.vbox_scroll_left = QVBoxLayout()

            # self.scroll_wid_left.setMinimumSize(300,700)

            self.scroll_area_right = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
            self.widget_scroll_right = QWidget()  # Widget that contains the collection of Vertical Box
            self.vbox_scroll_right = QVBoxLayout()
            # Scroll Area Properties
            self.scroll_left_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scroll_left_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_left_area.setWidgetResizable(True)

            self.scroll_area_right.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scroll_area_right.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area_right.setWidgetResizable(True)

            self.widget_scroll_left.setLayout(self.vbox_scroll_left)
            self.scroll_left_area.setWidget(self.widget_scroll_left)
            self.vbox_relationship.addWidget(self.scroll_left_area)

            self.widget_scroll_right.setLayout(self.vbox_scroll_right)
            self.scroll_area_right.setWidget(self.widget_scroll_right)
            self.vbox_dependencies.addWidget(self.scroll_area_right)

            self.vbox.addLayout(self.hbox)
            self.vbox.addLayout(self.hbox_rel_dep)

            self.setLayout(self.vbox)

        except Exception:
            traceback.print_exc()
    
    def generate_dependencies(self):
        try:
            skip: list = CausalRelationship.deleted
            for s in skip:
                self.document[s] = False
            with open('Builder/builder_out/builder_generated_dependencies.json', 'w') as outfile:
                json.dump(self.document, outfile, indent=4,check_circular=True,sort_keys=True)

            for i in range(len(self.document)):
                self.data = self.document[i]
                if self.data:
                    self.json_model = QJsonModel()
                    self.json_tree_view = QTreeView()
                    self.json_tree_view.setModel(self.json_model)
                    self.json_model.load(self.data)
                    self.causal_dependency = CausalRelationship(self.json_tree_view,i,False)
                    self.vbox_scroll_right.addWidget(self.causal_dependency)

            self.widget_scroll_right.setLayout(self.vbox_scroll_right)
            self.scroll_area_right.setWidget(self.widget_scroll_right)
            self.vbox_dependencies.addWidget(self.scroll_area_right)


        except Exception as e:
            print(e)
            traceback.print_exc()


    def leftScreen(self,document):
        for i in range(len(self.document)):
            self.data = self.document[i]
            self.json_model = QJsonModel()
            self.json_tree_view = QTreeView()
            self.json_tree_view.setModel(self.json_model)
            self.json_model.load(self.data)
            self.causal_relationship:QWidget = CausalRelationship(self.json_tree_view, i)
            self.vbox_scroll_left.addWidget(self.causal_relationship)
        self.widget_scroll_left.setLayout(self.vbox_scroll_left)
        self.scroll_left_area.setWidget(self.widget_scroll_left)
        self.vbox_relationship.addWidget(self.scroll_left_area)


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
                    json_file.close()
                    self.better_relationships(self.document)
                try:
                    self.button_generate.setEnabled(True)
                    self.leftScreen(self.document)

                except Exception:
                    traceback.print_exc()


            else:
                pass

    def better_relationships(self,json_data):
        try:
            # store ID->relationship array
            relationship_map = {}

            # store ID -> data without Artifact relationships
            data_key_map = {}

            # final product
            finale = []

            for element in json_data:
                relationship_id = element["Artifact_id"]
                relationship_arr = element["Artifact_Relationships"]
                relationship_map[relationship_id] = relationship_arr
                new_keys = {}

                for data_key in element:
                    if data_key == "Artifact_Relationships":
                        continue
                    else:
                        new_keys[data_key] = element[data_key]

                    data_key_map[relationship_id] = new_keys

            # replace relationship ID with actual data
            for key in relationship_map:
                arr = relationship_map[key]
                for i in range(len(arr)):
                    rel = arr[i]
                    data = data_key_map[rel]
                    arr[i] = data

            # for element in json_data:
            #     id = element["Artifact_id"]
            #     new_json_data = {}
            #     data = data_key_map[id]
            #     new_json_data[id] = data
            #     finale.append(new_json_data)
            #
            # return finale




        except Exception:
            traceback.print_exc()

    def search_feature(self):
        # Appending all JSON values from dictionary into a 2D array list
        self.array = []
        for i in range(len(self.document)):
            if 'title' in self.document[i] and 'content' in self.document[i] and 'y' in self.document[i]:
                self.array.append(
                    [str(self.document[i]['Artifact_id']), self.document[i]['start'], self.document[i]['title'],
                     self.document[i]['content'], self.document[i]['y']])
            elif 'content' in self.document[i] and 'title' in self.document[i]:
                self.array.append(
                    [str(self.document[i]['Artifact_id']), self.document[i]['start'], self.document[i]['title'],
                     self.document[i]['content'], ''])
            elif 'content' in self.document[i]:
                self.array.append(
                    [str(self.document[i]['Artifact_id']), self.document[i]['start'], '', self.document[i]['content'],
                     ''])
            else:
                self.array.append([str(self.document[i]['Artifact_id']), self.document[i]['start'], '', '', ''])

        # Creating the standard model for filtering
        self.model = QStandardItemModel(len(self.array), len(self.array[0]))
        self.model.setHorizontalHeaderLabels(['Artifact ID', 'Start time', 'Title', 'Content', 'Y'])
        # Inserting every item of the 2D array into the model an an Item object
        for row in range(len(self.array)):
            for col in range(len(self.array[i])):
                self.item = QStandardItem(self.array[row][col])
                self.model.setItem(row, col, self.item)
        # Setting the Filter Proxy model for filtering data
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(-1)
        # Adding the Search bar feature in the Layout
        search_label = QLabel('Search bar: ')
        self.search_field = QLineEdit()
        self.search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.hbox.addWidget(search_label)
        self.hbox.addWidget(self.search_field)