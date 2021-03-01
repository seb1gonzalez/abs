import logging

from PyQt5.QtWidgets import QMessageBox

class FileListMsgBox:
    def create_msg_box(self, item_name):
        logging.debug("create_msg_box(): Instantiated")
        msg = QMessageBox()
        msg.setWindowTitle("List File Information")
        msg.setMaximumHeight(500)
        msg.setIcon(QMessageBox.Information)
        msg.setText("The file you have selected is: " + item_name)
        msg.setInformativeText("Here you can see more details about the file you selected.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)
        retval = msg.exec_()
        logging.debug("value of pressed message box button: " + str(retval))
        logging.debug("create_msg_box(): Complete")

    def msgbtn(self, i):
        logging.debug("msgbtn(): Instantiated")
        logging.debug("Button pressed is: " + i.text())
        logging.debug("msgbtn(): Complete")