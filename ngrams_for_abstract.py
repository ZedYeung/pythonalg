# main problem is the data structure use both list and dict
# sometimes it's confusing that the input and ouput are different type
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import operator
import string
import re


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    # without split it will become letter one by one
    words = ngram.split(' ')
    for word in words:
        # print(word)
        if word not in commonWords:
            return False
        return True

# text cleaning
def cleanText(input):
    input = re.sub('\n+', " ", input).lower()
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = re.sub("u\.s\.", "us", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    return input

def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def no_common_word_ngrams(input, n):
    ngrams = getNgrams(input, n)
    ngrams = [ngram for ngram in ngrams.items() if not isCommon(ngram[0])]
    # ngrams = list(filter(lambda ngram: not isCommon(ngram[0]), ngrams.items()))
    return ngrams

"""
# use dict at first time, but finally decide to use list
def del_low_freq_ngrams(input, threshold):
    filter_value = list(filter(lambda item: item[1]>threshold, list(input.items())))
    return filter_value
"""


def del_low_freq_ngrams(input, threshold):
    filter_value = [ngram for ngram in input if ngram[1]>threshold]
    # filter_value = list(filter(lambda ngram: ngram[1]>threshold, input))
    return filter_value


def getNgrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngram = " ".join(input[i:i+n])
        if ngram not in output:
            output[ngram] = 0
        output[ngram] += 1
    return output


# get topic sentence
def getFirstSentenceContaining(ngram, content):
    sentences = content.split(".")
    for sentence in sentences:
        if ngram in sentence:
            return sentence
    return ""


# use first n ngrams
def get_topic_sentence(content, sorted_ngrams,  first_n_ngrams):
    for ngram in sorted_ngrams[:first_n_ngrams]:
        sentence = getFirstSentenceContaining(ngram[0], content)
        print(sentence)

content = str(urlopen("http://pythonscraping.com/files/space.txt").read(), 'utf-8')
clean_content = cleanText(content)
# ngrams = getNgrams(content, 2)
ngrams = no_common_word_ngrams(content, 2)
ngrams = del_low_freq_ngrams(ngrams, 3)
sorted_ngrams = sorted(ngrams, key=operator.itemgetter(1), reverse = True)
pprint(sorted_ngrams)

print('Use the ngrams to get topic sentence:')
get_topic_sentence(clean_content, sorted_ngrams, 5)
