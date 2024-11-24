
import sqlite3


database_name = 'jobs.db'

class JobsDB:
    def __init__(self):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.setup_database()
    
    def setup_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, title TEXT, url TEXT)''')
        self.connection.commit()
    
    def insert(self, title, url):
        self.cursor.execute("INSERT INTO jobs (title, url) VALUES (?, ?)", (title, url))
        self.connection.commit()
    
    def close(self):
        self.connection.close()

    def get_by_url(self, url):
        self.cursor.execute("SELECT * FROM jobs WHERE url = ?", (url,))
        return self.cursor.fetchone()
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM jobs")
        return self.cursor.fetchall()

    
