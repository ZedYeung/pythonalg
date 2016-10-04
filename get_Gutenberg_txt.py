import requests
html = requests.get('https://Gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    html.raise_for_status()
except Exception as e:
    print('There was a problem: %s' % e)
text = html.text
print('text len:' + str(len(text)))
print(text[:1000])

with open('RomeoAndJuliet.txt', 'wb') as text_file:
    for chunk in html.iter_content(100000):
        text_file.write(chunk)



