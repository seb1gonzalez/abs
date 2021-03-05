from PyQt5.QtWidgets import QFileDialog, QWidget
import logging

class DirectoryDialog:
    def directory_dialog(self):
        logging.info('directory_dialog(): Instantiated')
        widget = QFileDialog()
        foldername = str(QFileDialog.getExistingDirectory(widget, "Select Directory Containing JSON Files"))
        return foldername
        logging.info('directory_dialog(): Completed')