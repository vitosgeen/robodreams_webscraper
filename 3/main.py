import re

import html_parse


text ="""Welcome to the Regex Training Center! 

01/02/2021, 12-25-2020, 2021.03.15, 2022/04/30, 2023.06.20, and 2021.07.04. You can
also find dates with words: March 14, 2022, and December 25, 2020. 

(123) 456-7890, +1-800-555-1234, 800.555.1234, 800-555-1234, and 123.456.7890. 
Other formats include international numbers: +44 20 7946 0958, +91 98765 43210.

john.doe@example.com, jane_doe123@domain.org, support@service.net, info@company.co.uk, 
and contact.us@my-website.com. You might also find these tricky: weird.address+spam@gmail.com,
"quotes.included@funny.domain", and this.one.with.periods@weird.co.in.

http://example.com, https://secure.website.org, http://sub.domain.co, 
www.redirect.com, and ftp://ftp.downloads.com. Don't forget paths and parameters:
https://my.site.com/path/to/resource?param1=value1&param2=value2, 
http://www.files.net/files.zip, https://example.co.in/api/v1/resource, and 
https://another-site.org/downloads?query=search#anchor. 

0x1A3F, 0xBEEF, 0xDEADBEEF, 0x123456789ABCDEF, 0xA1B2C3, and 0x0. 

#FF5733, #C70039, #900C3F, #581845, #DAF7A6, and #FFC300. RGB color codes can be tricky: 
rgb(255, 99, 71), rgba(255, 99, 71, 0.5).

123-45-6789, 987-65-4321, 111-22-3333, 555-66-7777, and 999-88-7777. Note that Social 
Security numbers might also be written like 123 45 6789 or 123456789.

Let's throw in some random sentences for good measure:
- The quick brown fox jumps over the lazy dog.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- Jack and Jill went up the hill to fetch a pail of water.
- She sells seashells by the seashore.

1234567890, !@#$%^&*()_+-=[]{}|;':",./<>?, 3.14159, 42, and -273.15.
"""

def find_dates(text):
    dates_raw_data = re.findall(r'(\b(\d{4})([\/,\-,\.])\d{2}([\/,\-,\.])\d{2})|\b(([0-9]{2})([\/,\-,\.])\d{2}([\/,\-,\.])\d{4})|\b((January|February|March|April|May|June|July|August|September|October|November|December) (\d{2}), (\d{4}))\b', text)
    dates = []
    for match in dates_raw_data:
        matched_date = next(filter(None, match), None)
        if matched_date:
            dates.append(matched_date)

    return dates

def find_emails(text):
    return re.findall(r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

def find_urls(text):
    urls_raw_data = re.findall(r'(\b(ftp|http)(s)?:\/\/[a-zA-Z\-\.\/?=#0-9&]{1,})\b|(\bwww\.[a-zA-Z\-\.\/?=#0-9&]{1,}\b)', text)
    urls = []
    for match in urls_raw_data:
        matched_url = next(filter(None, match), None)
        if matched_url:
            urls.append(matched_url)

    return urls

def find_phone_numbers(text):
    phone_numbers_raw_data = re.findall(r'(\(\d{1,3}\) \d{3}-\d{4})|(\d{3}[\.\-]{1}\d{3}[\.\-]{1}\d{4})|(\+\d{1,3} \d{2,5} \d{2,5} \d{2,5})|(\+\d{1,3} \d{2,5} \d{2,5})', text)
    phone_numbers = []
    for match in phone_numbers_raw_data:
        matched_phone_number = next(filter(None, match), None)
        if matched_phone_number:
            phone_numbers.append(matched_phone_number)

    return phone_numbers

def print_results(results):
    for result in results:
        print(result)

if __name__ == '__main__':
    # Find dates
    dates = find_dates(text)
    print_results(dates)

    # Find emails
    emails = find_emails(text)
    print_results(emails)

    # Find URLs
    urls = find_urls(text)
    print_results(urls)

    # Find phone numbers
    phone_numbers = find_phone_numbers(text)
    print_results(phone_numbers)

    # Parse HTML with XPath
    url = 'https://br.indeed.com/' # closed source website to parse data from it
    data = html_parse.parse_html_xpath(url)
