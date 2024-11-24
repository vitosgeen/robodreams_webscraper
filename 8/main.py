from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import json

from jobs_db import JobsDB

def parse_jobs_marksandspencer_com():
    print('parse_jobs_marksandspencer_com')
    
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    max_page = 2    
    wait = WebDriverWait(driver, 10)
    results = []
    for page in range(1, max_page + 1):
        url = f'https://jobs.marksandspencer.com/search-jobs?page={page}'
        driver.get(url)

        jobs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.ais-Hits ol.ais-Hits-list li.ais-Hits-item')))
        for job in jobs:
            title = job.find_element(By.CSS_SELECTOR, 'h3').text
            url = job.find_element(By.CSS_SELECTOR, 'a[data-track-trigger]').get_attribute('href')
            results.append({
                'title': title,
                'url': url
            })

    driver.quit()
    return results

    


if __name__ == '__main__':
    jobs_result = parse_jobs_marksandspencer_com()

    # Save to database
    jobs_db = JobsDB()
    for job in jobs_result:
        if not jobs_db.get_by_url(job['url']):
            jobs_db.insert(job['title'], job['url'])
    jobs_db.close()
    
    # save to json file
    with open('jobs.json', 'w') as f:
        json.dump(jobs_result, f)
        
    print('Done')