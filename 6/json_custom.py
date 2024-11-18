# save the links and titles to json file
import json

FILE_PATH_JSON = './data/data.json'

def save_data(data):
    with open(FILE_PATH_JSON, 'w') as f:
        json.dump(data, f)

# load the links and titles from json file
def load_data():
    with open(FILE_PATH_JSON, 'r') as f:
        data = json.load(f)
    return data