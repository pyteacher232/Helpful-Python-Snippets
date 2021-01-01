from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbwMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tbwMain.setGeometry(QtCore.QRect(0, 0, 801, 451))
        self.tbwMain.setObjectName("tbwMain")
        self.tabBoxes = QtWidgets.QWidget()
        self.tabBoxes.setObjectName("tabBoxes")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabBoxes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(220, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.tblBoxes = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tblBoxes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tblBoxes.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblBoxes.setRowCount(1)
        self.tblBoxes.setObjectName("tblBoxes")
        self.tblBoxes.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tblBoxes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBoxes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBoxes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tblBoxes.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tblBoxes.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tblBoxes.setItem(0, 2, item)
        self.tblBoxes.horizontalHeader().setStretchLastSection(True)
        self.tblBoxes.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tblBoxes)
        spacerItem1 = QtWidgets.QSpacerItem(220, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.tbwMain.addTab(self.tabBoxes, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tbwMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        # - - - - -
        # self.tblBoxes.cellActivated.connect(self.test1)
        # self.tblBoxes.cellChanged.connect(self.test2)

        self.delegate = ItemDelegate(MainWindow)
        self.delegate.cellEditingStarted.connect(self.test1)
        self.tblBoxes.setItemDelegate(self.delegate)
        self.tblBoxes.cellActivated.connect(self.test2)

    def test1(self):
        print('Start cell edit!')
    def test2(self):
        print('End cell edit!')

class ItemDelegate(QtWidgets.QStyledItemDelegate):
    cellEditingStarted = QtCore.pyqtSignal(int, int)

    def createEditor(self, parent, option, index):
        result = super(ItemDelegate, self).createEditor(parent, option, index)
        if result:
            self.cellEditingStarted.emit(index.row(), index.column())
        return result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())