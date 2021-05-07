import logging

from PyQt5.QtWidgets import QFileDialog, QWidget

class JSONFileDialog:
    def json_dialog(self):
        logging.info('json_dialog(): Instantiated')
        widget = QFileDialog()
        filename = QFileDialog.getExistingDirectory(widget, "Choose a Directory")
        return filename
        logging.info('json_dialog(): Complete')