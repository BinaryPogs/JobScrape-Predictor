import os
from bs4 import BeautifulSoup
import requests
import re

def clean_html(raw_html):
    cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleaner, '', raw_html)
    return cleantext.split('\n')

def getJobDesc(title):
    text = []
    items = soup.find_all('div',class_='jobsearch-jobDescriptionText')
    for i in items:
        tag = i.find_all('ul')
        for i in tag:
            text.append(clean_html(str(i)))
    return text

base_url = 'https://www.indeed.com/viewjob?jk=c7612ac1efc3f60c&from=serp&vjs=3'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.find_all('div',class_='jobsearch-JobInfoHeader-title-container')
for title in titles:
    job_title = title.find('h3',class_="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title").text.strip('\n')
    print(getJobDesc(title))
    print(job_title)





