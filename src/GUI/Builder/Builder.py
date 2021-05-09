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

        """POP UPS"""
        self.error_pop = self.popup("Error")
        self.error_pop.setIcon(QMessageBox.Critical)
        self.save_pop = self.popup("Artifacts Saved")
        self.export_pop = self.popup("Artifacts Exported")
        self.custom_artifact_popup = self.popup("Custom Artifact Added")

        """ BUTTONS """
        self.button_import = QPushButton("Import")
        self.button_import.setMaximumWidth(80)
        self.button_save = QPushButton("Save")
        self.button_save.setMaximumWidth(80)
        self.button_customArtifact = QPushButton("Custom Artifact")
        self.button_customArtifact.setMaximumWidth(150)

        self.button_export = QPushButton("Export Script")
        self.button_delete = QPushButton("Delete Selected")
        self.button_delete.setStyleSheet("background-color:#ff1744; color:white")

        self.button_save.setEnabled(False)
        self.button_export.setEnabled(False)
        self.button_delete.setEnabled(False)
        self.button_customArtifact.setEnabled(False)

        self.button_import.clicked.connect(self.get_text_file)
        self.button_save.clicked.connect(self.save_feature)
        self.button_delete.clicked.connect(self.delete_selected)
        self.button_export.clicked.connect(self.export)
        self.button_customArtifact.clicked.connect(self.customArtifact)

        """BUILDER GLOBALS"""
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


        # Dictionaries to store UNIQUE data items
        self.artifactCommands = {} # wget , mkdir, echo ,etc.
        self.artifactTypes = {} # auditd , KeyPress, imgPoint, etc
        self.actionsCombo = None
        self.commandsCombo = None
        self.userArtifact = None
        self.custom_contentQlineEdit = None
        self.custom_classnameQlineEdit = None
        self.customArtifactColor = "black"

        """LAYOUTS"""
        self.buttons_HBOX = QHBoxLayout()
        self.buttons_HBOX.addWidget(self.button_import)
        self.buttons_HBOX.addWidget(self.button_save)
        self.buttons_HBOX.addWidget(self.button_export)
        self.buttons_HBOX.addWidget(self.button_customArtifact)
        self.buttons_HBOX.setAlignment(Qt.AlignTop)

        self.search_label = QLabel('Search bar: ')
        self.search_field = QLineEdit()
        self.search_field.setEnabled(False)
        self.search_field.setMaximumWidth(300)
        self.buttons_HBOX.addWidget(self.search_label)
        self.buttons_HBOX.addWidget(self.search_field)
        self.buttons_HBOX.addStretch()

        self.artifacts_VBOX = QVBoxLayout()
        self.artifacts_VBOX.setAlignment(Qt.AlignTop)

        self.table = TableView()
        self.table.setStyleSheet('subcontrol-position: left')
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        self.artifacts_VBOX.addWidget(QLabel("Relationships"))
        self.artifacts_VBOX.addWidget(self.table)
        self.under_table_HBOX = QHBoxLayout()
        self.under_table_HBOX.addWidget(self.button_delete)
        self.under_table_HBOX.addStretch()
        self.artifacts_VBOX.addLayout(self.under_table_HBOX)

        self.main_content_VBOX = QVBoxLayout()
        self.main_content_VBOX.setAlignment(Qt.AlignTop)
        self.main_content_VBOX.addLayout(self.buttons_HBOX)
        self.main_content_VBOX.addLayout(self.artifacts_VBOX)

        """MAIN LAYOUT"""
        self.setLayout(self.main_content_VBOX)

    def delete_selected(self):
        """
        Deletes selected rows from table
        """
        try:
            self.removed_list = self.table.selectionModel().selectedRows()
            for model_index in self.table.selectionModel().selectedRows():
                index = QPersistentModelIndex(model_index)
                self.removed_index_list.append(index)
            for index in self.removed_index_list:
                self.model.removeRow(index.row())

        except Exception as e:
            self.error_pop.setDetailedText(str(e))
            show = self.error_pop.exec_()

    def get_text_file(self):
        '''Reads JSON from Extractor, generates local attributes for table'''
        try:
            # Get file
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

            # Get column keys and populate artifact items
            self.keys = []
            for artifact in self.document:
                for key in artifact:
                    if key == "className":
                        self.artifactTypes[artifact[key]] = artifact[key]

                        if artifact[key] == "auditd":
                            command = artifact["content"].split(" ")[0]
                            self.artifactCommands[command] = command

                    if key not in self.keys:
                        self.keys.append(key)

            # 2D array that stores all values of the json artifacts
            self.json_array = []

            # Inserting values into 2D array
            for i in range(len(self.document)):
                self.json_array.append([])
                for j, key in enumerate(self.keys):
                    if key in self.document[i]:
                        if key == "start" and self.document[i][key] != "":
                            time: str = self.document[i][key]
                            time = time.split(" ")
                            if len(time) > 1:
                                time = time[1]
                                self.document[i][key] = time
                        self.json_array[i].append(str(self.document[i][key]))
                    else:
                        self.json_array[i].append("")

            # Creating the standard model for filtering
            self.model : QStandardItemModel = QStandardItemModel(len(self.json_array), len(self.json_array[0]))
            self.model.setHorizontalHeaderLabels(self.keys)

            # Inserting every item of the 2D array into the model an an Item object
            for row in range(len(self.json_array)):
                for col in range(len(self.json_array[row])):
                    item = QStandardItem(self.json_array[row][col])
                    item.setToolTip(self.json_array[row][col])
                    self.model.setItem(row, col, item)


            # Adding the search feature
            self.search_feature()
            self.table.setModel(self.filter_proxy_model)

            # Enable buttons
            self.search_field.setEnabled(True)
            self.button_save.setEnabled(True)
            self.button_export.setEnabled(True)
            self.button_delete.setEnabled(True)
            self.button_export.setEnabled(True)
            self.button_customArtifact.setEnabled(True)

        except Exception as e:
            self.error_pop.setDetailedText(str(e))
            show = self.error_pop.exec_()
            traceback.print_exc()

    def search_feature(self) :
        ''' Adds search proxy to model '''
        # Setting the Filter Proxy model for filtering data
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(-1)

        # Adding the Search bar feature in the Layout
        self.search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def save_feature(self) :
        '''Grabs current model, creates object to be saved as JSON '''
        saving_array = []
        skip_empty = {}
        try:
            for row in range(len(self.json_array)):
                saving_array.append([])
                for col in range(len(self.json_array[row])):
                    if self.model.item(row, col):
                        saving_array[row].append(self.model.item(row, col).text())
                        skip_empty[row] = False
                    else:
                        skip_empty[row] = True

            final_list = []
            for row in range(len(saving_array)):
                if skip_empty[row]:
                    break
                dic = {}
                final_list.append(dic)
                for col, key in enumerate(self.keys):
                    # if artifact id is empty, do not write this element
                    row_data = saving_array[row]
                    if col < len(row_data):
                        data = row_data[col]
                        final_list[row][key] = data
            # print(final_list[0]['y'])
            with open('Builder/builder_saved/relationships_saved.json', 'w') as json_file:
                json.dump(final_list, json_file, indent=4)
            show = self.save_pop.exec_()
        except Exception as e:
            self.error_pop.setDetailedText(str(e))
            show = self.error_pop.exec_()

    def export(self) :
        ''' Grabs current model, extracts keys needed for runner component, saves as JSON '''
        export = []
        skip_empty = {}
        try:
            for row in range(len(self.json_array)):
                export.append([])
                for col in range(len(self.json_array[row])):
                    if self.model.item(row, col):
                        export[row].append(self.model.item(row, col).text())
                        skip_empty[row] = False
                    else:
                        skip_empty[row] = True

            final_list = []
            for row in range(len(export)):
                if skip_empty[row]:
                    break
                dic = {}
                final_list.append(dic)
                for col, key in enumerate(self.keys):
                    if key in ["Artifact_id", "content", "className", "start"]:
                        final_list[row][key] = export[row][col]

            # print(final_list[0]['y'])
            with open('Builder/builder_out/builder_script.json', 'w') as json_file:
                json.dump(final_list, json_file, indent=4)

            show = self.export_pop.exec_()
        except Exception as e:
            self.error_pop.setDetailedText(str(e))
            show = self.error_pop.exec_()

    def undo_last(self):
        self.model.undo_item()

    def popup(self,message) -> QMessageBox:
        ''' Creates pop up window with custom message'''
        qmessage = QMessageBox()
        qmessage.setWindowTitle("ABS")
        qmessage.setText(message)
        qmessage.setIcon(QMessageBox.Information)
        return qmessage

    def customArtifact(self):
        try:
            self.userArtifact = QWidget()
            self.userArtifact.setMinimumWidth(500)
            self.userArtifact.setMinimumHeight(200)
            self.userArtifact.setWindowTitle("Custom Artifact")

            # Prepare Layout
            vbox = QVBoxLayout()
            vbox.setAlignment(Qt.AlignLeft)
            hboxTop= QHBoxLayout()
            hboxTop.setAlignment(Qt.AlignLeft)
            vboxCustom= QVBoxLayout()
            vboxCustom.setAlignment(Qt.AlignLeft)
            hboxButtons = QHBoxLayout()
            hboxButtons.setAlignment(Qt.AlignRight)

            # ---------------------------------------
            action_items = ["None"]
            for key in self.artifactTypes:
                action_items.append(key)
            self.actionsCombo = QComboBox()
            action_label = QLabel("Select classname")
            hboxTop.addWidget(action_label, alignment=Qt.AlignTop)
            self.addComboBoxToLayout(self.actionsCombo, action_items, hLayout=hboxTop)
            self.actionsCombo.currentIndexChanged.connect(self.action_selection_change)
            # -------------------------
            command_items = ["None"]
            for key in self.artifactCommands:
                command_items.append(key)
            self.commandsCombo = QComboBox()
            commands_label = QLabel("Select content")
            hboxTop.addWidget(commands_label, alignment=Qt.AlignTop)
            self.addComboBoxToLayout(self.commandsCombo,command_items,hLayout=hboxTop)
            self.commandsCombo.currentIndexChanged.connect(self.content_selection_change)
            # -------------------------
            custom_content_label = QLabel("Custom Content: ")
            custom_classname_label = QLabel("Custom Classname: ")
            self.custom_contentQlineEdit : QLineEdit = QLineEdit()
            self.custom_classnameQlineEdit : QLineEdit = QLineEdit()
            self.custom_contentQlineEdit.setMinimumWidth(300)
            self.custom_classnameQlineEdit.setMinimumWidth(300)

            button_add_custom_artifact = QPushButton("Add Artifact")
            button_add_custom_artifact.setMaximumWidth(150)
            button_add_custom_artifact.setStyleSheet("background-color:#43a047;color:white")
            button_add_custom_artifact.clicked.connect(self.addCustomArtifact)

            button_add_custom_color_artifact = QPushButton("Artifact Color")
            button_add_custom_color_artifact.setMaximumWidth(150)
            button_add_custom_color_artifact.clicked.connect(self.setArtifactColor)

            vboxCustom.addWidget(custom_classname_label,alignment=Qt.AlignTop)
            vboxCustom.addWidget(self.custom_classnameQlineEdit, alignment=Qt.AlignTop)

            vboxCustom.addWidget(custom_content_label,alignment=Qt.AlignTop)
            vboxCustom.addWidget(self.custom_contentQlineEdit, alignment=Qt.AlignTop)

            hboxButtons.addWidget(button_add_custom_color_artifact)
            hboxButtons.addStretch()
            hboxButtons.addWidget(button_add_custom_artifact)

            # -----------------------------
            vbox.addLayout(hboxTop)
            vbox.addLayout(vboxCustom)
            vbox.addLayout(hboxButtons)
            vbox.addStretch()
            self.userArtifact.setLayout(vbox)
            self.userArtifact.show()

        except Exception as e:
            self.error_pop.setDetailedText(str(e))
            show = self.error_pop.exec_()
            traceback.print_exc()

    def setArtifactColor(self):
        self.customArtifactColor:QColor = QColorDialog.getColor()
        self.custom_contentQlineEdit.setStyleSheet("color:"+self.customArtifactColor.name())
        self.custom_classnameQlineEdit.setStyleSheet("color:" + self.customArtifactColor.name())

    def action_selection_change(self):
        self.custom_classnameQlineEdit.setText(self.actionsCombo.currentText())

    def content_selection_change(self):
        self.custom_contentQlineEdit.setText(self.commandsCombo.currentText())

    def addComboBoxToLayout(self,combo:QComboBox,combo_items:list,vLayout:QVBoxLayout = None, hLayout:QHBoxLayout = None):
        if vLayout:
            combo.addItems(combo_items)
            vLayout.addWidget(combo,alignment=Qt.AlignTop)
            vLayout.addSpacing(10)
        elif hLayout:
            combo.addItems(combo_items)
            hLayout.addWidget(combo,alignment=Qt.AlignTop)
            hLayout.addSpacing(10)

    def addCustomArtifact(self):
        try:
            newContent = self.custom_contentQlineEdit.text()
            newClassname = self.custom_classnameQlineEdit.text()
            self.model.insertRow(self.model.rowCount())
            for col in range(self.model.columnCount()):
                if self.keys[col] == "content":
                    item = QStandardItem(newContent)
                    item.setForeground(self.customArtifactColor)
                    self.model.setItem(self.model.rowCount()-1, col, item)
                if self.keys[col] == "className":
                    item = QStandardItem(newClassname)
                    item.setForeground(self.customArtifactColor)
                    self.model.setItem(self.model.rowCount()-1, col, item)
                if self.keys[col] == "Artifact_id":
                    item = QStandardItem(str(self.model.rowCount()-1))
                    item.setForeground(self.customArtifactColor)
                    self.model.setItem(self.model.rowCount()-1, col, item)
                if self.keys[col] == "start":
                    item = QStandardItem("00:00:00.0000")
                    item.setForeground(self.customArtifactColor)
                    self.model.setItem(self.model.rowCount()-1, col, item)
            self.model.layoutChanged.emit()
            show = self.custom_artifact_popup.exec_()
        except Exception as e:
            self.error_pop.setDetailedText(str(e))
            show = self.error_pop.exec_()
            traceback.print_exc()

# Undo - not integrated - crashes software
class MyModel(QStandardItemModel):
    def __init__(self, list_data, parent=None):
        super(MyModel, self).__init__()
        self.list_data = None

        # self.model.dataChanged.connect(self.model.setData())
        self.stack = QUndoStack()
        # print(self.model.dataChanged.item.index.row())

    def setListData(self, listData):
        self.list_data = listData

    def isStackEmpty(self):
        return self.stack.count()

    def undo_item(self):
        self.stack.undo()

    def rowCount(self, parent):
        return len(self.list_data)

    def columnCount(self, parent):
        return len(self.list_data[0])

    def data(self, index, role):

        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.list_data[row][column]
            return value

        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            value = self.list_data[row][column]
            return value

    def setData(self, index, value, role=Qt.EditRole):

        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self.stack.push(CellEdit(index, value, self))
            self.list_data[row][column] = value
            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable

# Undo
class CellEdit(QUndoCommand):

    def __init__(self, index, value, model):
        super().__init__()
        self.index = index
        self.value = value
        self.prev = model.list_data[index.row()][index.column()]
        self.model = model

    def undo(self):
        self.model.list_data[self.index.row()][self.index.column()] = self.prev

    def redo(self):
        self.model.list_data[self.index.row()][self.index.column()] = self.value


class TableView(QTableView):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.parent = parent
        self.setDragEnabled(True)
        self.setSelectionBehavior(self.SelectRows)  # Select whole rows
        self.setAlternatingRowColors(True)
        self.setDropIndicatorShown(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(self.InternalMove)



