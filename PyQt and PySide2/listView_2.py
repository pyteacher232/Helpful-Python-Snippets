from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QListWidget"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox= QVBoxLayout()
        self.list = QListWidget()
        self.list.insertItem(0, "Python")
        self.list.insertItem(1, "Java")
        self.list.insertItem(2, "C++")
        self.list.insertItem(3, "C#")
        self.list.insertItem(4, "Ruby")
        self.list.insertItem(5, "Kotlin")
        self.list.clicked.connect(self.listview_clicked)
        vbox.addWidget(self.list)
        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()
    def listview_clicked(self):
        item = self.list.currentItem()
        self.label.setText(str(item.text()))
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())