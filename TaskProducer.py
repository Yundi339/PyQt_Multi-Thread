try:
    from PyQt6.QtCore import pyqtSignal, QRunnable, QMutex, QThread
except ImportError:
    from PyQt5.QtCore import pyqtSignal, QRunnable, QMutex, QThread
from queue import Queue

class TaskProducer(QRunnable):
    __send_signal = pyqtSignal(str)

    def __init__(self, index: int, queen: Queue, signal1: pyqtSignal, signal2: pyqtSignal):
        super(TaskProducer, self).__init__()
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
            "Thread {} Producer{}-{} Run."
            "</font>"
            .format(int(QThread.currentThreadId()),self.__index, count))
        self.__insert_sql_signal.emit(self.__index, 'Producer', int(QThread.currentThreadId()), 'Run')

        mutex.lock()
        if self.__queen.full():
            mutex.unlock()
            self.__send_signal.emit(
                "<font color=\"#0033FF\">"
                "Thread {} Producer{}-{} Full."
                "</font>"
                .format(int(QThread.currentThreadId()),self.__index, count))
            self.__insert_sql_signal.emit(self.__index, 'Producer', int(QThread.currentThreadId()), 'Full')

        else:
            QThread.msleep(self.__delay)
            num = self.__queen.qsize() + 1
            self.__queen.put(num)
            mutex.unlock()
            self.__send_signal.emit(
                "<font color=\"#0033FF\">"
                "Thread {} Producer{}-{} Put {}."
                "</font>"
                .format(int(QThread.currentThreadId()),self.__index, count, num))
            self.__insert_sql_signal.emit(self.__index, 'Producer', int(QThread.currentThreadId()), 'Put {}'.format(num))



