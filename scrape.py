import requests
from bs4 import BeautifulSoup

url = 'https://au.indeed.com/jobs?q=sql&l=Carlingford+NSW'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_="title")
for i in items:
name = i.find('a', class_='jobtitle turnstileLink').text.strip('\n')
print(name)