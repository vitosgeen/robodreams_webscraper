import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, Boolean, func
from sqlalchemy.orm import sessionmaker, declarative_base

FILE_PATH_DB = './data/links_titles.db'
FILE_PATH_SQLALCHEMY_DB = './data/links_titles_sqlalchemy.db'

#save the links and titles to SQLite database
def save_links_titles_db(links_titles):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links_titles
                 (title text, link text)''')
    for link_title in links_titles:
        link_title_loaded = load_link_title_by_url(link_title["link"])
        if link_title_loaded is not None:
            continue
        c.execute("INSERT INTO links_titles VALUES (?, ?)", (link_title["title"], link_title["link"]))
    conn.commit()
    conn.close()

#load the links and titles from SQLite database
def load_links_titles_db():
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('SELECT * FROM links_titles')
    links_titles = []
    for row in c.fetchall():
        links_titles.append({"title": row[0], "link": row[1]})
    conn.close()
    return links_titles
# save the links and titles to SQLite database using SQLAlchemy
def save_links_titles_sqlalchemy(links_titles):
    Base = declarative_base()
    class LinkTitle(Base):
        __tablename__ = 'links_titles'
        id = Column(Integer, primary_key=True)
        title = Column(String)
        link = Column(String)
    engine = create_engine('sqlite:///' + FILE_PATH_SQLALCHEMY_DB, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for link_title in links_titles:
        link_title_loaded = load_link_title_by_url_sqlalchemy(link_title["link"])
        if link_title_loaded is not None:
            continue
        link_title_db = LinkTitle(title=link_title["title"], link=link_title["link"])
        session.add(link_title_db)
    session.commit()
    session.close()

# load the links and titles from SQLite database using SQLAlchemy
def load_links_titles_sqlalchemy():
    Base = declarative_base()
    class LinkTitle(Base):
        __tablename__ = 'links_titles'
        id = Column(Integer, primary_key=True)
        title = Column(String)
        link = Column(String)
    engine = create_engine('sqlite:///' + FILE_PATH_SQLALCHEMY_DB, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    links_titles = []
    for link_title in session.query(LinkTitle):
        links_titles.append({"title": link_title.title, "link": link_title.link})
    session.close()
    return links_titles

# load the link title by url from SQLite database using SQLAlchemy
def load_link_title_by_url_sqlalchemy(url):
    Base = declarative_base()
    class LinkTitle(Base):
        __tablename__ = 'links_titles'
        id = Column(Integer, primary_key=True)
        title = Column(String)
        link = Column(String)
    engine = create_engine('sqlite:///' + FILE_PATH_SQLALCHEMY_DB, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    link_title = session.query(LinkTitle).filter(LinkTitle.link == url).first()
    session.close()
    if link_title is None:
        return None
    return {"title": link_title.title, "link": link_title.link}

# load the link title by url from SQLite database
def load_link_title_by_url(url):
    conn = sqlite3.connect(FILE_PATH_DB)
    c = conn.cursor()
    c.execute('SELECT * FROM links_titles WHERE link = ?', (url,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    return {"title": row[0], "link": row[1]}