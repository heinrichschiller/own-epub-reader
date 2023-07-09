# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from sources.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow(app)
    mainwindow.show()
    sys.exit(app.exec())
