import csv
import sqlite3 as lite
from os.path import dirname, abspath
import os

class DB(object):
    def __init__(self, dst_path, dbname):
        self.DB_Name = dst_path + '/' + dbname
        if not os.path.exists(self.DB_Name):
            open(self.DB_Name, 'w')
        self.setupDBCon()

    def setupDBCon(self):
        self.con = lite.connect(self.DB_Name, check_same_thread=False, isolation_level=None)
        self.cur = self.con.cursor()
        self.cur.execute("PRAGMA synchronous=OFF")
        self.cur.execute('pragma journal_mode=wal')