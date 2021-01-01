from PyQt5 import QtCore, QtGui, QtWidgets


class CheckBoxStyle(QtWidgets.QProxyStyle):
    def subElementRect(self, element, option, widget=None):
        r = super().subElementRect(element, option, widget)
        if element == QtWidgets.QStyle.SE_ItemViewItemCheckIndicator:
            r.moveCenter(option.rect.center())
        return r


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        data = ["1", "2", "3", "4", "5", "6"]

        self.tableWidget = QtWidgets.QTableWidget(0, 2)
        self.setCentralWidget(self.tableWidget)

        for text in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            text_item = QtWidgets.QTableWidgetItem(text)

            checkbox_item = QtWidgets.QTableWidgetItem()
            checkbox_item.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
            )
            checkbox_item.setCheckState(QtCore.Qt.Unchecked)

            self.tableWidget.setItem(row, 0, text_item)
            self.tableWidget.setItem(row, 1, checkbox_item)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    myStyle = CheckBoxStyle('Fusion')
    app.setStyle(myStyle)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())