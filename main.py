from PyQt5.QtWidgets import  QApplication

import winClas
import sys

def application():
    app = QApplication(sys.argv)
    window = winClas.Window()
    window.show()
    sys.exit(app.exec_())


application()
