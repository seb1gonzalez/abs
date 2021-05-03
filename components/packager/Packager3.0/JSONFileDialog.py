import logging

from PyQt5.QtWidgets import QFileDialog, QWidget

class JSONFileDialog:
    def json_dialog(self):
        logging.info('json_dialog(): Instantiated')
        widget = QFileDialog()
        filename, _ = QFileDialog.getOpenFileName(widget, "Choose a file for Config.JSON", "", "JSON Files (*.JSON)")
        return filename
        logging.info('json_dialog(): Complete')