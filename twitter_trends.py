from twitter import Twitter
from twitter.oauth import OAuth
from pprint import pprint
import json

t = Twitter(auth=OAuth('708991765693370368-yNyHxdYpTPiJyGzN3K9b0Oj8GL9NZ2Z',
    'MfVXIFSEAFKWqQGnRfEw2WvFq16UYvvLZNmsSq9kEpQkK',
    'mMmsPD4bRZKYgtok2LdnlPNiB',
    'ZARKUezYoIw85Ggskn7HtdtJX88cIBF7QuOGydCTcLNJuE4TEm'))

# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/
WORLD_WOE_ID = 1
US_WOE_ID = 23424977
JAPAN_WOE_ID = 23424856

world_trends = t.trends.place(_id=WORLD_WOE_ID)
us_trends = t.trends.place(_id=US_WOE_ID)
jp_trends = t.trends.place(_id=JAPAN_WOE_ID)
world_trends_set = set(trend['name'] for trend in world_trends[0]['trends'])
us_trends_set = set(trend['name'] for trend in us_trends[0]['trends'])
jp_trends_set = set(trend['name'] for trend in jp_trends[0]['trends'])
us_jp_common_trend = us_trends_set.intersection(jp_trends_set)
us_world_common_trend = us_trends_set.intersection(world_trends_set)

# json ending with location and the trends startswith url
# pprint ending with list of trends and the trends startswith name
# personally I appreciate the result of pprint
# pprint(world_trends)
pprint(us_trends)
pprint(jp_trends)
# without indent the output would all in a line
# print(json.dumps(world_trends, indent=1))
# print(json.dumps(us_trends, indent=1))
# there no common trends between jp and us mainly because of the Japanese
# pprint(us_jp_common_trend)
pprint(us_world_common_trend)




