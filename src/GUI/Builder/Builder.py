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

            self.document = None
            self.casual_relationship = None
            self.casual_dependency = None
            #self.json_tree_view = None

            self.dropdown = QComboBox()
            self.dropdown.addItems(["Network", "Mouse-Clicks", "Keystrokes"])
            # self.dropdown.addItem("Network")
            # self.dropdown.addItem("Mouse-Clicks")
            # self.dropdown.addItem("Keystrokes")

            self.hbox = QHBoxLayout()
            self.vbox = QVBoxLayout()

            self.hbox.addWidget(self.button_import)
            self.hbox.addWidget(self.button_save)
            self.hbox.addWidget(self.button_undo)
            self.hbox.addWidget(self.dropdown)
            self.hbox.setAlignment(Qt.AlignTop)

            self.hbox_rel_dep = QHBoxLayout()
            self.vbox_relationship = QVBoxLayout()
            self.vbox_dependencies = QVBoxLayout()



            #self.hbox_rel_dep.addWidget(self.vbox_relationship)
            #self.hbox_rel_dep.addStretch(1)
            #self.hbox_rel_dep.addWidget(self.vbox_dependencies)
            
            self.hbox_rel_dep.addLayout(self.vbox_relationship)
            self.hbox_rel_dep.addLayout(self.vbox_dependencies)
            self.hbox_rel_dep.setAlignment(Qt.AlignTop)

            #self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
            #self.widget = QWidget() 


            self.vbox.addLayout(self.hbox)
            #self.vbox.addStretch(1)
            self.vbox.addLayout(self.hbox_rel_dep)
            self.setLayout(self.vbox)
            # self.widget.setLayout(self.vbox)
            # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            # self.scroll.setWidgetResizable(True)
            # self.scroll.setWidget(self.widget)

            #self.setCentralWidget(self.scroll)

            # self.button1 = QPushButton('Import script')
            # self.button1.setMaximumWidth(80)
            # self.button1.setGeometry(0,0,80,20)
            self.button_import.clicked.connect(self.get_text_file)
            self.button_save.clicked.connect(self.save_changes)
            # self.layout.addWidget(self.button1)
            # self.setLayout(self.layout)
        except Exception:
            traceback.print_exc()
    
    def save_changes(self):
        if len(CasualRelationship.deleted) == 0 and len(CasualRelationship.hidden) == 0:
            return
        try:  
            index = 1
                          
            #scrollWidget = QScrollArea()
            #scrollWidget.setMinimumHeight(500)
            #self.vbox.addWidget(scrollWidget)
                 
                        
            for i in range(len(self.document)):
                #print("Lets see")
                data = self.document[i]
                #print(data)
                if data['Artifact_id'] in CasualRelationship.deleted:
                    print("its in deleted")
                    continue
                if data['Artifact_id'] in CasualRelationship.hidden:
                    print("itsin hidden")
                    continue

                #for key in data:
                     #print("This is the data = {}".format(key))
                # if (data['Artifact_id'] not in CasualRelationship.hidden) or (data['Artifact_id'] not in CasualRelationship.deleted):
                #     print(data)
                json_model = QJsonModel()
                json_tree_view = QTreeView()
                json_tree_view.setModel(json_model)
                json_model.load(data)
                self.casual_dependency = CasualRelationship(json_tree_view, data['Artifact_id'])
                self.vbox_dependencies.addWidget(self.casual_dependency)
                       
                            
                if index == 3:
                    break
                index +=1
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
                        index = 1
                          
                        #scrollWidget = QScrollBar()
                        #scrollWidget.setMinimumHeight(500)
                        #self.vbox.addWidget(scrollWidget)
                 
                        
                        for i in range(len(self.document)):
                            data = self.document[i]
                            print(data)
                            json_model = QJsonModel()
                            json_tree_view = QTreeView()
                            json_tree_view.setModel(json_model)
                            json_model.load(data)
                            self.casual_relationship = CasualRelationship(json_tree_view, data['Artifact_id'])
                            self.vbox_relationship.addWidget(self.casual_relationship)
                       
                            
                            if index == 3:
                                break
                            index +=1
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
