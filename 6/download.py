
import hashlib
import os
import requests


def download_file(url):
    #get hash of url
    hash = hashlib.md5(url.encode()).hexdigest()
    
    # check if file exists
    if os.path.exists(f'./downloads/{hash}'):
        return read_file(f'./downloads/{hash}')
    
    # create dir
    create_dir()
    
    # download file
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return None
    # check if response is ok
    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        return None
    
    # save file
    try:
        with open(f'./downloads/{hash}', 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(e)
        return None

    return read_file(f'./downloads/{hash}')

def create_dir():
    try:
        if not os.path.exists('./downloads'):
            os.makedirs('./downloads')
    except Exception as e:
        print(e)

def read_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            return content
    except Exception as e:
        print(e)
        return None
