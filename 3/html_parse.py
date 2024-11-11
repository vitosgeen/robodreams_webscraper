import download
import xml.etree.ElementTree as ET

from lxml import etree

def parse_html_xpath(url):
    page = download.download_file(url)
    if page is None:
        return None
    
    # parse html
    try:
        data = ET.parse(page)
    except Exception as e:
        print("Error etree.parse")
        return None
    
    # find input field search
    search_element_what = data.xpath('//input[@id="text-input-what"]')

    # find input field search by region
    search_element_where = data.xpath('//input[@id="text-input-where"]')

    # find search button form#jobsearch button[type="submit"]
    search_button = data.xpath('//form[@id="jobsearch"]//button[@type="submit"]')

    print(search_element_what)
    print(search_element_where)
    print(search_button)