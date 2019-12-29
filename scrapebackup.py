import requests
import re
import csv
from bs4 import BeautifulSoup

base_url = 'https://au.indeed.com/jobs?q=sql&l=Carlingford+NSW'
indeed_url = 'http://indeed.com'
job_urls = []

def clean_html(raw_html):
    cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleaner, '', raw_html)
    return cleantext

pgno_ext = "&start="
for i in range(1,19):
    response = requests.get(base_url + pgno_ext + str(10*i))
    #print(base_url + pgno_ext + str(10*i))
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_="title")
    for i in items:
        link = i.find('a', class_="jobtitle turnstileLink")
        if link.has_attr('href'):
            job_url = link.attrs['href']
            job_urls.append(job_url)

for jobs in job_urls:
    curr_url = indeed_url + jobs
    response = requests.get(curr_url)
    soup = BeautifulSoup(response.text,'lxml')
    items = soup.find_all('div',class_='jobsearch-jobDescriptionText')
    heading = soup.find_all('div',class_='icl-NavigableContainer-innerContainer')
    for h in heading:
        text = []
        company = h.find('h4', class_='jobsearch-CompanyReview--heading').text.strip('\n')
        for i in items:
            tag = i.find_all('ul')
            for i in tag:
                text.append(clean_html(str(i)))
            print(company,text)
            
                    
        
                #print(curr_url)
        
