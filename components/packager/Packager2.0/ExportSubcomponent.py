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
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        import_config_label = QLabel("Select Config.JSON file to export: ")
        import_config_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        import_config_label.setAlignment(Qt.AlignCenter)

        self.config_le = QLineEdit()
        self.config_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.config_le.setAlignment(Qt.AlignLeft)
        self.config_le.textChanged.connect(self.enable_config_clear)

        config_directory_butt = QPushButton()
        config_directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        config_directory_butt.clicked.connect(self.config_json_dialog)

        self.config_clear_butt = QPushButton("Clear")
        self.config_clear_butt.clicked.connect(self.clear_config)
        self.config_clear_butt.setEnabled(False)

        import_relationships_label = QLabel("Select Relationships.JSON file to export: ")
        import_relationships_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        import_relationships_label.setAlignment(Qt.AlignCenter)

        self.relationships_le = QLineEdit()
        self.relationships_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.relationships_le.setAlignment(Qt.AlignLeft)
        self.relationships_le.textChanged.connect(self.enable_relationship_clear)

        relationships_directory_butt = QPushButton()
        relationships_directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        relationships_directory_butt.clicked.connect(self.relationship_json_dialog)

        self.relationships_clear_butt = QPushButton("Clear")
        self.relationships_clear_butt.clicked.connect(self.clear_relationship)
        self.relationships_clear_butt.setEnabled(False)

        import_dependencies_label = QLabel("Select Dependencies.JSON file to export: ")
        import_dependencies_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        import_dependencies_label.setAlignment(Qt.AlignCenter)

        self.dependencies_le = QLineEdit()
        self.dependencies_le.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.dependencies_le.setAlignment(Qt.AlignLeft)
        self.dependencies_le.textChanged.connect(self.enable_dependency_clear)

        dependencies_directory_butt = QPushButton()
        dependencies_directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        dependencies_directory_butt.clicked.connect(self.dependency_json_dialog)

        self.dependencies_clear_butt = QPushButton("Clear")
        self.dependencies_clear_butt.clicked.connect(self.clear_dependency)
        self.dependencies_clear_butt.setEnabled(False)

        import_vm_label = QLabel("Select OVA file to Export: ")
        import_vm_label.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        import_vm_label.setAlignment(Qt.AlignCenter)

        self.vm_le = QLineEdit()
        self.vm_le.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        self.vm_le.setAlignment(Qt.AlignLeft)
        self.vm_le.textChanged.connect(self.enable_vm_clear)

        vm_directory_butt = QPushButton()
        vm_directory_butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirIcon')))
        vm_directory_butt.clicked.connect(self.vm_file_dialog)

        self.vm_clear_butt = QPushButton("Clear")
        self.vm_clear_butt.clicked.connect(self.clear_vm)
        self.vm_clear_butt.setEnabled(False)

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

        self.config_status_label = QLabel("Config File Status: N\A")
        self.config_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.config_status_label.setAlignment(Qt.AlignCenter)

        self.relationships_status_label = QLabel("Relationships File Status: N\A")
        self.relationships_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.relationships_status_label.setAlignment(Qt.AlignCenter)

        self.dependencies_status_label = QLabel("Dependencies File Status: N\A")
        self.dependencies_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.dependencies_status_label.setAlignment(Qt.AlignCenter)

        self.vm_status_label = QLabel("VM OVA Status: N\A")
        self.vm_status_label.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        self.vm_status_label.setAlignment(Qt.AlignCenter)

        self.status_completion_label = QLabel("Completion Status: Unavailable")
        self.status_completion_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.status_completion_label.setAlignment(Qt.AlignCenter)

        self.progress_bar_counter = 0
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)

        layout1.addWidget(import_config_label)
        layout1.addWidget(self.config_le)
        layout1.addWidget(config_directory_butt)
        layout1.addWidget(self.config_clear_butt)

        layout2.addWidget(import_relationships_label)
        layout2.addWidget(self.relationships_le)
        layout2.addWidget(relationships_directory_butt)
        layout2.addWidget(self.relationships_clear_butt)

        layout3.addWidget(import_dependencies_label)
        layout3.addWidget(self.dependencies_le)
        layout3.addWidget(dependencies_directory_butt)
        layout3.addWidget(self.dependencies_clear_butt)

        layout4.addWidget(import_vm_label)
        layout4.addWidget(self.vm_le)
        layout4.addWidget(vm_directory_butt)
        layout4.addWidget(self.vm_clear_butt)

        layout5.addWidget(self.config_status_label)
        layout5.addWidget(self.relationships_status_label)
        layout5.addWidget(self.dependencies_status_label)
        layout5.addWidget(self.vm_status_label)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addLayout(layout3)
        mainlayout.addStretch()
        mainlayout.addLayout(layout4)
        mainlayout.addStretch()
        mainlayout.addWidget(self.export_butt)
        mainlayout.addWidget(separator)
        mainlayout.addStretch()
        mainlayout.addWidget(status_title_label)
        mainlayout.addStretch()
        mainlayout.addLayout(layout5)
        mainlayout.addStretch()
        mainlayout.addWidget(self.status_completion_label)
        mainlayout.addWidget(self.progress_bar)
        mainlayout.addStretch()
        logging.debug("ExportManager(): Complete")

    def enable_config_clear(self):
        logging.debug("enable_config_clear(): Instantiated")
        self.config_clear_butt.setEnabled(True)
        self.update_export_butt()
        logging.debug("enable_config_clear(): Complete")

    def clear_config(self):
        logging.debug("clear_config(): Instantiated")
        self.config_le.setText("")
        self.config_clear_butt.setEnabled(False)
        self.update_export_butt()
        logging.debug("clear_config(): Complete")

    def enable_relationship_clear(self):
        logging.debug("enable_relationship_clear(): Instantiated")
        self.relationships_clear_butt.setEnabled(True)
        self.update_export_butt()
        logging.debug("enable_relationship_clear(): Complete")

    def clear_relationship(self):
        logging.debug("clear_relationship(): Instantiated")
        self.relationships_le.setText("")
        self.relationships_clear_butt.setEnabled(False)
        self.update_export_butt()
        logging.debug("clear_relationship(): Complete")

    def enable_dependency_clear(self):
        logging.debug("enable_dependency_clear(): Instantiated")
        self.dependencies_clear_butt.setEnabled(True)
        self.update_export_butt()
        logging.debug("enable_dependency_clear(): Complete")

    def clear_dependency(self):
        logging.debug("clear_dependency(): Instantiated")
        self.dependencies_le.setText("")
        self.dependencies_clear_butt.setEnabled(False)
        self.update_export_butt()
        logging.debug("clear_dependency(): Complete")

    def enable_vm_clear(self):
        logging.debug("enable_vm_clear(): Instantiated")
        self.vm_clear_butt.setEnabled(True)
        self.update_export_butt()
        logging.debug("enable_vm_clear(): Complete")

    def clear_vm(self):
        logging.debug("clear_vm(): Instantiated")
        self.vm_le.setText("")
        self.vm_clear_butt.setEnabled(False)
        self.update_export_butt()
        logging.debug("clear_vm(): Complete")

    def update_export_butt(self):
        logging.debug("update_import_butt(): Instantiated")
        if self.config_clear_butt.isEnabled() or self.relationships_clear_butt.isEnabled() or self.dependencies_clear_butt.isEnabled() or self.vm_clear_butt.isEnabled():
            self.export_butt.setEnabled(True)
        else:
            self.export_butt.setEnabled(False)
        logging.debug("update_import_butt(): Complete")

    def config_json_dialog(self):
        logging.debug("config_json_dialog(): Instantiated")
        file_chosen = JSONFileDialog().json_dialog()
        self.config_le.setText(file_chosen)
        logging.debug("config_json_dialog(): Complete")

    def relationship_json_dialog(self):
        logging.debug("relationship_json_dialog(): Instantiated")
        file_chosen = JSONFileDialog().json_dialog()
        self.relationships_le.setText(file_chosen)
        logging.debug("relationship_json_dialog(): Complete")

    def dependency_json_dialog(self):
        logging.debug("dependency_json_dialog(): Instantiated")
        file_chosen = JSONFileDialog().json_dialog()
        self.dependencies_le.setText(file_chosen)
        logging.debug("dependency_json_dialog(): Complete")

    def vm_file_dialog(self):
        logging.debug("vm_file_dialog(): Instantiated")
        file_chosen = JFileDialog().json_dialog()
        self.vm_le.setText(file_chosen)
        logging.debug("vm_file_dialog(): Complete")

    def start_export(self):
        logging.debug("start_export(): Instantiated")
        self.export_butt.setEnabled(False)
        self.progress_bar_counter = 0
        self.progress_bar.setValue(self.progress_bar_counter)
        bool_file_list = self.initial_status_update()
        self.export_thread = ExportThread(self.config_le.text(), self.relationships_le.text(), self.dependencies_le.text(), self.vm_le.text(), bool_file_list)
        self.export_thread.signal1.connect(self.successful_config_status)
        self.export_thread.signal2.connect(self.error_config_status)
        self.export_thread.signal3.connect(self.successful_relationship_status)
        self.export_thread.signal4.connect(self.error_relationship_status)
        self.export_thread.signal5.connect(self.successful_dependency_status)
        self.export_thread.signal6.connect(self.error_dependency_status)
        self.export_thread.signal7.connect(self.successful_vm_status)
        self.export_thread.signal8.connect(self.error_vm_status)
        self.export_thread.signal9.connect(self.update_progress_bar)
        self.export_thread.signal10.connect(self.successful_finish_progress_bar)
        self.export_thread.signal11.connect(self.failed_finish_progress_bar)
        self.export_thread.start()
        logging.debug("start_export(): Complete")

    def initial_status_update(self):
        logging.debug("initial_status_update(): Instantiated")
        temp_list = []
        if self.config_le.text() == '':
            self.config_status_label.setText("Config File Status: No File Input")
            temp_list.append(0)
        else:
            self.config_status_label.setText("Config File Status: Starting")
            temp_list.append(1)
        if self.relationships_le.text() == '':
            self.relationships_status_label.setText("Relationships File Status: No File Input")
            temp_list.append(0)
        else:
            self.relationships_status_label.setText("Relationships File Status: Starting")
            temp_list.append(1)
        if self.dependencies_le.text() == '':
            self.dependencies_status_label.setText("Dependencies File Status: No File Input")
            temp_list.append(0)
        else:
            self.dependencies_status_label.setText("Dependencies File Status: Starting")
            temp_list.append(1)
        if self.vm_le.text() == '':
            self.vm_status_label.setText("VM OVA Status: No File Input")
            temp_list.append(0)
        else:
            self.vm_status_label.setText("VM OVA Status: Starting")
            temp_list.append(1)
        self.status_completion_label.setText("Completion Status: Starting")
        logging.debug("initial_status_update(): Complete")
        return temp_list

    def successful_config_status(self):
        logging.debug("successful_config_status(): Instantiated")
        self.config_status_label.setText("Config File Status: Successful Export")
        logging.debug("successful_config_status(): Complete")

    def error_config_status(self):
        logging.debug("error_config_status(): Instantiated")
        self.config_status_label.setText("Config File Status: Error Encountered on Export")
        logging.debug("error_config_status(): Complete")

    def successful_relationship_status(self):
        logging.debug("successful_relationship_status(): Instantiated")
        self.relationships_status_label.setText("Relationships File Status: Successful Export")
        logging.debug("successful_relationship_status(): Complete")

    def error_relationship_status(self):
        logging.debug("error_relationship_status(): Instantiated")
        self.relationships_status_label.setText("Relationships File Status: Error Encountered on Export")
        logging.debug("error_relationship_status(): Complete")

    def successful_dependency_status(self):
        logging.debug("successful_dependency_status(): Instantiated")
        self.dependencies_status_label.setText("Dependencies File Status: Successful Export")
        logging.debug("successful_dependency_status(): Complete")

    def error_dependency_status(self):
        logging.debug("error_dependency_status(): Instantiated")
        self.dependencies_status_label.setText("Dependencies File Status: Error Encountered on Export")
        logging.debug("error_dependency_status(): Complete")

    def successful_vm_status(self):
        logging.debug("successful_vm_status(): Instantiated")
        self.vm_status_label.setText("VM OVA Status: Successful Export")
        logging.debug("successful_vm_status(): Complete")

    def error_vm_status(self):
        logging.debug("error_vm_status(): Instantiated")
        self.vm_status_label.setText("VM OVA Status: Error Encountered on Export")
        logging.debug("error_dependency_status(): Complete")

    def update_progress_bar(self):
        logging.debug("update_progress_bar(): Instantiated")
        self.progress_bar_counter += 10
        if self.progress_bar_counter == 10:
            self.status_completion_label.setText("Completion Status: Working on Config File")
        elif self.progress_bar_counter == 20:
            self.status_completion_label.setText("Completion Status: Finished Config File")
        elif self.progress_bar_counter == 30:
            self.status_completion_label.setText("Completion Status: Working on Relationships File")
        elif self.progress_bar_counter == 40:
            self.status_completion_label.setText("Completion Status: Finished Relationships File")
        elif self.progress_bar_counter == 50:
            self.status_completion_label.setText("Completion Status: Working on Dependencies File")
        elif self.progress_bar_counter == 60:
            self.status_completion_label.setText("Completion Status: Finished Dependencies File")
        elif self.progress_bar_counter == 70:
            self.status_completion_label.setText("Completion Status: Working on OVA File")
        elif self.progress_bar_counter == 80:
            self.status_completion_label.setText("Completion Status: Finished OVA File")
        elif self.progress_bar_counter == 90:
            self.status_completion_label.setText("Completion Status: Working on Zip File")
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