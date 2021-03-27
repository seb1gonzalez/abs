import logging
import json
import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDoubleSpinBox, QListWidget, QPushButton, QStyle

from Causal_Extractor.RelationshipExtractor import RelationshipExtractor
from Dialogs.DirectoryDialog import DirectoryDialog
from MessageBoxs.FileListMsgBox import FileListMsgBox

class ConfMng(QWidget):
    def __init__(self,parent):
        logging.debug("ConfMng(): Instantiated")
        super(ConfMng, self).__init__(parent)
        mainlayout = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QHBoxLayout()

        self.files = []
        self.extract_json_data()

        agent_name_label = QLabel("Name of Agent: ")
        agent_name_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        agent_name_label.setAlignment(Qt.AlignLeft)

        self.agent_name_le = QLineEdit(self.data['Agent Name'])
        self.agent_name_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.agent_name_le.setAlignment(Qt.AlignLeft)

        time_label = QLabel("Time Delta (sec.): ")
        time_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        time_label.setAlignment(Qt.AlignLeft)

        self.timesp = QDoubleSpinBox()
        self.timesp.setMinimumWidth(200)
        self.timesp.setAlignment(Qt.AlignLeft)
        self.timesp.setMaximum(31540000) # Seconds in a year
        self.timesp.setValue(self.data['Time Range'])

        directory_json_label = QLabel("Folder Containing JSON files: ")
        directory_json_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        directory_json_label.setAlignment(Qt.AlignLeft)

        self.directory_json_le = QLineEdit(self.data['Data Folder'])
        self.directory_json_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.directory_json_le.setAlignment(Qt.AlignLeft)

        directory_butt = QPushButton()
        directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        directory_butt.clicked.connect(self.directory_chooser)

        file_label = QLabel("Files to be Analyzed:")

        self.file_list = QListWidget()
        self.create_file_list()

        overwrite_butt = QPushButton("Overwrite Config File")
        overwrite_butt.clicked.connect(self.overwrite_config_file)

        extract_butt = QPushButton("Start Relationship Extraction")
        extract_butt.clicked.connect(self.relationship_extraction)

        layout1.addWidget(agent_name_label)
        layout1.addWidget(self.agent_name_le)

        layout2.addWidget(time_label)
        layout2.addWidget(self.timesp)
        layout2.addStretch()

        layout3.addWidget(directory_json_label)
        layout3.addWidget(self.directory_json_le)
        layout3.addWidget(directory_butt)

        layout4.addWidget(file_label)
        layout4.addWidget(self.file_list)

        layout5.addWidget(overwrite_butt)
        layout5.addWidget(extract_butt)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addLayout(layout3)
        mainlayout.addStretch()
        mainlayout.addLayout(layout4)
        mainlayout.addStretch()
        mainlayout.addLayout(layout5)
        mainlayout.addStretch()
        logging.debug("ConfMng(): Complete")
        

    def extract_json_data(self):
        logging.debug("extract_json_data(): Instantiated")
        json_file = open(os.getcwd() + '/../Config/Config.JSON')
        self.data = json.load(json_file)
        logging.debug(self.data)
        logging.debug(self.data)
        json_file.close()
        logging.debug("extract_json_data(): Complete")

    def directory_chooser(self):
        logging.debug("folder_chooser(): Instantiated")
        dir_chosen = DirectoryDialog().directory_dialog()
        self.directory_json_le.setText(dir_chosen)
        self.update_list(dir_chosen)
        logging.debug("folder_chooser(): Complete")

    def update_list(self, dir_chosen):
        logging.debug("update_list(): Instantiated")
        self.data['Data Folder'] = dir_chosen
        self.files = self.find_data_files()
        self.update_file_list(self.files)
        logging.debug("update_list(): Complete")

    def update_file_list(self, files):
        logging.debug("create_file_list(): Instantiated")
        self.file_list.clear()
        index = 0
        while index < len(files):
            self.file_list.insertItem(index, files[index])
            index += 1
        self.file_list.clicked.connect(self.list_item_clicked)
        logging.debug("create_file_list(): Complete")

    def create_file_list(self):
        logging.debug("create_file_list(): Instantiated")
        self.files = self.find_data_files()
        index = 0
        while index < len(self.files):
            self.file_list.insertItem(index, self.files[index])
            index += 1
        self.file_list.clicked.connect(self.list_item_clicked)
        logging.debug("create_file_list(): Complete")

    def find_data_files(self):
        logging.debug("find_data_files(): Instantiated")
        ret_list = []
        for root, dirs, files in os.walk(self.data['Data Folder']):
            for file in files:
                if file.endswith(".JSON") or file.endswith(".json"):
                    ret_list.append(os.path.abspath(os.path.join(root, file)))  # Causes warning, but doesn't affect performance
        logging.debug(ret_list)
        return ret_list
        logging.debug("find_data_files(): Complete")

    def list_item_clicked(self, item):
        logging.debug("list_item_clicked(): Instantiated")
        FileListMsgBox().create_msg_box(item.data())
        logging.debug("list_item_clicked(): Complete")

    def overwrite_config_file(self):
        logging.debug("overwrite_config_file(): Instantiated")
        self.data['Agent Name'] = self.agent_name_le.text()
        self.data['Time Range'] = self.timesp.value()
        self.data['Data Folder'] = self.directory_json_le.text()
        with open(os.getcwd() + '/../Config/Config.JSON', 'w') as outfile:
            json.dump(self.data, outfile, ensure_ascii=False, indent=4)
        logging.debug("overwrite_config_file(): Complete")

    def relationship_extraction(self):
        logging.debug("relationship_extraction(): Instantiated")
        RelationshipExtractor().extract_relationships(self.files, (str(self.timesp.value())).split('.'))
        logging.debug("relationship_extraction(): Complete")

""" if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("main(): Instantiated")
    logging.basicConfig(format='%(levelname)s:%(message)s')
    app = QApplication(sys.argv)
    ConfMngApp = ConfMng()
    ConfMngApp.setGeometry(700, 450, 350, 300)
    ConfMngApp.show()
    app.exec_()
    logging.debug("main(): Complete") """
