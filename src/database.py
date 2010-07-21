
import sqlite3
import os

class Interval:
    def __init__(self, start, end, idle, app):
        self.start = start
        self.end = end
        self.idle = idle
        self.app = app

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

    def get_intervals(self, where_clause, args=[], distinct=None):
        c = self.conn.cursor()

        if distinct is not None:
            result = c.execute('select distinct(%s) from intervals where '%distinct+where_clause, args)
            intervals = []
            for row in result:
                intervals.append(row[0])
        else:
            result = c.execute('select * from intervals where '+where_clause, args)
            intervals = []
            for row in result:
                intervals.append(Interval(row[0], row[1], row[2], row[3]))


        c.close()

        return intervals

    def count_intervals(self, where_clause, args=[]):
        c = self.conn.cursor()

        c.execute('select count(*) from intervals where '+where_clause, args)
        result = c.fetchone()
        c.close()

        return result[0]


