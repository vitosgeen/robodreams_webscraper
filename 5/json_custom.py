# save the links and titles to json file
import json

FILE_PATH_JSON = './data/links_titles.json'

def save_links_titles(links_titles):
    with open(FILE_PATH_JSON, 'w') as f:
        json.dump(links_titles, f)

# load the links and titles from json file
def load_links_titles():
    with open(FILE_PATH_JSON, 'r') as f:
        links_titles = json.load(f)
    return links_titles