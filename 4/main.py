import re
from bs4 import BeautifulSoup
import download

# Extract all titles from the html
def extract_titles_by_regex(html):
    titles = re.findall(r'<div class="job_secteur_title">(.*?)</div>', html, re.DOTALL)
    # Remove html tags
    titles = [re.sub(r'<.*?>', '', title) for title in titles]
    return titles

def extract_links_by_regex(html):
    links = re.findall(r'<a href="(.*?)" title="(.*?)" class="jobCard_link"', html)
    # get only the first element of the tuple (the link)
    links = [link[0] for link in links]    
    return links

def extract_links_titles_by_regex(html):
    links_titles = re.findall(r'<a href="(.*?)" title="(.*?)" class="jobCard_link"', html)
    return links_titles

def extract_links_titles_by_bs4(html):
    soup = BeautifulSoup(html, 'html.parser')
    hrefs = soup.find_all('a', class_='jobCard_link')
    links_titles = []
    for href in hrefs:
        title = href.find('div', class_ = "job_secteur_title").text
        link = href['href']
        links_titles.append((link, title))
    return links_titles

if __name__ == '__main__':
    url = 'https://www.lejobadequat.com/emplois'
    html = download.download_file(url)
    if html is None:
        print("Error downloading file")
        exit(1)
    
    titles = extract_titles_by_regex(html)
    links = extract_links_by_regex(html)
    
    links_titles = zip(links, titles)
    for link, title in links_titles:
        print(f"{title} -> {link}")

    links_titles = extract_links_titles_by_regex(html)
    for link, title in links_titles:
        print(f"{title} -> {link}")

    links_titles = extract_links_titles_by_bs4(html)
    for link, title in links_titles:
        print(f"{title} -> {link}")
