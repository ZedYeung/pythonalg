from twitter import Twitter
from twitter.oauth import OAuth
from pprint import pprint

t = Twitter(auth=OAuth('708991765693370368-yNyHxdYpTPiJyGzN3K9b0Oj8GL9NZ2Z',
    'MfVXIFSEAFKWqQGnRfEw2WvFq16UYvvLZNmsSq9kEpQkK',
    'mMmsPD4bRZKYgtok2LdnlPNiB',
    'ZARKUezYoIw85Ggskn7HtdtJX88cIBF7QuOGydCTcLNJuE4TEm'))

# Search for the latest tweets about #python
python_tweets = t.search.tweets(q='#python')
pprint(python_tweets)

# Get your "home" timeline
t.statuses.home_timeline()

# Get a particular friend's timeline  中文不行
t.statuses.user_timeline(screen_name="J.K. Rowling")

# to pass in GET/POST parameters, such as `count`
t.statuses.home_timeline(count=5)

# to pass in the GET/POST parameter `id` you need to use `_id`
t.statuses.oembed(_id=1234567890)

# Update your status
t.statuses.update(status="Who will buy twitter?")

# Send a direct message
t.direct_messages.new(
    user="billybob",
    text="I think yer swell!")

# Get the members of tamtar's list "Things That Are Rad"
t.lists.members(owner_screen_name="tamtar", slug="things-that-are-rad")

# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reason:
t.users.lookup(
    screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

# Overriding Method: GET/POST
# you should not need to use this method as this library properly
# detects whether GET or POST should be used, Nevertheless
# to force a particular method, use `_method`
t.statuses.oembed(_id=1234567890, _method='GET')

# Send images along with your tweets:
# - first just read images from the web or from files the regular way:
with open("example.png", "rb") as imagefile:
    imagedata = imagefile.read()
# - then upload medias one by one on Twitter's dedicated server
#   and collect each one's id:
t_up = Twitter(domain='upload.twitter.com',
               auth=OAuth(token, token_key, con_secret, con_secret_key))
id_img1 = t_up.media.upload(media=imagedata)["media_id_string"]
id_img2 = t_up.media.upload(media=imagedata)["media_id_string"]

# - finally send your tweet with the list of media ids:
t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))

# Or send a tweet with an image (or set a logo/banner similarily)
# using the old deprecated method that will probably disappear some day
params = {"media[]": imagedata, "status": "PTT ★"}
# Or for an image encoded as base64:
params = {"media[]": base64_image, "status": "PTT ★", "_base64": True}
t.statuses.update_with_media(**params)
