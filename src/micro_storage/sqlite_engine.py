from . import StorageEngineInterface
import sqlite3
import json


class SQLiteEngine(StorageEngineInterface):
    table_name = 'storage'

    def __init__(self, db_file='app_storage.db'):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.init()

    def init(self):
        res = self.conn.execute("SELECT name FROM sqlite_schema where type='table' and name = ?", (self.table_name,))
        if res.fetchone() is None:
            self.conn.execute("CREATE TABLE "+self.table_name+" (name, value, serialized)")

    def set(self, key, value):
        with self.conn:
            res = self.conn.execute("SELECT * FROM " + self.table_name + " where name = ?", (key,))
            data = res.fetchone()

        serialized = False
        if type(value) is dict or type(value) is list:
            serialized = True
            value = json.dumps(value).encode('utf8')

        if data is None:
            with self.conn:
                self.conn.execute("INSERT INTO " + self.table_name + " VALUES(?,?,?)", (key, value, serialized))
        else:
            with self.conn:
                self.conn.execute("UPDATE " + self.table_name + " set value = ? ,serialized = ? where name = ?", (value, serialized, key))

    def get(self, key):
        res = self.conn.execute("SELECT * FROM "+self.table_name+" where name = ?", (key,))
        data = res.fetchone()
        if data is None:
            return None
        if data[2]:
            value = json.loads(data[1].decode('utf8'))
            return value

        return data[1]

    def exists(self, key):
        res = self.conn.execute("SELECT * FROM " + self.table_name + " where name = ?", (key,))

        return True if res.fetchone() else False
