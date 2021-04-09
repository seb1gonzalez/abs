import logging

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStyle, QFrame, QProgressBar

from Packager.Dialogs.JSONFileDialog import JSONFileDialog
from Packager.ImportHandler import ImportThread

class ImportManager(QWidget):
    def __init__(self, parent):
        logging.debug("ImportManager(): Instantiated")
        super(ImportManager, self).__init__(parent)
        mainlayout = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()

        import_config_label = QLabel("Select Config.JSON file to import: ")
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

        import_relationships_label = QLabel("Select Relationships.JSON file to import: ")
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

        import_dependencies_label = QLabel("Select Dependencies.JSON file to import: ")
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

        self.config_status_label = QLabel("Config File Status: N\A")
        self.config_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.config_status_label.setAlignment(Qt.AlignCenter)

        self.relationships_status_label = QLabel("Relationships File Status: N\A")
        self.relationships_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.relationships_status_label.setAlignment(Qt.AlignCenter)

        self.dependencies_status_label = QLabel("Dependencies File Status: N\A")
        self.dependencies_status_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        self.dependencies_status_label.setAlignment(Qt.AlignCenter)

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

        layout4.addWidget(self.config_status_label)
        layout4.addWidget(self.relationships_status_label)
        layout4.addWidget(self.dependencies_status_label)

        mainlayout.addStretch()
        mainlayout.addLayout(layout1)
        mainlayout.addStretch()
        mainlayout.addLayout(layout2)
        mainlayout.addStretch()
        mainlayout.addLayout(layout3)
        mainlayout.addStretch()
        mainlayout.addWidget(self.import_butt)
        mainlayout.addWidget(separator)
        mainlayout.addStretch()
        mainlayout.addWidget(status_title_label)
        mainlayout.addStretch()
        mainlayout.addLayout(layout4)
        mainlayout.addStretch()
        mainlayout.addWidget(self.status_completion_label)
        mainlayout.addWidget(self.progress_bar)
        mainlayout.addStretch()
        logging.debug("ImportManager(): Complete")

    def enable_config_clear(self):
        logging.debug("enable_config_clear(): Instantiated")
        self.config_clear_butt.setEnabled(True)
        self.update_import_butt()
        logging.debug("enable_config_clear(): Complete")

    def clear_config(self):
        logging.debug("clear_config(): Instantiated")
        self.config_le.setText("")
        self.config_clear_butt.setEnabled(False)
        self.update_import_butt()
        logging.debug("clear_config(): Complete")

    def enable_relationship_clear(self):
        logging.debug("enable_relationship_clear(): Instantiated")
        self.relationships_clear_butt.setEnabled(True)
        self.update_import_butt()
        logging.debug("enable_relationship_clear(): Complete")

    def clear_relationship(self):
        logging.debug("clear_relationship(): Instantiated")
        self.relationships_le.setText("")
        self.relationships_clear_butt.setEnabled(False)
        self.update_import_butt()
        logging.debug("clear_relationship(): Complete")

    def enable_dependency_clear(self):
        logging.debug("enable_dependency_clear(): Instantiated")
        self.dependencies_clear_butt.setEnabled(True)
        self.update_import_butt()
        logging.debug("enable_dependency_clear(): Complete")

    def clear_dependency(self):
        logging.debug("clear_dependency(): Instantiated")
        self.dependencies_le.setText("")
        self.dependencies_clear_butt.setEnabled(False)
        self.update_import_butt()
        logging.debug("clear_dependency(): Complete")

    def update_import_butt(self):
        logging.debug("update_import_butt(): Instantiated")
        if self.config_clear_butt.isEnabled() or self.relationships_clear_butt.isEnabled() or self.dependencies_clear_butt.isEnabled():
            self.import_butt.setEnabled(True)
        else:
            self.import_butt.setEnabled(False)
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

    def start_import(self):
        logging.debug("start_import(): Instantiated")
        self.import_butt.setEnabled(False)
        self.progress_bar_counter = 0
        self.progress_bar.setValue(self.progress_bar_counter)
        bool_file_list = self.initial_status_update()
        self.import_thread = ImportThread(self.config_le.text(), self.relationships_le.text(), self.dependencies_le.text(), bool_file_list)
        self.import_thread.signal1.connect(self.successful_config_status)
        self.import_thread.signal2.connect(self.error_config_status)
        self.import_thread.signal3.connect(self.successful_relationship_status)
        self.import_thread.signal4.connect(self.error_relationship_status)
        self.import_thread.signal5.connect(self.successful_dependency_status)
        self.import_thread.signal6.connect(self.error_dependency_status)
        self.import_thread.signal7.connect(self.update_progress_bar)
        self.import_thread.signal8.connect(self.finish_progress_bar)
        self.import_thread.start()
        logging.debug("start_import(): Complete")

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
        self.status_completion_label.setText("Completion Status: Starting")
        logging.debug("initial_status_update(): Complete")
        return temp_list

    def successful_config_status(self):
        logging.debug("successful_config_status(): Instantiated")
        self.config_status_label.setText("Config File Status: Successful Import")
        logging.debug("successful_config_status(): Complete")

    def error_config_status(self):
        logging.debug("error_config_status(): Instantiated")
        self.config_status_label.setText("Config File Status: Error Encountered on Import")
        logging.debug("error_config_status(): Complete")

    def successful_relationship_status(self):
        logging.debug("successful_relationship_status(): Instantiated")
        self.relationships_status_label.setText("Relationships File Status: Successful Import")
        logging.debug("successful_relationship_status(): Complete")

    def error_relationship_status(self):
        logging.debug("error_relationship_status(): Instantiated")
        self.relationships_status_label.setText("Relationships File Status: Error Encountered on Import")
        logging.debug("error_relationship_status(): Complete")

    def successful_dependency_status(self):
        logging.debug("successful_dependency_status(): Instantiated")
        self.dependencies_status_label.setText("Dependencies File Status: Successful Import")
        logging.debug("successful_dependency_status(): Complete")

    def error_dependency_status(self):
        logging.debug("error_dependency_status(): Instantiated")
        self.dependencies_status_label.setText("Dependencies File Status: Error Encountered on Import")
        logging.debug("error_dependency_status(): Complete")

    def update_progress_bar(self):
        logging.debug("update_progress_bar(): Instantiated")
        self.progress_bar_counter += 16
        if self.progress_bar_counter == 16:
            self.status_completion_label.setText("Completion Status: Working on Config File")
        elif self.progress_bar_counter == 32:
            self.status_completion_label.setText("Completion Status: Finished Config File")
        elif self.progress_bar_counter == 48:
            self.status_completion_label.setText("Completion Status: Working on Relationships File")
        elif self.progress_bar_counter == 64:
            self.status_completion_label.setText("Completion Status: Finished Relationships File")
        elif self.progress_bar_counter == 80:
            self.status_completion_label.setText("Completion Status: Working on Dependencies File")
        elif self.progress_bar_counter == 96:
            self.status_completion_label.setText("Completion Status: Finished Dependencies File")
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("update_progress_bar(): Complete")

    def finish_progress_bar(self):
        logging.debug("finish_progress_bar(): Instantiated")
        self.progress_bar_counter = 100
        self.status_completion_label.setText("Completion Status: Finished Importing Files")
        self.import_butt.setEnabled(True)
        self.progress_bar.setValue(self.progress_bar_counter)
        logging.debug("finish_progress_bar(): Complete")


    """ def __init__(self, parent):
        super(ImportManager, self).__init__(parent)
        global list
        list = []
        self.pbar = QProgressBar(self)
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(125,100)
        self.label1 = QLabel("", self)
        self.label1.setFixedWidth(10000)
        self.label1.move(30, 150)
        self.pushButton.clicked.connect(self.actionButton2)

    def actionButton2(self):
        file_chosen = JFileDialog().json_dialog() #file select
        for i in range(101): #progress bar
            time.sleep(0.05)
            self.pbar.setValue(i)
        head, name = ntpath.split(file_chosen) #obtain file name
        list.append(name) #add to list
        if substring in name:
            with open(file_chosen) as f:
                data = json.load(f)
                dataFile.append(data)
        else:
            data2 = open(file_chosen)
            dataFile.append(data2.read())
        print(dataFile)
        temp = " ".join(list)
        self.label1.setText(temp) """