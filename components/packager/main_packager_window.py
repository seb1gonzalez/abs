import sys
import logging

#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout
from Packager.ImportSubcomponent import ImportManager
#from Packager.ExportSubcomponent import ExportManager

class PackagerTabWindow(QTabWidget):
   def __init__(self, parent = None):
      super(PackagerTabWindow, self).__init__(parent)
      self.setGeometry(100, 100, 1000, 500)
      self.tab1 = QWidget()
      #self.tab2 = QWidget()
		
      self.addTab(self.tab1,"Import")
      #self.addTab(self.tab2,"Export")
      self.import_UI()
      #self.export_UI()
      self.setWindowTitle("Agent Build System: Packager")
		
   def import_UI(self):
       tab1_layout = QVBoxLayout()
       import_subcomp = ImportManager(self)
       tab1_layout.addWidget(import_subcomp)
       self.tab1.setLayout(tab1_layout)
		
   """ def export_UI(self):
       tab2_layout = QVBoxLayout()
       builder = ExportManager(self)
       tab2_layout.addWidget(builder)
       self.tab2.setLayout(tab2_layout) """
		
def main():
   app = QApplication(sys.argv)
   ex = PackagerTabWindow()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()