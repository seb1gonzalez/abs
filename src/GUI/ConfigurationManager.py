import logging
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class ConfMng(QMainWindow):
    def __init__(self):
        logging.info("ConfMng(): Instantiated")
        super(ConfMng, self).__init__()
        self.setWindowTitle("Agent Build System: Configuration Manager")
        mainwidget = QWidget()
        self.setCentralWidget(mainwidget)
        mainlayout = QVBoxLayout()
        layout1 = QHBoxLayout()

        agent_name_label = QLabel("Name of agent:")
        agent_name_label.setFont(QtGui.QFont("Times", weight = QtGui.QFont.Bold))
        agent_name_label.setAlignment(Qt.AlignLeft)

        layout1.addWidget(agent_name_label)

        mainlayout.addLayout(layout1)
        logging.info("ConfMng(): Complete")

if __name__ == '__main__':
    logging.info("main(): Instantiated")
    logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.DEBUG)
    #appctxt = ApplicationContext()
    app = QApplication(sys.argv)
    app = ConfMng()
    #app.setGeometry(500, 300, 500, 150)
    app.show()
    #sys.exit(app.exec_())
    app.exec_()
    #exit_code = appctxt.app.exec_()
    logging.info("main(): Complete")