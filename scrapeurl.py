import requests
import re
from bs4 import BeautifulSoup

base_url = 'https://au.indeed.com/jobs?q=sql&l=Carlingford+NSW'
indeed_url = 'http://indeed.com'
job_urls = []

def cleanhtml(raw_html):
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
    response = requests.get(indeed_url + jobs)
    soup = BeautifulSoup(response.text,'lxml')
    items = soup.find_all('div',class_='jobsearch-jobDescriptionText')
    for i in items:
        text = cleanhtml(str(i))
        print(text)

