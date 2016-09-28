from twitter import Twitter
from twitter.oauth import OAuth
from collections import Counter
from pprint import pprint
from prettytable import PrettyTable
import json

t = Twitter(auth=OAuth('708991765693370368-yNyHxdYpTPiJyGzN3K9b0Oj8GL9NZ2Z',
    'MfVXIFSEAFKWqQGnRfEw2WvFq16UYvvLZNmsSq9kEpQkK',
    'mMmsPD4bRZKYgtok2LdnlPNiB',
    'ZARKUezYoIw85Ggskn7HtdtJX88cIBF7QuOGydCTcLNJuE4TEm'))
# Search for the latest tweets about #something
q = '#ThingsHillaryGoogles'
# show how many results
count = 100
# The Twitter Search API only searches Tweets published in the past 7 days.
# the Search API is focused on relevance but not completeness
# you should use a Streaming API instead for completeness
search_tweets = t.search.tweets(q=q, count=count)
# the print is ridiculously complicated
# pprint(search_tweets)

statuses = search_tweets['statuses']
# Why use for iterate
# because twitter timelines are constantly adding new tweets to front
# https://dev.twitter.com/rest/public/timelines
for _ in range(5):
    print('Length of statuses:', len(statuses))
    try:
        next_results = search_tweets['search_metadata']['next_results']
    except KeyError as e:
        print('No more result when next_results does not exist')
        break
# ?max_id=778486882464206847&q=%23ThingsHillaryGoogles&count=10&include_entities=1
    kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
    kwargs_search_tweets = t.search.tweets(**kwargs)
    statuses += kwargs_search_tweets['statuses']

# print(json.dumps(statuses[0], indent=1))

# collect the text, screen_names and hashtags
status_texts = [status['text'] for status in statuses]

screen_names = [user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags']]

# Compute a collection of all words from all tweets
words = [word for text in status_texts for word in text.split()]

# Explore the first n items for each...
pprint(status_texts[0:10])
pprint(screen_names[0:10])
pprint(hashtags[0:10])
pprint(words[5:15])

# search most_common
for item in [words]:
    c = Counter(item)
    # top  10 common
    pprint(c.most_common()[9:15])

for label, data in (('Word', words),
                    ('Screen Name', screen_names),
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:10]]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print(pt)

# A function for computing lexical diversity
def lexical_diversity(tokens):
    return len(set(tokens))/len(tokens)

# A function for computing the average number of words per tweet
def average_words(statuses):
    total_words = sum([len(status.split()) for status in statuses ])
    return total_words/len(statuses)

print(lexical_diversity(words))
print(average_words(status_texts))
# print(lexical_diversity(screen_names))
# print(lexical_diversity(hashtags))

retweets = [
    # Store out a tuple of these three values ...
    (status['retweet_count'],
     status['retweeted_status']['user']['screen_name'],
     status['text'])
    # ... for each status ...
    for status in statuses
    # ... so long as the status meets this condition.
    if 'retweeted_status' in status
    ]

# Slice off the first 5 from the sorted results and display each item in the tuple
pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[pt.add_row(row) for row in sorted(retweets, reverse=True)[:5]]
pt.max_width['Text'] = 50
pt.align = 'l'
print(pt)




