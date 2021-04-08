import logging

from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QProgressBar, QPushButton

from Causal_Extractor.RelationshipExtractor import RelationshipExtractor

class ResultsDlg(QDialog):
    def __init__(self):
        logging.debug('create_dialog(): Instantiated')
        super().__init__()
        self.setWindowTitle("Results")
        self.setGeometry(750, 100, 400, 150)
        
        self.artifact_counter = 0
        self.relationship_counter = 0
        self.progress_counter= 0

        mainlayout = QVBoxLayout(self)

        self.artifact_label = QLabel("Salient Artifacts: " + str(self.artifact_counter))

        self.relationship_label = QLabel("Pairwise Relationships: " + str(self.relationship_counter))

        self.status_label = QLabel("Status: Not Finished")

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        
        self.continue_bttn = QPushButton("Ok")
        self.continue_bttn.setEnabled(False)

        mainlayout.addWidget(self.artifact_label)
        mainlayout.addWidget(self.relationship_label)
        mainlayout.addWidget(self.status_label)
        mainlayout.addWidget(self.progress_bar)
        logging.debug('create_dialog(): Completed')

    def start_extraction(self, files, delta_time):
        logging.debug('start_extraction(): Instantiated')
        self.relationship_thread = RelationshipExtractor(files, delta_time)
        self.relationship_thread.signal1.connect(self.update_artifact)
        self.relationship_thread.signal2.connect(self.update_relationship)
        self.relationship_thread.signal3.connect(self.update_progress_bar)
        self.relationship_thread.start()
        logging.debug('start_extraction(): Completed')

    def update_artifact(self):
        logging.debug('update_artifact(): Signal1 Emit')
        self.artifact_counter += 1
        self.artifact_label.setText("Salient Artifacts: " + str(self.artifact_counter))

    def update_relationship(self):
        logging.debug('update_relationship(): Signal2 Emit')
        self.relationship_counter += 1
        self.relationship_label.setText("Pairwise Relationships: " + str(self.relationship_counter))

    def update_progress_bar(self):
        logging.debug('update_progress_bar(): Signal3 Emit')
        self.progress_counter += 20
        self.progress_bar.setValue(self.progress_counter)
        self.thread_status()

    def thread_status(self):
        logging.debug('thread_status(): Check')
        if self.progress_counter == 0:
            self.status_label.setText("Status: Retrieving JSON Data")
        elif self.progress_counter == 20:
            self.status_label.setText("Status: Retrieving Artifacts")
        elif self.progress_counter == 40:
            self.status_label.setText("Status: Finding Relationships")
        elif self.progress_counter == 60:
            self.status_label.setText("Status: Cleaning Relationship Structure")
        elif self.progress_counter == 80:
            self.status_label.setText("Status: Writing Relationships to File")
        else:
            self.status_label.setText("Status: Finished")
            self.continue_bttn.setEnabled(True)