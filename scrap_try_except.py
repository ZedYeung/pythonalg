from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
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