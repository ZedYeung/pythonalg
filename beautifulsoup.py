from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title('http://www.github.com')

if title == None:
    print('Title could not be found')
else:
    print(title)
# print(html.read())
# bsobj = BeautifulSoup(html.read())
# print(bsobj.h1)
# print(bsobj.body)

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsobj = BeautifulSoup(html)
namelist = bsobj.findAll('span', {'class': 'green'})
for name in namelist:
    print(name.get_text())
heading = bsobj.findAll({'h1', 'h2'})
print(heading.get_text())



