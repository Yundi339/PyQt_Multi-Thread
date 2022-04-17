try:
    from PyQt6.QtCore import QObject, pyqtSlot
except ImportError:
    from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3
import os,time


class Sql(QObject):
    def __init__(self):
        super(Sql, self).__init__()
        self.sql_path = 'multi-thread.db'
        self.exist = os.path.exists(self.sql_path)
        self.index = 0

    @pyqtSlot()
    def run(self):
        self.sql_connect = sqlite3.connect(self.sql_path)
        if not self.exist:
            self.create_sqlite()
        print('sql open')

    def create_sqlite(self):
        # id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
        self.sql_connect.execute(
            '''
            CREATE TABLE log (
            id INTEGER,
            name TEXT,
            thread_id INTEGER,
            message TEXT
            );
            ''')
        self.sql_connect.commit()
        print('sql create')

    @pyqtSlot(int,str,int,str)
    def insert_sqlite(self, id, name, thread_id, message):
        cursor = self.sql_connect.cursor()  # 创建一个Cursor,通过Cursor执行create insert select等sql语句
        cursor.execute(
            "INSERT INTO log (id,name,thread_id,message) VALUES ({},'{}',{},'{}')"
                .format(id, name, thread_id, message))
        print("{} insert {} rows".format(time.time(),cursor.rowcount))
        cursor.close()
        self.index += 1
        if self.index > 100:
            self.sql_connect.commit()
            self.index = 0

    @pyqtSlot()
    def quit(self):
        self.sql_connect.commit()
        self.sql_connect.close()


