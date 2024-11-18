
import download
import bs_parser
import json_custom
import sqlite_custom

URL_BBC_SPORT = 'https://www.bbc.com/sport'

if __name__ == '__main__':
    html = download.download_file(URL_BBC_SPORT)
    if html is None:
        print("Error downloading file")
        exit(1)

    links_titles = bs_parser.parser_links_bbs_sport(html, 5)
    print("--------links_titles---------")
    print(links_titles)

    links_titles_topics = []
    for link in links_titles:
        html = download.download_file(link['link'])
        if html is None:
            print("Error downloading file")
            continue

        topics = bs_parser.parser_topics_bbs_sport_article(html)
        print("--------topics---------")
        print(topics)

        links_titles_topics.append({"title": link['title'], "link": link['link'], "topics": topics})
        

    print("--------links_titles_topics---------")
    print(links_titles_topics)
    
    json_custom.save_data(links_titles_topics)
    data = json_custom.load_data()
    # print(data)

    # create the table links_data in SQLite database
    sqlite_custom.create_table_links_data()

    # save the links and titles to SQLite database
    sqlite_custom.save_links_titles_db(links_titles_topics)
    
    # save the topics to SQLite database 
    sqlite_custom.save_topics_db(links_titles_topics)