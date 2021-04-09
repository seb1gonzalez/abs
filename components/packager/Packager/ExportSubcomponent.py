import json

from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QLabel

class ExportManager(QWidget):
    def __init__(self):
        super().__init__()
        global list2
        list2 = []
        self.setWindowTitle("Export")
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(25, 25, 150, 50)
        self.pbar2 = QProgressBar(self)
        self.pbar2.setGeometry(25, 85, 150, 50)
        self.pushButton = QPushButton("Choose File", self)
        self.pushButton.move(200, 92)
        self.pushButton2 = QPushButton("ZIP File", self)
        self.pushButton2.move(200, 32)
        self.label2 = QLabel("", self)
        self.label2.setFixedWidth(10000)
        self.label2.move(30, 150)
        self.pushButton.clicked.connect(self.actionButton2)
        self.pushButton2.clicked.connect(self.actionButton)

    def actionButton(self):
        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)

        fileData = json.dumps(dataFile2, indent=2).encode("utf-8")
        print(fileData)
        output = gzip.open("test.json.gz", "wb")
        output.write(fileData)
        output.close()

    def actionButton2(self):
        file_chosen = JFileDialog().json_dialog()
        for i in range(101):
            time.sleep(0.05)
            self.pbar2.setValue(i)
        head, name = ntpath.split(file_chosen)
        list2.append(name)
        if substring in name:
            with open(file_chosen) as f:
                data = json.load(f)
                dataFile2.append(data)
        else:
            data2 = open(file_chosen, "r")
            dataFile2.append(data2.read())
        temp = " ".join(list2)
        self.label2.setText(temp)