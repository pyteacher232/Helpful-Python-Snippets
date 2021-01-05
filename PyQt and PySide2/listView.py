import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    listWidget = QListWidget()
    window.setWindowTitle("Demo for QListWidget")

    QListWidgetItem("Geeks", listWidget)
    QListWidgetItem("For", listWidget)
    QListWidgetItem("Geeks", listWidget)

    listWidgetItem = QListWidgetItem("GeeksForGeeks")
    listWidget.addItem(listWidgetItem)

    window_layout = QVBoxLayout(window)
    window_layout.addWidget(listWidget)
    window.setLayout(window_layout)

    window.show()

    sys.exit(app.exec_())
