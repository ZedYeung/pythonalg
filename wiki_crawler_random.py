from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())
def get_links(url):
    html = urlopen('https://en.wikipedia.org/' + url)
    bsobj = BeautifulSoup(html, 'html.parser')
    return bsobj.find('div', {'id': 'bodyContent'}).findAll('a', {'href': re.compile('^(/wiki/)((?!:).)*$')})

links = get_links('')

while len(links) > 0:
    new_url = links[random.randint(0,len(links) - 1)].attrs['href']
    print(new_url)
    links = get_links(new_url)


