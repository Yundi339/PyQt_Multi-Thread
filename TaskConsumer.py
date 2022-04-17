try:
    from PyQt6.QtCore import pyqtSignal, QRunnable, QMutex, QThread
except ImportError:
    from PyQt5.QtCore import pyqtSignal, QRunnable, QMutex, QThread
from queue import Queue


class TaskConsumer(QRunnable):
    __send_signal = pyqtSignal(str)

    def __init__(self, index: int, queen: Queue, signal1: pyqtSignal, signal2: pyqtSignal):
        super(TaskConsumer, self).__init__()
        self.__send_signal = signal1
        self.__insert_sql_signal = signal2
        self.__queen = queen
        self.__count = 0
        self.__index = index
        self.__delay = 500

    def run(self):
        mutex = QMutex()
        mutex.lock()
        self.__count += 1
        count = self.__count
        mutex.unlock()
        self.__send_signal.emit(
            "<font color=\"#000000\">"
            "Thread {} Consumer{}-{} Run."
            "</font>"
                .format(int(QThread.currentThreadId()), self.__index, count))
        self.__insert_sql_signal.emit(self.__index, 'Consumer', int(QThread.currentThreadId()), 'Run')
        QThread.msleep(self.__delay)
        mutex.lock()
        if self.__queen.empty():
            mutex.unlock()
            self.__send_signal.emit(
                "<font color=\"#FF0000\">"
                "Thread {} Consumer{}-{} Empty."
                "</font>"
                    .format(int(QThread.currentThreadId()), self.__index, count))
            self.__insert_sql_signal.emit(self.__index, 'Consumer', int(QThread.currentThreadId()), 'Empty')

        else:
            num = self.__queen.get()
            mutex.unlock()
            self.__send_signal.emit(
                "<font color=\"#FF0000\">"
                "Thread {} Consumer{}-{} Get {}."
                "</font>"
                    .format(int(QThread.currentThreadId()), self.__index, count, num))
            self.__insert_sql_signal.emit(self.__index, 'Consumer', int(QThread.currentThreadId()), 'Get {}'.format(num))
