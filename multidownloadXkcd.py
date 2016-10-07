#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
import os
import requests
import bs4
import threading
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd


def download_xkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        html = requests.get('http://xkcd.com/%s' % (urlNumber))
        html.raise_for_status()

        soup = bs4.BeautifulSoup(html.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            html = requests.get(comicUrl)
            html.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in html.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects.
downloadThreads = [] # a list of all the Thread objects
for i in range(0, 1800, 100): # loops 18 times, creates 18 threads, for there're 1700+ comic now
    downloadThread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
