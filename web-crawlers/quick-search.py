import sys, webbrowser, bs4, requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()
#print(res.text)

print('Googling results for you...Keywords: ' + ' '.join(sys.argv[1:]))
soup = bs4.BeautifulSoup(res.text, features='html.parser')
linkElements = soup.select('.rc a')

numToOpen = min(5, len(linkElements))

print("Will open %s pages as results" % numToOpen)
for i in range(numToOpen):
    webbrowser.open(linkElements[i].get('href'))