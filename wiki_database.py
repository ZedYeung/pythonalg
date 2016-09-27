from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mysql', charset='utf8')
cursor=conn.cursor()
cursor.execute('use scraping')

random.seed(datetime.datetime.now())


def store(title, content):
    cursor.execute('insert into pages (title,content) values (\"%s\",\"%s\")', (title, content))
    cursor.connection.commit()


def get_links(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bs = BeautifulSoup(html, "html.parser")
    title = bs.find("h1").get_text()
    content = bs.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bs.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = get_links("/wiki/Abraham_Lincoln")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        links = get_links(newArticle)
finally:
    cursor.close()
    conn.close()



