from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import datetime

pages = set()
random.seed(datetime.datetime.now())


def get_internal_links(bsobj, inurl):
    # domain = urlparse(inurl).scheme + "://" + urlparse(inurl).netloc
    internal_links = []
    # Finds all links that begin with a "/"
    # regular expression is decided by href
    # for link in bsobj.findAll("a", {'href': re.compile("^(/|.*" + domain + ")")}):
    for link in bsobj.findAll("a", {'href': re.compile("^/(.*)")}):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                if link.attrs['href'].startswith("/"):
                    # concatenate url
                    internal_links.append(inurl + link.attrs['href'])
                else:
                    internal_links.append(link.attrs['href'])
    return internal_links


def get_external_links(bsobj, exurl):
    external_links = []
    # regular expression is decided by href
    # for link in bsobj.findAll('a', {'href': re.compile('^(https?|www)((?!' + exurl +').)*$')}):
    for link in bsobj.findAll('a', {'href': re.compile('^(https?|www)(?!' + exurl + ').*$')}):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])
    return external_links


def get_random_external_link(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html, 'html.parser')
    external_links = get_external_links(bsobj, urlparse(url).netloc)
    if len(external_links) == 0:
        print('no external link, looking around the site for one')
        domain = urlparse(url).scheme + '://' + urlparse(url).netloc
        internal_links = get_external_links(bsobj, domain)
        return get_random_external_link(internal_links[random.randint(0, len(internal_links) - 1)])
    else:
        return external_links[random.randint(0, len(external_links) - 1)]


def follow_random_external_link(url):
    external_link = get_random_external_link(url)
    print("Random external link is: " + external_link)
    follow_random_external_link(external_link)

# Collects a list of all external URLs found on the site
all_external_links = set()
all_internal_links = set()


def get_all_external_links(url):
    html = urlopen(url)
    domain = urlparse(url).scheme+"://"+urlparse(url).netloc
    netloc = urlparse(url).netloc
    bsobj = BeautifulSoup(html, "html.parser")
    internal_links = get_internal_links(bsobj, domain)
    external_links = get_external_links(bsobj, netloc)

    for link in external_links:
        if link not in all_external_links:
            all_external_links.add(link)
            print(link)

    for link in internal_links:
        if link not in all_internal_links:
            all_internal_links.add(link)
            get_all_external_links(link)

if __name__ == '__main__':
    get_all_external_links('https://www.huxiu.com/article/164311.html')
#   get_all_external_links('https://www.huxiu.com/')
#   follow_random_external_link('https://www.huxiu.com/')
#   follow_random_external_link('http://36kr.com/')
#   links = get_external_links(bsobj, exurl)
#   for link in links:
#       print(link)



