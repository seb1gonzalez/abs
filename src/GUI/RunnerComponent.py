from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox, QFileDialog, QVBoxLayout, QPushButton)
from Runner.Runner import Runner
import sys
import subprocess
import logging

class App(QWidget):
        
    def __init__(self):
        super().__init__()
        self.title = 'Runner Component'
        self.left = 10
        self.top = 10
        self. width = 500
        self.height = 250
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QVBoxLayout()
        self.button = QPushButton('Invoke ECELd')
        self.button2 = QPushButton('Import Scripts')
        self.button3 = QPushButton('Run Agent')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.ECELd_clicked)
        self.button2.clicked.connect(self.import_script_button_clicked)
        self.button3.clicked.connect(self.run_agent_clicked)
        self.show()

    def ECELd_clicked(self):
        alert = QMessageBox()
        alert.setText('ECELd has been invoked!')
        alert.exec()
        Runner.run_eceldnetsys(self)


    def import_script_button_clicked(self):
        global cmd
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        alert = QMessageBox()
        alert.setText(fileName + " has been loaded.")
        alert.exec()
        cmd = str(fileName)
        print(cmd)


    def run_agent_clicked(self):
        try:
            subprocess.run(cmd, shell=True)
        except NameError:
            alert = QMessageBox()
            alert.setText('No script was specified.')
            alert.exec()
            print("No script was specified.")
        
        
        


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
