
from bs4 import BeautifulSoup

# Parser for BBC News Sport
# output: list of dictionaries with keys 'title' and 'link' and related topics
def parser_links_bbs_sport(html, limit_links=5):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('ul.e12imr580 li.e1gp961v0 .eqfxz1e5 .e1y4nx260 a.exn3ah91')
    links_titles = []
    for link in links:
        if link['href'].startswith('http'):
            links_titles.append({"title": link.text, "link": link['href']})
        else:
            links_titles.append({"title": link.text, "link": 'https://www.bbc.com' + link['href']})
        if len(links_titles) >= limit_links:
            break

    return links_titles

def parser_topics_bbs_sport_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.select('.ed0g1kj1 a.ed0g1kj0')
    topics = []
    for t in link:
        topics.append(t.text)

    return topics