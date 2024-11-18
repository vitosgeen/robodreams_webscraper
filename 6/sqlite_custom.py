import sqlite3

FILE_PATH_DB = './data/links_data.db'

#save the links and titles to SQLite database
def save_links_titles_db(links_titles):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    for link_title in links_titles:
        link_title_loaded = load_link_title_by_url(link_title["link"])
        if link_title_loaded is not None:
            continue
        c.execute('INSERT INTO links_data (title, link) VALUES (?, ?)', (link_title["title"], link_title["link"]))
    conn.commit()
    conn.close()

# load the link title by url from SQLite database
def load_link_title_by_url(url):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('SELECT * FROM links_data WHERE link = ?', (url,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    return {"id": row[0], "title": row[1], "link": row[2]}

# save the topics to SQLite database
def save_topics_db(links_titles_topics):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    for link_title in links_titles_topics:
        link_title_loaded = load_link_title_by_url(link_title["link"])
        if link_title_loaded is None:
            continue
        for topic in link_title["topics"]:
            topic_loaded = load_topic_by_name(topic)
            if topic_loaded is None:
                c.execute('INSERT INTO topics (topic) VALUES (?)', (topic,))
                topic_id = c.lastrowid
            else:
                topic_id = topic_loaded["id"]
            
            link_topic_loaded = load_link_topic_by_ids(link_title_loaded["id"], topic_id)
            if link_topic_loaded is not None:
                continue
            c.execute('INSERT INTO links_topics (link_id, topic_id) VALUES (?, ?)', (link_title_loaded["id"], topic_id))
            conn.commit()
    conn.close()

# load the link topic by ids from SQLite database
def load_link_topic_by_ids(link_id, topic_id):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('SELECT * FROM links_topics WHERE link_id = ? AND topic_id = ?', (link_id, topic_id))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    return {"link_id": row[0], "topic_id": row[1]}

# load the topic by name from SQLite database
def load_topic_by_name(topic):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('SELECT * FROM topics WHERE topic = ?', (topic,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    return {"id": row[0], "topic": row[1]}

# create the table links_data in SQLite database
def create_table_links_data():
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links_data
                    (id integer primary key autoincrement, title text, link text)''')
    c.execute('''CREATE TABLE IF NOT EXISTS links_topics
                    (link_id integer, topic_id integer)''')
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                    (id integer primary key autoincrement, topic text)''')
    conn.commit()
    conn.close()