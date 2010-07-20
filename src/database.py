
import sqlite3
import os


class Database:
    def __init__(self):
        self.DB_PATH = os.path.join(os.environ['HOME'],'.dmeterdb')
        if not os.path.exists(self.DB_PATH):
            self.create_db()

        self.conn = sqlite3.connect(self.DB_PATH)

    def create_db(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute('''
            create table if not exists intervals 
            (start text, end text, idle integer, app text);
        ''')
        conn.commit()
        c.close()

    def add_interval(self, start, end, isIdle, appname):
        c = self.conn.cursor()
        c.execute('''
            insert into intervals values
            ('%s','%s',%d,'%s')
        '''%(start, end, isIdle, appname))
        self.conn.commit()
        c.close()

