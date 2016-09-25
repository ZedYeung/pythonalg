from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
from collections import Counter
import re
import string
from collections import OrderedDict


def clean_input(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', ' ', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    clean_input = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower == 'a' or item.lower == 'i'):
            clean_input.append(item)
    return clean_input


def ngrams(input, n):
    input = clean_input(input)
    output = {}
    for i in range(len(input) - n + 1):
        new_ngram = ' '.join(input[i: i+n])
        if new_ngram in output:
            output[new_ngram]+=1
        else:
            output[new_ngram]=1
    return output

# html = urlopen('http://en.wikipedia.org/wiki/Abraham_Lincoln')
html = urlopen('http://en.wikipedia.org/wiki/Trump')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id': 'mw-content-text'}).get_text()

ngrams = ngrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
pprint(ngrams)

# c = Counter(ngrams)
# pprint(c[:20])

print('2-grams count is:' + str(len(ngrams)))

