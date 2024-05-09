import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QDockWidget, QTextEdit, QFileDialog
)


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        with open(resource_path('resources/styles/style.qss'), 'r') as f:
            self.setStyleSheet(f.read())
        self.setWindowTitle("Smooth Notepad")
        self.setMinimumSize(500, 400)

        tool_bar = self.menuBar()
        menu = tool_bar.addMenu("&Menu")

        img_paths ={
            "open": os.path.join(os.path.dirname(__file__), "resources/img/open.png"),
            "save": os.path.join(os.path.dirname(__file__), "resources/img/save.png"),
            "save_as": os.path.join(os.path.dirname(__file__), "resources/img/save_as.png"),
            "close": os.path.join(os.path.dirname(__file__), "resources/img/leave.png")
        }

        self.path = ""

        open_file = QAction(QIcon(img_paths["open"]), "&Open file", self)
        open_file.setWhatsThis("Open a text file.")
        open_file.setStatusTip("Open a  text file.")
        open_file.setShortcut(QKeySequence("Ctrl+Q"))
        open_file.triggered.connect(self.open_file_def)
        menu.addAction(open_file)

        save_file = QAction(QIcon(img_paths["save"]), "&Save file", self)
        save_file.setWhatsThis("Save the file in the same path.")
        save_file.setStatusTip("Save the file in the same path.")
        save_file.setShortcut(QKeySequence("Ctrl+O"))
        save_file.triggered.connect(self.save_def)
        menu.addAction(save_file)

        save_as = QAction(QIcon(img_paths["save_as"]), "&Save as...", self)
        save_as.setWhatsThis("Save the file in a path chosen by yourself.")
        save_as.setStatusTip("Save the file in a path chosen by yourself.")
        save_as.setShortcut(QKeySequence("Ctrl+G"))
        save_as.triggered.connect(self.save_as_def)
        menu.addAction(save_as)

        close_program = QAction(QIcon(img_paths["close"]), "&Close the program", self)
        close_program.setWhatsThis("Close the program.")
        close_program.setStatusTip("Close the program.")
        close_program.setShortcut(QKeySequence("Ctrl+S"))
        close_program.triggered.connect(self.close_program_def)
        menu.addAction(close_program)

        self.statusBar()

        toolbar = QToolBar("Tools Bar")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolbar.addAction(open_file)
        toolbar.addAction(save_file)
        toolbar.addAction(save_as)
        self.addToolBar(toolbar)

        self.dock_text = QTextEdit("")
        self.dock1 = QDockWidget()
        self.dock1.setWindowTitle(self.dock_title())
        self.dock1.setWidget(self.dock_text)
        self.dock1.setMinimumWidth(50)

        self.addDockWidget(Qt.TopDockWidgetArea, self.dock1)

    def save_as_def(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")

        if path:
            self.path = path
            file = open(self.path, "w")
            file.write(self.dock_text.toPlainText())
            file.close()

    def save_def(self):
        if self.path:
            with open(self.path, 'w') as file:
                file.write(self.dock_text.toPlainText())
        else:

            file_name = 'textfile.txt'
            with open(file_name, 'w') as file:
                file.write(self.dock_text.toPlainText())

    def open_file_def(self):
        new_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")

        if new_path:
            self.path = new_path
            file = open(self.path, "r")
            self.dock_text.setText(file.read())
            file.close()
            self.dock_title()

    def dock_title(self):
        name_txt = self.get_name_txt()
        if self.path == "":
            return "New Document"
        else:
            self.dock1.setWindowTitle(name_txt)

    def get_name_txt(self):
        name_txt = self.path.split("/")[-1]
        return name_txt

    def close_program_def(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
