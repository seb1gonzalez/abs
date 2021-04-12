from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog, QLineEdit, QLabel, QMessageBox, QFileDialog, QVBoxLayout, QGridLayout, QHBoxLayout, QPushButton, QPlainTextEdit)
from PyQt5.QtGui import QTextCursor
from Runner.Runner import Runner
#from ..agent_builder.agent_builder import build_agent
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
        

        self.layout = QHBoxLayout()
        self.button1 = QPushButton('Import Script')
        self.button1.setFixedSize(125, 30)
        self.layout = QHBoxLayout()
        self.button2 = QPushButton('Clear Script')
        self.button2.setFixedSize(125, 30)
        
        self.scriptlabel = QLabel('Script: ')
        self.scriptlabel.setWordWrap(False)
        #self.scriptlabel.setFixedWidth(250)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.scriptlabel)
        self.run = QHBoxLayout()
        self.run.addStretch(1)
        self.button3 = QPushButton('Run Agent')
        self.button3.setFixedSize(100,30)
        self.run.addWidget(self.button3) 

        self.logwindow = QVBoxLayout()
        self.log = QPlainTextEdit()
        #self.log.setFixedWidth(300)
        self.log.setReadOnly(True)
        self.log.moveCursor(QTextCursor.End)
        content = self.open_log_file()
        self.log.setPlainText(content)
        self.logwindow.addWidget(self.log)
        self.logwindow.addLayout(self.run)
        
        self.scriptwindow = QHBoxLayout()
        self.script = QPlainTextEdit()
        #script_content = self.open_script_file()
        #self.script.setPlainText(script_content)
        self.scriptwindow.addWidget(self.script)
        self.scriptwindow.addLayout(self.logwindow)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addLayout(self.layout)
        self.mainlayout.addLayout(self.scriptwindow)
        
        self.setLayout(self.mainlayout)

        self.button1.clicked.connect(self.import_script_button_clicked)
        self.button2.clicked.connect(self.clear_loaded_script)
        self.button3.clicked.connect(self.run_agent_clicked)
        #self.show()


    def ECELd_clicked(self):
        self.display_alert('ECELd has been invoked!')
        Runner.run_eceld(self)

    #helper fuction to set script name on gui
    def set_script_name(self, cmd):
        self.scriptlabel.setText("Script: "+ cmd)

    #import script
    def import_script_button_clicked(self):
        global cmd
        global fileName
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        self.display_alert(fileName + " has been loaded.")
        cmd = "python3 " + str(fileName)
        print(cmd)
        self.set_script_name(str(fileName))
        self.update_log_window("\nDEBUG:root:RunnerComponent.py(): Script Added.")
        script_content = self.open_script_file(fileName)
        self.script.setPlainText(script_content)
        #print(self.script.toPlainText())

    #run agent
    def run_agent_clicked(self):
        self.update_script(fileName)
        try:
            subprocess.run(cmd, shell=True)
        except (NameError , TypeError):
            self.display_alert('No script was specified.')


    #initialize or grab preexisting log history
    def open_log_file(self):
        global content
        f = open('Runner/logs.txt', 'r')
        content = f.read()
        f.close()
        return content

    def open_script_file(self, file):
        global script_content
        f = open(file, 'r')
        script_content = f.read()
        f.close()
        return script_content

    #appends each log to log history
    def update_log_window(self, msg):
        f = open('Runner/logs.txt', 'a')
        f.write(msg)
        f.close()
        self.open_log_file()
        self.log.setPlainText(content)
        self.log.moveCursor(QTextCursor.End)


    def update_script(self, file):
        f = open(file, 'w')
        new_content = self.script.toPlainText()
        f.write(new_content)
        f.close()
    

    #clears loaded script
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

    #display message box alert
    def display_alert(self, msg):
        alert = QMessageBox()
        alert.setText(msg)
        alert.exec()
        self.update_log_window("\nDEBUG:root:RunnerComponent.py(): "+msg)

    #clears loaded script
    def clear_loaded_script(self):
        global cmd
        try:
            if cmd is None:
                self.set_script_name('')
                self.display_alert('Script has already been cleared.')
            else:
                cmd = None
                self.set_script_name('')
                self.script.setPlainText('')
                self.update_log_window("\nDEBUG:root:RunnerComponent.py(): Script Removed.")
        except (NameError, TypeError):
            self.display_alert('Nothing to clear.')

    #display message box alert
    def display_alert(self, msg):
        alert = QMessageBox()
        alert.setText(msg)
        alert.exec()
        self.update_log_window("\nDEBUG:root:RunnerComponent.py(): "+msg)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
