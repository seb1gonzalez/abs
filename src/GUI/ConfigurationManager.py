import logging
import json
import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDoubleSpinBox, QListWidget, QPushButton, QStyle, QFrame

#from Causal_Extractor.RelationshipExtractor import RelationshipExtractor
from Dialogs.DirectoryDialog import DirectoryDialog
from Dialogs.ResultsDialog import ResultsDlg
from MessageBoxs.FileListMsgBox import FileListMsgBox
from MessageBoxs.OverwriteMsgBox import OverwriteMsgBox

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

        self.agent_name_def = ""
        self.time_def = 0.00
        self.directory_file_def = ""
        self.files = []
        self.extract_json_data()

        agent_name_label = QLabel("Name of Agent: ")
        agent_name_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        agent_name_label.setAlignment(Qt.AlignCenter)

        self.agent_name_le = QLineEdit(self.data['Agent Name'])
        self.agent_name_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.agent_name_le.setAlignment(Qt.AlignLeft)
        self.agent_name_le.textChanged.connect(self.update_agent_name_butt)

        self.agent_name_butt = QPushButton("Reset")
        self.agent_name_butt.clicked.connect(self.agent_name_reset)
        self.agent_name_butt.setEnabled(False)

        time_label = QLabel("Time Delta (sec.): ")
        time_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        time_label.setAlignment(Qt.AlignCenter)

        self.timesp = QDoubleSpinBox()
        self.timesp.setMinimumWidth(200)
        self.timesp.setAlignment(Qt.AlignLeft)
        self.timesp.setMaximum(31540000) # Seconds in a year
        self.timesp.setValue(self.data['Time Range'])
        self.timesp.valueChanged.connect(self.update_timesp_butt)

        self.timesp_butt = QPushButton("Reset")
        self.timesp_butt.clicked.connect(self.timesp_reset)
        self.timesp_butt.setEnabled(False)

        directory_json_label = QLabel("Folder Containing JSON files: ")
        directory_json_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        directory_json_label.setAlignment(Qt.AlignCenter)

        self.directory_json_le = QLineEdit(self.data['Data Folder'])
        self.directory_json_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.directory_json_le.setAlignment(Qt.AlignLeft)
        self.directory_json_le.textChanged.connect(self.update_directory_butt)

        directory_butt = QPushButton()
        directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        directory_butt.clicked.connect(self.directory_chooser)

        self.directory_reset_butt = QPushButton("Reset")
        self.directory_reset_butt.clicked.connect(self.directory_reset)
        self.directory_reset_butt.setEnabled(False)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedHeight(10)
        separator.setLineWidth(3)

        file_label = QLabel("Files to be Analyzed:")

        self.file_list = QListWidget()
        self.create_file_list()

        self.overwrite_butt = QPushButton("Overwrite Config File")
        self.overwrite_butt.clicked.connect(self.overwrite_config_file)
        self.overwrite_butt.setEnabled(False)

        self.extract_butt = QPushButton("Start Relationship Extraction")
        self.extract_butt.clicked.connect(self.relationship_extraction)

        layout1.addWidget(agent_name_label)
        layout1.addWidget(self.agent_name_le)
        layout1.addWidget(self.agent_name_butt)

        layout2.addWidget(time_label)
        layout2.addWidget(self.timesp)
        layout2.addStretch()
        layout2.addWidget(self.timesp_butt)

        layout3.addWidget(directory_json_label)
        layout3.addWidget(self.directory_json_le)
        layout3.addWidget(directory_butt)
        layout3.addWidget(self.directory_reset_butt)

        layout4.addWidget(file_label)
        layout4.addWidget(self.file_list)

        layout5.addWidget(self.overwrite_butt)
        layout5.addWidget(self.extract_butt)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addLayout(layout3)
        mainlayout.addStretch()
        mainlayout.addWidget(separator)
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
        self.agent_name_def = self.data['Agent Name']
        self.time_def = self.data['Time Range']
        self.directory_file_def = self.data['Data Folder']
        logging.debug(self.data)
        json_file.close()
        logging.debug("extract_json_data(): Complete")

    def update_agent_name_butt(self):
        logging.debug("update_agent_name_butt(): Instantiated")
        self.agent_name_butt.setEnabled(True)
        self.update_overwrite_butt()
        logging.debug("update_agent_name_butt(): Complete")

    def agent_name_reset(self):
        logging.debug("agent_name_reset(): Instantiated")
        self.agent_name_le.setText(self.agent_name_def)
        self.agent_name_butt.setEnabled(False)
        self.update_overwrite_butt()
        logging.debug("agent_name_reset(): Complete")

    def update_timesp_butt(self):
        logging.debug("update_timesp_butt(): Instantiated")
        self.timesp_butt.setEnabled(True)
        self.update_overwrite_butt()
        logging.debug("update_timesp_butt(): Complete")

    def timesp_reset(self):
        logging.debug("timesp_reset(): Instantiated")
        self.timesp.setValue(self.time_def)
        self.timesp_butt.setEnabled(False)
        self.update_overwrite_butt()
        logging.debug("timesp_reset(): Complete")

    def update_directory_butt(self):
        logging.debug("update_directory_butt(): Instantiated")
        self.directory_reset_butt.setEnabled(True)
        self.update_overwrite_butt()
        logging.debug("update_directory_butt(): Complete")

    def directory_reset(self):
        logging.debug("directory_reset(): Instantiated")
        self.directory_json_le.setText(self.directory_file_def)
        self.directory_reset_butt.setEnabled(False)
        self.update_list(self.directory_json_le.text())
        self.update_overwrite_butt()
        logging.debug("directory_reset(): Complete")

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

    def update_overwrite_butt(self):
        logging.debug("update_overwrite_butt(): Instantiated")
        if self.agent_name_butt.isEnabled() or self.timesp_butt.isEnabled() or self.directory_reset_butt.isEnabled():
            self.overwrite_butt.setEnabled(True)
            self.extract_butt.setEnabled(False)
        else:
            self.overwrite_butt.setEnabled(False)
            self.extract_butt.setEnabled(True)
        logging.debug("update_overwrite_butt(): Complete")

    def overwrite_config_file(self):
        logging.debug("overwrite_config_file(): Instantiated")
        self.data['Agent Name'] = self.agent_name_le.text()
        self.data['Time Range'] = self.timesp.value()
        self.data['Data Folder'] = self.directory_json_le.text()
        try:
            with open(os.getcwd() + '/../Config/Config.JSON', 'w') as outfile:
                json.dump(self.data, outfile, ensure_ascii=False, indent=4)
            OverwriteMsgBox().create_msg_box(self.data, 1)
            self.agent_name_def = self.agent_name_le.text()
            self.time_def = self.timesp.value()
            self.directory_file_def = self.directory_json_le.text()
            self.agent_name_butt.setEnabled(False)
            self.timesp_butt.setEnabled(False)
            self.directory_reset_butt.setEnabled(False)
            self.overwrite_butt.setEnabled(False)
            self.extract_butt.setEnabled(True)
        except:
            OverwriteMsgBox().create_msg_box(self.data, 0)
        logging.debug("overwrite_config_file(): Complete")

    def relationship_extraction(self):
        logging.debug("relationship_extraction(): Instantiated")
        self.results_w = ResultsDlg()
        self.results_w.start_extraction(self.files, (str(self.timesp.value())).split('.'))
        self.results_w.show()
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
