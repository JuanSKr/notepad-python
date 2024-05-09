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

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        with open(resource_path('resources/styles/style.qss'), 'r') as f:
            self.setStyleSheet(f.read())
        self.setWindowTitle("Smooth Notepad")
        self.setMinimumSize(500, 400)

        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")

        ruta_abrir = os.path.join(os.path.dirname(__file__), "resources/img/open.png")
        ruta_guardar = os.path.join(os.path.dirname(__file__), "resources/img/save.png")
        ruta_guardar_como = os.path.join(os.path.dirname(__file__), "resources/img/save_as.png")
        ruta_salir = os.path.join(os.path.dirname(__file__), "resources/img/leave.png")

        self.ruta = ""

        abrir_archivo = QAction(QIcon(ruta_abrir), "&Open file", self)
        abrir_archivo.setWhatsThis("Open a text file.")
        abrir_archivo.setStatusTip("Open a  text file.")
        abrir_archivo.setShortcut(QKeySequence("Ctrl+Q"))
        abrir_archivo.triggered.connect(self.abrir_archivo)
        menu.addAction(abrir_archivo)

        guardar_archivo = QAction(QIcon(ruta_guardar), "&Save file", self)
        guardar_archivo.setWhatsThis("Save the file in the same path.")
        guardar_archivo.setStatusTip("Save the file in the same path.")
        guardar_archivo.setShortcut(QKeySequence("Ctrl+O"))
        guardar_archivo.triggered.connect(self.guardar_archivo)
        menu.addAction(guardar_archivo)

        guardar_como = QAction(QIcon(ruta_guardar_como), "&Save as...", self)
        guardar_como.setWhatsThis("Save the file in a path choosen by yourself.")
        guardar_como.setStatusTip("Save the file in a path choose by yourself.")
        guardar_como.setShortcut(QKeySequence("Ctrl+G"))
        guardar_como.triggered.connect(self.guardar_como)
        menu.addAction(guardar_como)

        cerrar_programa = QAction(QIcon(ruta_salir), "&Close the program", self)
        cerrar_programa.setWhatsThis("Close the program.")
        cerrar_programa.setStatusTip("Close the program.")
        cerrar_programa.setShortcut(QKeySequence("Ctrl+S"))
        cerrar_programa.triggered.connect(self.cerrar_programa)
        menu.addAction(cerrar_programa)

        self.statusBar()

        barra_herramientas = QToolBar("Tools Bar")
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_herramientas.addAction(abrir_archivo)
        barra_herramientas.addAction(guardar_archivo)
        barra_herramientas.addAction(guardar_como)
        self.addToolBar(barra_herramientas)

        self.texto_dock = QTextEdit("")
        self.dock1 = QDockWidget()
        self.dock1.setWindowTitle(self.dock_title())
        self.dock1.setWidget(self.texto_dock)
        self.dock1.setMinimumWidth(50)

        self.addDockWidget(Qt.TopDockWidgetArea, self.dock1)

    def guardar_como(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")

        if ruta:
            self.ruta = ruta
            archivo = open(self.ruta, "w")
            archivo.write(self.texto_dock.toPlainText())
            archivo.close()

    def guardar_archivo(self):
        if self.ruta:
            with open(self.ruta, 'w') as file:
                file.write(self.texto_dock.toPlainText())
        else:

            file_name = 'textfile.txt'
            with open(file_name, 'w') as file:
                file.write(self.texto_dock.toPlainText())

    def abrir_archivo(self):
        nueva_ruta, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")

        if nueva_ruta:
            self.ruta = nueva_ruta
            archivo = open(self.ruta, "r")
            self.texto_dock.setText(archivo.read())
            archivo.close()
            self.dock_title()

    def dock_title(self):
        nombre_txt = self.obtener_nombre_txt()
        if self.ruta == "":
            return "New Document"
        else:
            self.dock1.setWindowTitle(nombre_txt)

    def obtener_nombre_txt(self):
        nombre_txt = self.ruta.split("/")[-1]
        return nombre_txt

    def cerrar_programa(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
