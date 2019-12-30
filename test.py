import os
from bs4 import BeautifulSoup
import requests

base_url = 'https://www.indeed.com/viewjob?jk=c7612ac1efc3f60c&from=serp&vjs=3'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.find_all('div',class_='jobsearch-JobInfoHeader-title-container')
for title in titles:
    job_title = title.find('h3',class_="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title").text.strip('\n')

print(job_title)