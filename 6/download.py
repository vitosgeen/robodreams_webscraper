
import hashlib
import os
import random
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
        response = requests.get(url, headers={'User-Agent': get_random_user_agent()})
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

def get_random_user_agent():
    user_agents = collection_of_user_agents()
    return user_agents[random.randint(0, len(user_agents)-1)]

def collection_of_user_agents():
    return [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    ]