import json
from JSONTREE.qjsonmodel import QJsonModel

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QAction, QWidget, QFileDialog, \
    QTextEdit, QPushButton, QVBoxLayout, QGridLayout, QTreeView
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
# from BuilderTreeView import TreeviewBuilder

class DialogApp(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        # self.resize(500,500)
        # self.setWindowTitle("Builder: Import Module")

        self.grid_layout = QGridLayout()

        self.json_model = QJsonModel()
        self.json_tree_view = QTreeView()
        # self.get_text_file()
        self.json_tree_view.setModel(self.json_model)

        self.button1 = QPushButton('Import script')
        self.button1.clicked.connect(self.get_text_file)

        self.grid_layout.addWidget(self.button1,0,0)


        self.setLayout(self.grid_layout)


    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec_():
            file_name = dialog.selectedFiles()
            if file_name[0].endswith(('.json','.JSON')):
                with open(file_name[0]) as json_file:  # Opens any file in the JSON format / Abre el JSON file y lo guarda como 'json_file'
                    document = json.load(json_file)
                    self.json_model.load(document)
                    self.grid_layout.addWidget(self.json_tree_view, 1, 0)
                    json_file.close()
                    # text.close()  # closing the txt file
            else:
                pass

#  if __name__=='__main__':
#     app = QApplication(sys.argv)
#     demo = DialogApp()
#     demo.show()
#     sys.exit(app.exec_())