#save the links and titles to csv file
import csv

FILE_PATH_CSV = './data/links_titles.csv'

def save_links_titles_csv(links_titles):
    with open(FILE_PATH_CSV, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Link"])
        for link_title in links_titles:
            writer.writerow([link_title["title"], link_title["link"]])

#load the links and titles from csv file
def load_links_titles_csv():
    with open(FILE_PATH_CSV, 'r') as f:
        reader = csv.reader(f)
        links_titles = []
        next(reader)
        for row in reader:
            links_titles.append({"title": row[0], "link": row[1]})
    return links_titles