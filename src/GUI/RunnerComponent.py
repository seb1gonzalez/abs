from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog, QLineEdit, QLabel, QMessageBox, QFileDialog, QVBoxLayout, QGridLayout, QHBoxLayout, QPushButton, QPlainTextEdit)
from Runner.Runner import Runner
import sys
import subprocess
import logging


class RunnerApp(QWidget):
        
    global cmd

    def __init__(self, parent):
        super().__init__(parent)
        self.title = 'Runner Component'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 250
        self.initUI()
    
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.layout = QVBoxLayout()
        self.button = QPushButton('Invoke ECELd')
        self.button.setFixedSize(250, 30)
        self.button2 = QPushButton('Import Script')
        self.button2.setFixedSize(250, 30)
        self.deletebutton = QPushButton('Clear Script')
        self.deletebutton.setFixedSize(250,30)
        
        self.scriptlabel = QLabel('Script: ')
        self.scriptlabel.setWordWrap(True)
        self.scriptlabel.setFixedWidth(250)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.scriptlabel)
        self.layout.addWidget(self.deletebutton)
        
        self.run = QHBoxLayout()
        self.run.addStretch(1)
        self.button3 = QPushButton('Run Agent')
        self.button3.setFixedSize(100,30)
        self.run.addWidget(self.button3) 

        self.logwindow = QVBoxLayout()
        self.log = QPlainTextEdit()
        self.log.setFixedWidth(300)
        self.log.setReadOnly(True)
        content = self.open_log_file()
        self.log.setPlainText(content)
        self.logwindow.addWidget(self.log)
        self.logwindow.addLayout(self.run)
        
        self.mainlayout = QHBoxLayout()
        self.mainlayout.addLayout(self.layout)
        self.mainlayout.addLayout(self.logwindow)
        
        self.setLayout(self.mainlayout)

        self.button.clicked.connect(self.ECELd_clicked)
        self.button2.clicked.connect(self.import_script_button_clicked)
        self.button3.clicked.connect(self.run_agent_clicked)
        self.deletebutton.clicked.connect(self.clear_loaded_script)
        #self.show()

    def ECELd_clicked(self):
        self.display_alert('ECELd has been invoked!')
        Runner.run_eceld(self)


    def set_script_name(self, cmd):
        self.scriptlabel.setText("Script: "+ cmd)


    def import_script_button_clicked(self):
        global cmd
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        self.display_alert(fileName + " has been loaded.")
        cmd = str(fileName)
        print(cmd)
        self.set_script_name(cmd)
        self.update_log_window("\nDEBUG:root:RunnerComponent.py(): Script Added.")


    def run_agent_clicked(self):
        try:
            subprocess.run(cmd, shell=True)
        except (NameError , TypeError):
            self.display_alert('No script was specified.')


    def open_log_file(self):
        global content
        f = open('/home/kali/Desktop/abs/src/GUI/Runner/logs.txt', 'r')
        content = f.read()
        f.close()
        return content

    def update_log_window(self, msg):
        f = open('/home/kali/Desktop/abs/src/GUI/Runner/logs.txt', 'a')
        f.write(msg)
        f.close()
        self.open_log_file()
        self.log.setPlainText(content)

    def clear_loaded_script(self):
        global cmd
        try:
            if cmd is None:
                self.set_script_name('')
                self.display_alert('Script has already been cleared.')
            else:
                cmd = None
                self.set_script_name('')
                self.update_log_window("\nDEBUG:root:RunnerComponent.py(): Script Removed.")
        except (NameError, TypeError):
            self.display_alert('Nothing to clear.')
            

    def display_alert(self, msg):
        alert = QMessageBox()
        alert.setText(msg)
        alert.exec()
        self.update_log_window("\nDEBUG:root:RunnerComponent.py(): "+msg)



    
    


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
