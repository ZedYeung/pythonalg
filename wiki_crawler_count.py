from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bsobj = BeautifulSoup(html)
count_all = 0
for link in bsobj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        count_all += 1
print(count_all)

count = 0
for link in bsobj.find('div', {'id': 'bodyContent'}).findAll('a', {'href': re.compile('^(/wiki/)((?!:).)*$')}):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        count += 1
print(count)


