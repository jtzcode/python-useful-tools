import sys, webbrowser, bs4, requests

res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
#print(res.text)

print('Googling results for you...Keywords: ' + ' '.join(sys.argv[1:]))
soup = bs4.BeautifulSoup(res.text, features='html.parser')
linkElements = soup.select('a')

numToOpen = min(5, len(linkElements))

print("Will open %s pages as results" % numToOpen)
for i in range(numToOpen):
    webbrowser.open('https://google.com' + linkElements[i].get('href'))