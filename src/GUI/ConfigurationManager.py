import logging
import json
import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QListWidget, QPushButton

from MessageBoxs.FileListMsgBox import FileListMsgBox

class ConfMng(QWidget):
    def __init__(self,parent):
        logging.debug("ConfMng(): Instantiated")
        super(ConfMng, self).__init__(parent)
        # self.setWindowTitle("Agent Build System: Configuration Manager")
        # mainwidget = QWidget()
        #self.addWidget(mainwidget)
        mainlayout = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QHBoxLayout()

        self.extract_json_data()

        agent_name_label = QLabel("Name of Agent: " + self.data['Agent Name'])
        agent_name_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        agent_name_label.setAlignment(Qt.AlignLeft)

        time_label = QLabel("Time Range:")
        time_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        time_label.setAlignment(Qt.AlignLeft)

        self.timesp = QSpinBox()
        self.timesp.setAlignment(Qt.AlignRight)
        self.timesp.setMaximum(31540000) # Seconds in a year
        self.timesp.setValue(self.data['Time Range'])

        file_label = QLabel("Files to be Analyzed:")

        self.file_list = QListWidget()
        self.create_file_list()

        continue_butt = QPushButton("Continue")

        layout1.addWidget(agent_name_label)

        layout2.addWidget(time_label)
        layout2.addWidget(self.timesp)

        layout3.addWidget(file_label)
        layout3.addWidget(self.file_list)

        layout4.addStretch()
        layout4.addWidget(continue_butt)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addLayout(layout3)
        mainlayout.addStretch()
        mainlayout.addLayout(layout4)
        mainlayout.addStretch()
        #mainwidget.setLayout(mainlayout)
        logging.debug("ConfMng(): Complete")
        

    def extract_json_data(self):
        logging.debug("extract_json_data(): Instantiated")
        json_file = open(os.getcwd() + '/Config/Config.json')
        self.data = json.load(json_file)
        logging.debug(self.data)
        json_file.close()
        logging.debug("extract_json_data(): Complete")

    def create_file_list(self):
        logging.debug("create_file_list(): Instantiated")
        files = self.find_data_files()
        index = 0
        while index < len(files):
            self.file_list.insertItem(index, files[index])
            index += 1
        self.file_list.clicked.connect(self.list_item_clicked)
        logging.debug("create_file_list(): Complete")

    def find_data_files(self):
        logging.debug("find_data_files(): Instantiated")
        ret_list = []
        for root, dirs, files in os.walk(self.data['Data Folder']):
            for file in files:
                if file.endswith(".JSON") or file.endswith(".json"):
                    ret_list.append(file)
        logging.debug(ret_list)
        return ret_list
        logging.debug("find_data_files(): Complete")

    def list_item_clicked(self, item):
        logging.debug("list_item_clicked(): Instantiated")
        FileListMsgBox().create_msg_box(item.data())
        logging.debug("list_item_clicked(): Complete")

# if __name__ == '__main__':
#     logging.getLogger().setLevel(logging.DEBUG)
#     logging.debug("main(): Instantiated")
#     logging.basicConfig(format='%(levelname)s:%(message)s')
#     app = QApplication(sys.argv)
#     ConfMngApp = ConfMng()
#     ConfMngApp.setGeometry(700, 450, 350, 300)
#     ConfMngApp.show()
#     app.exec_()
#     logging.debug("main(): Complete")
