import requests
import re
import csv
import pandas as pd
import os
from pandas import DataFrame
from bs4 import BeautifulSoup

base_url = 'https://au.indeed.com/jobs?q=sql&l=Carlingford+NSW'
indeed_url = 'http://indeed.com'
job_urls = []

filename = input('Enter output filename:')
def clean_html(raw_html):
    cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleaner, '', raw_html)
    return cleantext

def print_progress_bar(iteration, total, prefix="", suffix="", length=30, fill="=", head=">", track="."):
    filled_length = int(length * iteration // total)
    if filled_length == 0:
        bar = track * length
    elif filled_length == 1:
        bar = head + track * (length - 1)
    elif filled_length == length:
        bar = fill * filled_length
    else:
        bar = fill * (filled_length-1) + ">" + "." * (length-filled_length)
    print("\r" + prefix + "[" + bar + "] " + str(iteration) + "/" + str(total), suffix, end = "\r")
    if iteration == total: 
        print()

pgno_ext = "&start="
pages = 19
print("Scraping job URLs...")
for i in range(1,pages):
    response = requests.get(base_url + pgno_ext + str(10*i))
    print_progress_bar(i+1,pages)
    #print(base_url + pgno_ext + str(10*i))
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_="title")
    for i in items:
        link = i.find('a', class_="jobtitle turnstileLink")
        if link.has_attr('href'):
            job_url = link.attrs['href']
            job_urls.append(job_url)
            
        
count = 0
prev_text = ''
print("Scraping job information...")
print_progress_bar(0,len(job_urls))
with open(filename +'.csv',mode='w', newline='') as job_file:
    file_writer = csv.writer(job_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['CompanyName','JobDesc'])
    for index,jobs in enumerate(job_urls):
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
        if prev_text != text:
            file_writer.writerow([company,text])
        prev_text  = text
        print_progress_bar(count+1,len(job_urls))
        count+=1

df = pd.read_csv(filename+'.csv', encoding='ISO-8859-1')

df.to_csv(filename + '_cleaned.csv', index=False, header=True)


                    

        
