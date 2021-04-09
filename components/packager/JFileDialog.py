from PyQt5.QtWidgets import QFileDialog, QWidget
import logging

class JFileDialog:
    def json_dialog(self):
        logging.info('json_dialog(): Instantiated')
        widget = QFileDialog()
        filename, _ = QFileDialog.getOpenFileNames(widget, "Choose a file", "", "All Files (*)")
        return filename[0]
        logging.info('json_dialog(): Completed')