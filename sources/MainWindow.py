# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMainWindow, QFileDialog
from forms.ui_mainwindow import Ui_MainWindow
from sources.EpubReader import EpubReader


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Open_File.triggered.connect(self.open_file)
        self.ui.action_Exit.triggered.connect(self.exit_app)

    def open_file(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)

        if dialog.exec():
            file_name = dialog.selectedFiles()
            print(file_name)
            reader = EpubReader()
            self.ui.textBrowser.setHtml(reader.read_epub(file_name[0]))

    def exit_app(self):
        self.app.quit()
