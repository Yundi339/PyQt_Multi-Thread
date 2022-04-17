try:
    from PyQt6.QtCore import QObject, pyqtSlot, QThreadPool, pyqtSignal
except ImportError:
    from PyQt5.QtCore import QObject, pyqtSlot, QThreadPool, pyqtSignal

from queue import Queue
from TaskProducer import TaskProducer
from TaskConsumer import TaskConsumer


class Manage(QObject):
    _send_signal = pyqtSignal(str)
    def __init__(self):
        super(Manage, self).__init__()
        self.queue = Queue(maxsize=6)
        self.index = 0
        self.ProducerQueen = []
        self.ConsumerQueen = []

    @pyqtSlot()
    def run(self):
        TID = int(self.thread().currentThreadId())
        self._send_signal.emit(
            "<font color=\"#000000\">"
                "Manage Thread {} start."
            "</font>"
           .format(TID))
        self.ProducerPool = QThreadPool()
        self.ConsumerPool = QThreadPool()

        self.ProducerPool.setMaxThreadCount(5)
        self.ConsumerPool.setMaxThreadCount(5)

    @pyqtSlot(str)
    def create_task(self, task_type):
        if task_type == 'Producer':
            self.index += 1
            task = TaskProducer(self.index, self.queue, self._send_signal)
            self.ProducerQueen.append(task)
        else:
            self.index += 1
            task = TaskConsumer(self.index, self.queue, self._send_signal)
            self.ConsumerQueen.append(task)
        return task

    @pyqtSlot(str)
    def add_simple(self, task_type:str):
        TID = int(self.thread().currentThreadId())
        self._send_signal.emit(
            "<font color=\"#000000\">"
                "Manage Thread {} add simple."
            "</font>"
            .format(TID))
        task = self.create_task(task_type)
        task.setAutoDelete(True)
        if task_type == 'Producer':
            self.ProducerPool.start(task)
        else:
            self.ConsumerPool.start(task)

    @pyqtSlot(str)
    def add_multiple(self, task_type:str):
        TID = int(self.thread().currentThreadId())
        self._send_signal.emit(
            "<font color=\"#000000\">"
                "Manage Thread {} add multiple."
            "</font>"
            .format(TID))
        for _ in range(10):
            task = self.create_task(task_type)
            task.setAutoDelete(True)
            if task_type == 'Producer':
                self.ProducerPool.start(task)
            else:
                self.ConsumerPool.start(task)


    @pyqtSlot()
    def quit(self):
        # Removes the Runnables that are not yet started from the queue.
        self.ProducerPool.clear()
        self.ConsumerPool.clear()

    def __del__(self):
        self.quit()
        del self.queue
        del self.ProducerQueen
        del self.ConsumerQueen



