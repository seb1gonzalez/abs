import logging
import platform

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStyle, QFrame, QProgressBar

#from JSONFileDialog import JSONFileDialog
from JFileDialog import JFileDialog
from ImportHandler import ImportThread

class ImportManager(QWidget):
    def __init__(self, parent):
        logging.debug("ImportManager(): Instantiated")
        super(ImportManager, self).__init__(parent)
        mainlayout = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        import_zip_label = QLabel("Select ZIP file to import: ")
        import_zip_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        import_zip_label.setAlignment(Qt.AlignCenter)

        self.zip_le = QLineEdit()
        self.zip_le.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        self.zip_le.setAlignment(Qt.AlignLeft)
        self.zip_le.textChanged.connect(self.enable_zip_clear)

        zip_directory_butt = QPushButton()
        zip_directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        zip_directory_butt.clicked.connect(self.zip_file_dialog)

        self.zip_clear_butt = QPushButton("Clear")
        self.zip_clear_butt.clicked.connect(self.clear_zip)
        self.zip_clear_butt.setEnabled(False)

        self.import_butt = QPushButton("Start Importing Files")
        self.import_butt.clicked.connect(self.start_import)
        self.import_butt.setEnabled(False)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedHeight(10)
        separator.setLineWidth(3)

        status_title_label = QLabel("Status of Imported Files")
        status_title_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        status_title_label.setAlignment(Qt.AlignCenter)

        self.zip_status_label = QLabel("ZIP File Status: N\A")
        self.zip_status_label.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        self.zip_status_label.setAlignment(Qt.AlignCenter)

        self.status_completion_label = QLabel("Completion Status: Unavailable")
        self.status_completion_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.status_completion_label.setAlignment(Qt.AlignCenter)

        self.progress_bar_counter = 0
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)

        layout1.addWidget(import_zip_label)
        layout1.addWidget(self.zip_le)
        layout1.addWidget(zip_directory_butt)
        layout1.addWidget(self.zip_clear_butt)

        layout2.addWidget(self.zip_status_label)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addWidget(self.import_butt)
        mainlayout.addWidget(separator)
        mainlayout.addStretch()
        mainlayout.addWidget(status_title_label)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addWidget(self.status_completion_label)
        mainlayout.addWidget(self.progress_bar)
        mainlayout.addStretch()
        logging.debug("ImportManager(): Complete")

    def enable_zip_clear(self):
        logging.debug("enable_zip_clear(): Instantiated")
        self.zip_clear_butt.setEnabled(True)
        self.update_import_butt()
        logging.debug("enable_zip_clear(): Complete")

    def clear_zip(self):
        logging.debug("clear_zip(): Instantiated")
        self.zip_le.setText("")
        self.zip_clear_butt.setEnabled(False)
        self.update_import_butt()
        logging.debug("clear_zip(): Complete")

    def update_import_butt(self):
        logging.debug("update_import_butt(): Instantiated")
        if self.zip_clear_butt.isEnabled():
            self.import_butt.setEnabled(True)
        else:
            self.import_butt.setEnabled(False)
        logging.debug("update_import_butt(): Complete")

    def zip_file_dialog(self):
        logging.debug("zip_file_dialog(): Instantiated")
        file_chosen = JFileDialog().json_dialog()
        self.zip_le.setText(file_chosen)
        logging.debug("zip_file_dialog(): Complete")

    def start_import(self):
        logging.debug("start_import(): Instantiated")
        self.import_butt.setEnabled(False)
        self.progress_bar_counter = 0
        self.progress_bar.setValue(self.progress_bar_counter)
        bool_file_list = self.initial_status_update()
        self.import_thread = ImportThread(self.zip_le.text(), bool_file_list)
        self.import_thread.signal1.connect(self.successful_zip_status)
        self.import_thread.signal2.connect(self.error_zip_status)
        self.import_thread.signal3.connect(self.update_progress_bar)
        self.import_thread.signal4.connect(self.finish_progress_bar)
        self.import_thread.start()
        logging.debug("start_import(): Complete")

    def initial_status_update(self):
        logging.debug("initial_status_update(): Instantiated")
        temp_list = []
        if self.zip_le.text() == '':
            self.zip_status_label.setText("ZIP File Status: No File Input")
            temp_list.append(0)
        else:
            self.zip_status_label.setText("ZIP File Status: Starting")
            temp_list.append(1)
        self.status_completion_label.setText("Completion Status: Starting")
        logging.debug("initial_status_update(): Complete")
        return temp_list

    def successful_zip_status(self):
        logging.debug("successful_zip_status(): Instantiated")
        self.zip_status_label.setText("ZIP File Status: Successful Import")
        logging.debug("successful_config_status(): Complete")

    def error_zip_status(self):
        logging.debug("error_zip_status(): Instantiated")
        self.zip_status_label.setText("ZIP File Status: Error Encountered on Import")
        logging.debug("error_zip_status(): Complete")

    def update_progress_bar(self):
        logging.debug("update_progress_bar(): Instantiated")
        self.progress_bar_counter += 10
        if self.progress_bar_counter == 10:
            self.status_completion_label.setText("Completion Status: Working on ZIP File")
        elif self.progress_bar_counter == 100:
            self.status_completion_label.setText("Completion Status: Finished ZIP File")
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("update_progress_bar(): Complete")

    def finish_progress_bar(self):
        logging.debug("finish_progress_bar(): Instantiated")
        self.progress_bar_counter = 100
        self.status_completion_label.setText("Completion Status: Finished Importing Files")
        self.import_butt.setEnabled(True)
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("finish_progress_bar(): Complete")