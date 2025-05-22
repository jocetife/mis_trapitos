import ui_inicio
import sys
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

if __name__ == "__main__":
    app = QApplication(sys.argv)
    inicio = ui_inicio.inicio()
    inicio.show()
    sys.exit(app.exec())