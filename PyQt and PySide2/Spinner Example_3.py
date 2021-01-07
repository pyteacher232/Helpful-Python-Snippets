import PyQt5.QtWidgets as QWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from waitingspinnerwidget import QtWaitingSpinner
import sys

class Example_Window(QWidgets.QWidget):
    def __init__(self):
        super(QWidgets.QWidget,self).__init__()

        self.initUI()

    def initUI(self):
        self.button = QWidgets.QPushButton("Start Spinner") # +
        self.button.clicked.connect(self.toggle_spinner)

        self.spinner = QtWaitingSpinner(self, centerOnParent=False)

        self.grid = QWidgets.QGridLayout()
        self.grid.addWidget(self.button, 0, 0)

#        self.grid.addWidget(self.spinner,0,1)        # ---
        self.grid.addWidget(self.spinner, 0, 1, 1, 2) # +++    <---

        self.setLayout(self.grid)
        self.show()

    def toggle_spinner(self):
        if self.spinner.isSpinning():
            self.spinner.stop()
            self.button.setText("Start Spinner") # +
        else:
            self.spinner.start()
            self.button.setText("Stop Spinner")  # +

if __name__ == '__main__':
    app = QWidgets.QApplication([])
    main = Example_Window()
    main.resize(170, 70)                               # +++
    sys.exit(app.exec())