from PySide2 import QtWidgets


class TestDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(TestDialog, self).__init__(*args, **kwargs)

        main_layout = QtWidgets.QHBoxLayout(self)

        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)

        w1 = QtWidgets.QPushButton("small")
        w2 = QtWidgets.QPushButton("large")
        w1.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        w2.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )

        main_layout.addWidget(w1, stretch=1)
        main_layout.addWidget(w2, stretch=2)

        self.setMinimumSize(450, 100)
        self.resize(450, 100)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test = TestDialog()
    test.show()
    sys.exit(app.exec_())