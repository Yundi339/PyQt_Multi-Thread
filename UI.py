try:
    from PyQt6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PyQt5 import QtCore, QtGui, QtWidgets


class UI_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UI_MainWindow, self).__init__(parent)
        self.setupUi()
        self.qss()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(350, 450)
        self.setMinimumSize(QtCore.QSize(320, 0))
        self.setMaximumSize(QtCore.QSize(800, 16777215))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(305, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(305, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(300, 80))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.widget)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("PyQt_Multi-Thread")

        self.label.setText("输出")

        self.pushButton.setText("连续生产10次")
        self.pushButton_2.setText("连续消费10次")
        self.pushButton_3.setText("生产1次")
        self.pushButton_4.setText("消费1次")

        self.textEdit.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

    def qss(self):
        self.widget.setStyleSheet('''
            QPushButton{
                font-size:12px;
            }
        ''')
        self.centralwidget.setStyleSheet('''
            QLabel{
                font-size:11px;
            }
        ''')

# if __name__ == '__main__':
#     import sys
#     from PyQt5.QtCore import QCoreApplication, Qt
#     from PyQt5 import QtWidgets
#     QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
#     app = QtWidgets.QApplication(sys.argv)
#     gui = UI_MainWindow()
#     gui.show()
#     sys.exit(app.exec())
