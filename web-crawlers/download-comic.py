import os, bs4, requests
url = 'https://xkcd.com'

os.makedirs('xkcd_comic', exist_ok=True)
while not url.endswith('#'):
    print('Downloading the page: %s' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    comic = soup.select('#comic img')
    if comic == []:
        print('No comic image.')
    else:
        comicUrl = 'http:' + comic[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
    imageFile = open(os.path.join('xkcd_comic', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Dowloading completed.')