import sys
import os
import json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget,  QGridLayout, QLabel, QListView, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import *

current_folder = os.path.dirname(os.path.realpath(__file__))
load_icon = os.path.join(current_folder, 'icon_load.png')

class loaderDialog(QWidget):
    def __init__(self, parent=None):
        super(loaderDialog, self).__init__(parent)
        self.initUI()


    def get_values_dict(self):
        """Getting data of unique values using in tables
        and making a dict of mappings for specific table
        Operation can take a long time
        """

        script_folder = current_folder
        file_local = os.path.join(script_folder, 'attributes.json')

        with open(file_local, 'r', encoding='utf-8') as fp:
            data = json.load(fp)

        return data


    def initUI(self):
        """Set GUI and get all data for launching
        """

        self.setWindowTitle('Layer loader')
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setGeometry(500, 500, 400, 520)

        self.listView = QTreeWidget()
        self.listView.setHeaderLabel('Layers')

        self.setLayout(self.grid)
        self.grid.addWidget(self.listView, 0, 1, 1, 2)

        self.case_strings = self.get_values_dict()
        self.load_data_to_tree(self.case_strings)

        self.show()


    def loading_fig(self):
        """Animation of rotating wheel
        """

        self.spin_wheel_init = QLabel()
        self.spin_wheel_init.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_wheel_init.setPixmap(QPixmap(load_icon))
        self.grid.addWidget(self.spin_wheel_init, 0, 1, 1, 2)
        angle = 0

        while True:
            tr = QTransform().rotate(angle)
            angle = angle + 1 if angle<360 else 0
            self.spin_wheel_init.setPixmap(QPixmap(load_icon).transformed(tr))
            time.sleep(0.001)
            QtCore.QCoreApplication.processEvents()


    def load_data_to_tree(self, data):
        """Giving keys to treeview
        """
        for name in data:
            child = QTreeWidgetItem(self.listView)
            child.setFlags(child.flags() | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable)
            child.setText(0, name)
            child.setCheckState(0, Qt.Unchecked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = loaderDialog()
    w.show()
    sys.exit(app.exec_())