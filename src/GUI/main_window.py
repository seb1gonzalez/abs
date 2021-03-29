import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ConfigurationManager import ConfMng
from Builder.Builder import Builder
from RunnerComponent import RunnerApp

class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      self.setGeometry(100, 100, 1200,800)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = QWidget()
		
      self.addTab(self.tab1,"Extractor")
      self.addTab(self.tab2,"Builder")
      self.addTab(self.tab3,"Runner")
      self.extractor_UI()
      self.builder_UI()
      self.runner_UI()
      self.setWindowTitle("Agent Build System")
		
   def extractor_UI(self):
       tab1_layout = QVBoxLayout()
       extractor = ConfMng(self)
       tab1_layout.addWidget(extractor)
       self.tab1.setLayout(tab1_layout)


		
   def builder_UI(self):
       tab2_layout = QVBoxLayout()
       builder = Builder(self)
       tab2_layout.addWidget(builder)
       self.tab2.setLayout(tab2_layout)

		
   def runner_UI(self):
       tab3_layout = QVBoxLayout()
       runner = RunnerApp(self)
       tab3_layout.addWidget(runner)
       self.tab3.setLayout(tab3_layout)
		
def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()