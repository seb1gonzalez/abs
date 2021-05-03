import json
import datetime
import traceback
import sys

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
            # self.button_undo = QPushButton("Undo")
            # self.button_undo.setMaximumWidth(80)
            self.button_undo_deleted_rows = QPushButton("Restore Rows")
            self.button_undo_deleted_rows.setMaximumWidth(100)

            self.button_delta_time = QPushButton("Adjust Delta Time")

            self.button_generate = QPushButton("Export")
            self.button_generate.setMaximumWidth(80)
            self.button_delete = QPushButton("Delete Selected")
            self.button_delete.setStyleSheet("background-color:#ff1744;")
            self.button_delete.setMaximumWidth(100)

            self.button_delta_time.setEnabled(False)
            self.button_save.setEnabled(False)
            self.button_generate.setEnabled(False)
            self.button_delete.setEnabled(False)

            self.button_import.clicked.connect(self.get_text_file)
            self.button_save.clicked.connect(self.save_feature)
            self.button_delete.clicked.connect(self.delete_selected)

            # self.button_generate.clicked.connect(self.generate_dependencies)
            self.document = None
            self.casual_relationship = None
            self.casual_dependency = None
            self.json_model = None
            self.json_tree_view = None
            self.data = None
            self.removed_list = []
            self.removed_index_list = []
            self.model = None

            self.buttons_HBOX = QHBoxLayout()
            self.buttons_HBOX.addWidget(self.button_import)
            self.buttons_HBOX.addWidget(self.button_save)
            self.buttons_HBOX.addWidget(self.button_delta_time)
            # self.buttons_HBOX.addWidget(self.button_undo)
            self.buttons_HBOX.addWidget(self.button_generate)
            self.buttons_HBOX.setAlignment(Qt.AlignTop)

            self.search_label = QLabel('Search bar: ')
            self.search_field = QLineEdit()
            self.search_field.setEnabled(False)
            self.search_field.setMaximumWidth(300)
            self.buttons_HBOX.addWidget(self.search_label)
            self.buttons_HBOX.addWidget(self.search_field)
            self.buttons_HBOX.addStretch()

            self.relationships_VBOX = QVBoxLayout()
            self.relationships_VBOX.setAlignment(Qt.AlignTop)
            
            
            self.table = TableView()
            self.table.setStyleSheet('subcontrol-position: left')
            self.table.verticalHeader().setSectionResizeMode(QHeaderView.Interactive)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

            self.relationships_VBOX.addWidget(QLabel("Relationships"))
            self.relationships_VBOX.addWidget(self.table)
            under_table_HBOX = QHBoxLayout()
            under_table_HBOX.addWidget(self.button_delete)
            # under_table_HBOX.addWidget(self.button_undo_deleted_rows)
            under_table_HBOX.addStretch()

            self.relationships_VBOX.addLayout(under_table_HBOX)


            self.main_content_VBOX = QVBoxLayout()
            self.main_content_VBOX.setAlignment(Qt.AlignTop)
            self.main_content_VBOX.addLayout(self.buttons_HBOX)
            self.main_content_VBOX.addLayout(self.relationships_VBOX)
            self.setLayout(self.main_content_VBOX)
            

        except Exception:
            traceback.print_exc()

    # def generate_dependencies(self):
    #     try:
    #         skip: list = CasualRelationship.deleted
    #         for s in skip:
    #             self.document[s] = False
    #         for i in range(len(self.document)):
    #             self.data = self.document[i]
    #             if self.data:
    #                 self.json_model = QJsonModel()
    #                 self.json_tree_view = QTreeView()
    #                 # self.json_tree_view.setModel(self.json_model)
    #                 self.json_model.load(self.data)
    #                 self.casual_dependency = CasualRelationship(self.json_tree_view, i, False)
    #                 self.vbox_scroll_right.addWidget(self.casual_dependency)
    #         self.widget_scroll_right.setLayout(self.vbox_scroll_right)
    #         self.scroll_area_right.setWidget(self.widget_scroll_right)
    #         self.dependencies_VBOX.addWidget(self.scroll_area_right)
    #     except Exception:
    #         traceback.print_exc()


    def undo_delete(self):

        for index in self.removed_list:
            print(index)


    def delete_selected(self):
        self.removed_list = self.table.selectionModel().selectedRows()

        for model_index in self.table.selectionModel().selectedRows():
            index = QPersistentModelIndex(model_index)
            self.removed_index_list.append(index)

        for index in self.removed_index_list:
            self.model.removeRow(index.row())



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
                    # self.better_relationships(self.document)
                try:

                    # Adding the search feature
                    self.search_feature()
                    self.search_field.setEnabled(True)
                    self.button_delta_time.setEnabled(True)
                    self.button_save.setEnabled(True)
                    self.button_generate.setEnabled(True)
                    self.button_delete.setEnabled(True)
                    self.table.setModel(self.filter_proxy_model)



                    self.button_generate.setEnabled(True)

                except Exception:
                    traceback.print_exc()

            else:
                pass

    def better_relationships(self, json_data):
        try:
            for element in json_data:
                element_rel = []
                relationships = element["Artifact_Relationships"]
                for i in range(len(relationships)):
                    rel = relationships[i]
                    if isinstance(rel, int):
                        r = json_data[rel]
                        element_rel.append(r)
                element["Artifact_Relationships"] = element_rel

        except Exception:
            traceback.print_exc()

    def textchanged(self, text):
        print("contents of text box: " + text)

    def search_feature(self):

        # Gathering all keys from dictionary in a list
        keys = []
        for i in range(len(self.document)):
            for key in self.document[i].keys():
                if key not in keys:
                    keys.append(key)

        # 2D array that stores all values of the json artifacts
        self.json_array = []
        

        # Inserting values into 2D array
        for i in range(len(self.document)):
            self.json_array.append([])
            for j, key in enumerate(keys):
                if key in self.document[i]:
                    if key == "start":
                        time : str = self.document[i][key]
                        time = time.split(" ")
                        time = time[1]
                        self.document[i][key] = time

                    self.json_array[i].append(str(self.document[i][key]))
                else:
                    self.json_array[i].append('')

        # Creating the standard model for filtering
        self.model = QStandardItemModel(len(self.json_array), len(self.json_array[0]))
        self.model.setHorizontalHeaderLabels(keys)

        # Inserting every item of the 2D array into the model an an Item object
        for row in range(len(self.json_array)):
            for col in range(len(self.json_array[row])):
                item = QStandardItem(self.json_array[row][col])
                self.model.setItem(row, col, item)
                  

        # Setting the Filter Proxy model for filtering data
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(-1)

        # Adding the Search bar feature in the Layout
        self.search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def save_feature(self):
            #Gathering all keys from dictionary in a list
            self.keys = []
            for i in range (len(self.document)):
                for key in self.document[i].keys():
                    if key not in keys:
                        self.keys.append(key)
            
            saving_array = []
            for row in range (len(self.json_array)):
                saving_array.append([])
                for col in range (len(self.json_array[row])):
                    saving_array[row].append(self.model.item(row,col).text())
            
            
            final_list = []
            for row in range (len(saving_array)):
                dic = {}
                final_list.append(dic)
                for col,key in enumerate(keys):
                    final_list[row][key] = saving_array[row][col]
            
            #print(final_list[0]['y'])
            with open('~/Documents/relationships_saved.json', 'w') as json_file:
                json_format = json.dump(final_list, json_file)


class TableView(QTableView):
    def __init__(self,parent=None):
        super(TableView, self).__init__(parent)

        self.parent = parent
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setSelectionBehavior(self.SelectRows)  #Select whole rows
        self.setAlternatingRowColors(True)
        self.setDropIndicatorShown(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(self.InternalMove)
        # self.setMaximumHeight(900)



# class TrashList(QTableWidget):
#     def __init__(self,parent):
#         super(TrashList, self).__init__(parent)
#         self.setDragEnabled(True)
#         self.setAcceptDrops(True)
#         # self.setDragDropMode(self.DragDrop)
#         self.setSelectionBehavior(self.SelectRows)  #Select whole rows
#         # self.setSelectionMode(self.SingleSelection) # Only select/drag one row each time
#         self.setDragDropOverwriteMode(False)        # Removes the original item after moving instead of clearing it

