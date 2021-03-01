from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QVBoxLayout, QPushButton
from runner import Runner
import sys

class App(QWidget):
        
    def __init__(self):
        super().__init__()
        self.title = 'Runner Component'
        self.left = 10
        self.top = 10
        self. width = 500
        self.height = 150
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QVBoxLayout()
        self.button = QPushButton('Invoke ECELd')
        self.button2 = QPushButton('Import Scripts')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.on_ECELd_clicked)
        self.button2.clicked.connect(self.on_button_clicked)
        self.show()

    def on_ECELd_clicked(self):
        Runner.run_eceldnetsys()

    def on_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())