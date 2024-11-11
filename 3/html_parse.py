import download
import xml.etree.ElementTree as ET

from lxml import etree

def parse_html_xpath(url):
    html = download.download_file(url)
    if html is None:
        return None    
    
    # parse html
    try:
        data_tree = etree.HTML(html)
    except Exception as e:
        print("Error etree.HTML")
        return None
    
    # find input field search
    search_element_what = data_tree.xpath('//input[@id="text-input-what"]')
    if not search_element_what:
        print("search_element_what not found")

    # find input field search by region
    search_element_where = data_tree.xpath('//input[@id="text-input-where"]')
    if not search_element_where:
        print("search_element_where not found")

    # find search button form#jobsearch button[type="submit"]
    search_button = data_tree.xpath('//form[@id="jobsearch"]//button[@type="submit"]')
    if not search_button:
        print("search_button not found")

    print(search_element_what)
    print(search_element_where)
    print(search_button)