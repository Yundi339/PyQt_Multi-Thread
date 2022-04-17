#  -*- coding: UTF-8 -*

try:
    from PyQt6 import  QtWidgets
    from PyQt6.QtCore import Qt
    # close high Dpi scale
    # from PyQt6.QtGui import QGuiApplication
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor);
except ImportError:
    from PyQt5 import  QtWidgets
    from PyQt5.QtCore import QCoreApplication, Qt
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

import sys
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec())
