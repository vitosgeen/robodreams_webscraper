
# Extract all titles from the html
import re


def extract_titles_by_regex(html):
    titles = re.findall(r'<h3 class="jobCard_title.*?">(.*?)</h3>', html, re.DOTALL)
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
    # format the result more readable
    links_titles = [{"title": link[1], "link": link[0]} for link in links_titles]
    return links_titles