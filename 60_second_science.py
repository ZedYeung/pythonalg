#! python3
# download 60_second_science mp3 and transcript.

import requests
import os
from bs4 import BeautifulSoup
import threading

url = 'https://www.scientificamerican.com/podcast/60-second-science/'
os.makedirs(r'F:\Fighting\60_second_science', exist_ok=True)   # store mp3 and transcript in ./60_second_science
os.chdir(r'F:\Fighting\60_second_science')
os.makedirs('mp3', exist_ok=True)
os.makedirs('Transcript', exist_ok=True)


def get_html(url):
	html = requests.get(url)
	try:
		html.raise_for_status()
	except Exception as e:
		print('There was a problem: %s' % e)
	return html


def download_science(startPage, endPage):
	for urlNumber in range(startPage, endPage):
		# Download the page.
		print('Downloading page https://www.scientificamerican.com/podcast/60-second-science/?page=%s...' % urlNumber)
		html = get_html('https://www.scientificamerican.com/podcast/60-second-science/?page=' + str(urlNumber))

		soup = BeautifulSoup(html.text, 'html.parser')

		# Find the URL of the comic image.
		content_urls = soup.select('h3 a')
		if content_urls == []:
			print('Could not find resource.')
		else:
			# There are 17 radios per page
			for i in range(17):
				content_url = content_urls[i].get('href')
				title = content_urls[i].getText()
				title = title.replace(': ', '-').replace(' ', '_').replace('\"', '\'').replace('?', '')
				html = get_html(content_url)
				soup = BeautifulSoup(html.text, 'html.parser')

				# Download the mp3 and save to ./60_second_science/mp3
				mp3_url = 'https://www.scientificamerican.com' \
						+ soup.select('div[class=tooltip-outer] a')[0].get('href')
				print('Downloading mp3 of %s...' % title)
				mp3 = get_html(mp3_url)
				with open(os.path.join('mp3', title + '.mp3'), 'wb') as mp3_file:
					for chunk in mp3.iter_content(100000):
						mp3_file.write(chunk)

				# Download the Transcript and save to ./60_second_science/Transcript
				print('Downloading transcript of %s...' % title)
				with open(os.path.join('Transcript', title + '.txt'), 'wb') as transcript_file:
					transcript = soup.select('div[class=transcript__inner]')[0].getText() # modified: only take text in <p>
					transcript_file.write(transcript.encode('utf-8'))
	print('Done.')

if __name__ == '__main__':
	download_science(6, )





