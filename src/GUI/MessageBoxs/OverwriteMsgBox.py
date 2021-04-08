import logging

from PyQt5.QtWidgets import QMessageBox

class OverwriteMsgBox:
    def create_msg_box(self, file_info, success):
        logging.debug("create_msg_box(): Instantiated")
        msg = QMessageBox()
        msg.setWindowTitle("Overwrite Information")
        msg.setMaximumHeight(500)
        msg.setIcon(QMessageBox.Information)

        if success:
            string_info = ""
            msg.setText("The file information you have provided has been overwritten.")
            for key in file_info:
                string_info += key + "->" + str(file_info[key]) + "\n"
            msg.setDetailedText(string_info)

        if not success:
            msg.setText("The file information you have provided has encountered an error.")

        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        logging.debug("create_msg_box(): Complete")