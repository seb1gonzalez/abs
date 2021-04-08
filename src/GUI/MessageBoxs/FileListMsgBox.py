import logging

from PyQt5.QtWidgets import QMessageBox, QTextEdit

class FileListMsgBox:
    def create_msg_box(self, item_name):
        logging.debug("create_msg_box(): Instantiated")
        msg = QMessageBox()
        msg.setWindowTitle("List File Information")
        msg.setMaximumHeight(500)
        msg.setIcon(QMessageBox.Information)
        msg.setText("The file to be imported: \n" + item_name)
        msg.setInformativeText("Click on Show Details to see what is contained inside the file.")

        self.get_file_info(msg, item_name)

        retval = msg.exec_()
        logging.debug("create_msg_box(): Complete")

    def get_file_info(self, msg, file):
        logging.debug("get_file_info(): Instantiated")
        f_buff = open(file, "r")
        msg.setDetailedText(f_buff.read())
        f_buff.close()
        logging.debug("get_file_info(): Complete")