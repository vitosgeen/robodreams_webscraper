
import csv
import json
import download
import regex_extractor
import csv_custom
import json_custom
import sqlite_custom
import xml_custom

URL_LEJOB = 'https://www.lejobadequat.com/emplois'

def get_links_titles(html):
    titles = regex_extractor.extract_titles_by_regex(html)
    links = regex_extractor.extract_links_by_regex(html)
    
    links_titles = []
    links_titles_zip = zip(links, titles)
    for link, title in links_titles_zip:
        links_titles.append({"title": title, "link": link})

    return links_titles

if __name__ == '__main__':
    html = download.download_file(URL_LEJOB)
    if html is None:
        print("Error downloading file")
        exit(1)
        
    links_titles = get_links_titles(html)

    json_custom.save_links_titles(links_titles)
    links_titles = json_custom.load_links_titles()
    print("--------json---------")
    print(links_titles)

    csv_custom.save_links_titles_csv(links_titles)
    links_titles = csv_custom.load_links_titles_csv()
    print("--------csv---------")
    print(links_titles)

    xml_custom.save_links_titles_xml(links_titles)
    links_titles = xml_custom.load_links_titles_xml()
    print("--------xml---------")
    print(links_titles)

    sqlite_custom.save_links_titles_db(links_titles)
    print("---------SQLite--------")
    links_titles = sqlite_custom.load_links_titles_db()
    print(links_titles)

    sqlite_custom.save_links_titles_sqlalchemy(links_titles)
    print("---------SQLite SQLAlchemy--------")
    links_titles = sqlite_custom.load_links_titles_sqlalchemy()
    print(links_titles)