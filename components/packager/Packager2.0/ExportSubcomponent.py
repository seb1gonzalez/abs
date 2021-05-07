import logging

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStyle, QFrame, QProgressBar

from JSONFileDialog import JSONFileDialog
from JFileDialog import JFileDialog
from ExportHandler import ExportThread

class ExportManager(QWidget):
    def __init__(self, parent):
        logging.debug("ExportManager(): Instantiated")
        super(ExportManager, self).__init__(parent)
        mainlayout = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        import_file_label = QLabel("Select Folder from Data Folder to export: ")
        import_file_label.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        import_file_label.setAlignment(Qt.AlignCenter)

        self.file_le = QLineEdit()
        self.file_le.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        self.file_le.setAlignment(Qt.AlignLeft)
        self.file_le.textChanged.connect(self.enable_file_clear)

        file_directory_butt = QPushButton()
        file_directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        file_directory_butt.clicked.connect(self.file_json_dialog)

        self.file_clear_butt = QPushButton("Clear")
        self.file_clear_butt.clicked.connect(self.clear_file)
        self.file_clear_butt.setEnabled(False)

        self.export_butt = QPushButton("Start Exporting Files")
        self.export_butt.clicked.connect(self.start_export)
        self.export_butt.setEnabled(False)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedHeight(10)
        separator.setLineWidth(3)

        status_title_label = QLabel("Status of Exported Files")
        status_title_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        status_title_label.setAlignment(Qt.AlignCenter)

        self.file_status_label = QLabel("ZIP File Status: N\A")
        self.file_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.file_status_label.setAlignment(Qt.AlignCenter)

        self.status_completion_label = QLabel("Completion Status: Unavailable")
        self.status_completion_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.status_completion_label.setAlignment(Qt.AlignCenter)

        self.progress_bar_counter = 0
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)

        layout1.addWidget(import_file_label)
        layout1.addWidget(self.file_le)
        layout1.addWidget(file_directory_butt)
        layout1.addWidget(self.file_clear_butt)

        layout2.addWidget(self.file_status_label)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addWidget(self.export_butt)
        mainlayout.addWidget(separator)
        mainlayout.addStretch()
        mainlayout.addWidget(status_title_label)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addWidget(self.status_completion_label)
        mainlayout.addWidget(self.progress_bar)
        mainlayout.addStretch()
        logging.debug("ExportManager(): Complete")

    def enable_file_clear(self):
        logging.debug("enable_file_clear(): Instantiated")
        self.file_clear_butt.setEnabled(True)
        self.update_export_butt()
        logging.debug("enable_file_clear(): Complete")

    def clear_file(self):
        logging.debug("clear_file(): Instantiated")
        self.file_le.setText("")
        self.file_clear_butt.setEnabled(False)
        self.update_export_butt()
        logging.debug("clear_file(): Complete")

    def update_export_butt(self):
        logging.debug("update_import_butt(): Instantiated")
        if self.file_clear_butt.isEnabled():
            self.export_butt.setEnabled(True)
        else:
            self.export_butt.setEnabled(False)
        logging.debug("update_import_butt(): Complete")

    def file_json_dialog(self):
        logging.debug("file_json_dialog(): Instantiated")
        file_chosen = JSONFileDialog().json_dialog()
        self.file_le.setText(file_chosen)
        logging.debug("file_json_dialog(): Complete")

    def start_export(self):
        logging.debug("start_export(): Instantiated")
        self.export_butt.setEnabled(False)
        self.progress_bar_counter = 0
        self.progress_bar.setValue(self.progress_bar_counter)
        bool_file_list = self.initial_status_update()
        self.export_thread = ExportThread(self.file_le.text(), bool_file_list)
        self.export_thread.signal1.connect(self.successful_file_status)
        self.export_thread.signal2.connect(self.error_file_status)
        self.export_thread.signal3.connect(self.update_progress_bar)
        self.export_thread.signal4.connect(self.successful_finish_progress_bar)
        self.export_thread.signal5.connect(self.failed_finish_progress_bar)
        self.export_thread.start()
        logging.debug("start_export(): Complete")

    def initial_status_update(self):
        logging.debug("initial_status_update(): Instantiated")
        temp_list = []
        if self.file_le.text() == '':
            self.file_status_label.setText("File Status: No Folder Input")
            temp_list.append(0)
        else:
            self.file_status_label.setText("File Status: Starting")
            temp_list.append(1)
        self.status_completion_label.setText("Completion Status: Starting")
        logging.debug("initial_status_update(): Complete")
        return temp_list

    def successful_file_status(self):
        logging.debug("successful_file_status(): Instantiated")
        self.file_status_label.setText("File Status: Successful Export")
        logging.debug("successful_config_status(): Complete")

    def error_file_status(self):
        logging.debug("error_file_status(): Instantiated")
        self.file_status_label.setText("File Status: Error Encountered on Export")
        logging.debug("error_file_status(): Complete")

    def update_progress_bar(self):
        logging.debug("update_progress_bar(): Instantiated")
        self.progress_bar_counter += 10
        if self.progress_bar_counter == 10:
            self.status_completion_label.setText("Completion Status: Working on ZIP File")
        elif self.progress_bar_counter == 100:
            self.status_completion_label.setText("Completion Status: Finished ZIP File")
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("update_progress_bar(): Complete")

    def successful_finish_progress_bar(self):
        logging.debug("successful_finish_progress_bar(): Instantiated")
        self.progress_bar_counter = 100
        self.status_completion_label.setText("Completion Status: Successfully Exported Files")
        self.export_butt.setEnabled(True)
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("successful_finish_progress_bar(): Complete")

    def failed_finish_progress_bar(self):
        logging.debug("failed_finish_progress_bar(): Instantiated")
        self.progress_bar_counter = 100
        self.status_completion_label.setText("Completion Status: Failed to Export Files (Zip Failure)")
        self.export_butt.setEnabled(True)
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("failed_finish_progress_bar(): Complete")