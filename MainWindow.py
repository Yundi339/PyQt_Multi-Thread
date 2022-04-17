from UI import UI_MainWindow
from ThreadManage import Manage
try:
    from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot
    from PyQt6.QtWidgets import QMessageBox
except ImportError:
    from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
    from PyQt5.QtWidgets import QMessageBox

class MainWindow(UI_MainWindow):
    __quit_signal = pyqtSignal()
    __add_multiple_signal = pyqtSignal(str)
    __add_simple_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton3_clicked)
        self.pushButton_4.clicked.connect(self.pushButton4_clicked)

        self.manage_thread = QThread()
        self.manage_object = Manage()
        self.manage_object.moveToThread(self.manage_thread)
        self.manage_thread.started.connect(self.manage_object.run)
        self.manage_thread.finished.connect(self.manage_object.deleteLater)

        self.manage_object._send_signal.connect(self.manage_receive)
        self.__quit_signal.connect(self.manage_object.quit)
        self.__add_multiple_signal.connect(self.manage_object.add_multiple)
        self.__add_simple_signal.connect(self.manage_object.add_simple)

        self.manage_thread.start()


    def pushButton_clicked(self):
        self.__add_multiple_signal.emit('Producer')

    def pushButton2_clicked(self):
        self.__add_multiple_signal.emit('Consumer')

    def pushButton3_clicked(self):
        self.__add_simple_signal.emit('Producer')

    def pushButton4_clicked(self):
        self.__add_simple_signal.emit('Consumer')


    @pyqtSlot(str)
    def manage_receive(self, text: str):
        self.textEdit.append(text)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Warning', '是否要退出程序？')
        if reply == QMessageBox.StandardButton.Yes:
            try:
                if self.manage_thread.isRunning():
                    self.manage_object.quit()
                    self.manage_thread.quit()
                    self.manage_thread.wait()
                if self.manage_thread.isFinished():
                    del self.manage_object
                    del self.manage_thread
                else:
                    print('Thread quit error')
            except:
                print('Error')
            finally:
                super(MainWindow, self).closeEvent(event)
                # event.accept()
                # sys.exit(0)
        else:
            event.ignore()

