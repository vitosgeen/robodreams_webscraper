import sqlite3

database_name = 'quotes.db'

def setup_database():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    # Create table authors if it does not exist (id, name)
    c.execute('''CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT)''')
    # Create table quotes if it does not exist (id, text, author_id)
    c.execute('''CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, text TEXT, author_id INTEGER, FOREIGN KEY(author_id) REFERENCES authors(id))''')
    # Create table tags if it does not exist (id, name)
    c.execute('''CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY KEY, name TEXT)''')
    # Create table quotes_tags if it does not exist (quote_id, tag_id)  
    c.execute('''CREATE TABLE IF NOT EXISTS quotes_tags (quote_id INTEGER, tag_id INTEGER, FOREIGN KEY(quote_id) REFERENCES quotes(id), FOREIGN KEY(tag_id) REFERENCES tags(id))''')
    conn.commit()
    conn.close()