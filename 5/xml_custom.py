
# save the links and titles to xml file
import xml.etree.ElementTree as ET

FILE_PATH_XML = './data/links_titles.xml'

def save_links_titles_xml(links_titles):
    root = ET.Element("links_titles")
    for link_title in links_titles:
        link_title_element = ET.SubElement(root, "link_title")
        title_element = ET.SubElement(link_title_element, "title")
        title_element.text = link_title["title"]
        link_element = ET.SubElement(link_title_element, "link")
        link_element.text = link_title["link"]
    tree = ET.ElementTree(root)
    tree.write(FILE_PATH_XML, encoding='utf-8', xml_declaration=True)

# load the links and titles from xml file
def load_links_titles_xml():
    tree = ET.parse(FILE_PATH_XML)
    root = tree.getroot()
    links_titles = []
    for link_title_element in root:
        title = link_title_element.find("title").text
        link = link_title_element.find("link").text
        links_titles.append({"title": title, "link": link})
    return links_titles